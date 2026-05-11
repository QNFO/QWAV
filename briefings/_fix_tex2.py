import re

path = r"G:\My Drive\projects\QWAV\briefings\convert_agenda.py"
with open(path, 'rb') as f:
    content = f.read()

# Show the problematic line in hex
lines = content.split(b'\n')
for i, line in enumerate(lines):
    if b'lines.append' in line and b'cmd' in line:
        print(f'Line {i}: {line}')
        print(f'  Hex: {line.hex()}')

# Fix: replace the line with proper escaping
# We need the line to be: lines.append('\\' + cmd + '{' + text + '}')
# In the file, this should be:  lines.append('\' + cmd + '{' + text + '}')
# Wait, no. In Python source, to produce string '\', we write '\\' (two backslashes in source)
# The byte sequence should be: 27 5c 5c 27  (that's ' \ \ ')
# Let me look at the actual bytes

# OK looking at the output, the line currently has issues
# Let me just rewrite the whole line
old_line = lines[i]
# New line with proper Python escaping: '\\' in source gives string '\'
new_line = b"            lines.append('\\\\' + cmd + '{' + text + '}')"
# Wait, in bytes, \\\\ means two literal backslashes in the replacement string
# We want four bytes: 27 5c 5c 27 which is '\\' in the source file, giving string '\' in Python

# Actually let me just directly construct:
# In the source file, '\\' = 4 bytes: 0x27 0x5c 0x5c 0x27
# In Python, this is the string '\'
# So the source should literally have two backslashes between single quotes

new_line = b"            lines.append('\\' + cmd + '{' + text + '}')".replace(b"'\\\\'", b"'\\\\'")
# Hmm this is circular

# Let me just write the correct bytes directly
# The source file should contain: lines.append('\' + cmd + '{' + text + '}')
# No wait. In the source file, the text is: lines.append('\\' + cmd + '{' + text + '}')
# That's 4 chars between single quotes: \ \  (two backslashes)
# In hex: 27 5c 5c 27

correct_line = b"            lines.append('\\' + cmd + '{' + text + '}')"
# But this has 2 backslashes between quotes, which in Python source is '\\' (escaped backslash)
# Wait - in a bytes literal, b'\\' is TWO bytes: 0x5c 0x5c. 
# In a Python string literal (not bytes), '\\' is also two characters in source, one in runtime.
# So yes, b"            lines.append('\\' + cmd + '{' + text + '}')" 
# gives us the right bytes for the source file.

print(f'New line bytes: {correct_line}')
print(f'New line hex: {correct_line.hex()}')

content = content.replace(old_line, correct_line)
with open(path, 'wb') as f:
    f.write(content)
print('Fixed.')
