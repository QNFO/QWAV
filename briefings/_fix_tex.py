import os
path = r"G:\My Drive\projects\QWAV\briefings\convert_agenda.py"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# The source file has: lines.append('\\\\' + cmd + '{' + text + '}')
# In the source, \\\\ represents two escaped backslashes, giving the string \\
# We want a single backslash: \\ in source gives string \
# So in source: '\\' evaluates to the string \

old = "lines.append('\\\\' + cmd + '{' + text + '}')"
new = "lines.append('\\\\' + cmd + '{' + text + '}')"  # Actually we want single backslash...

# Wait, let me think about this more carefully.
# The file literally contains: lines.append('\\\\' + cmd + '{' + text + '}')
# In the file as raw text, that's: lines.append(' (backslash)(backslash) ' + cmd...
# In Python, '\\\\' is a string of two characters: \ and \
# But we want the string \ (single backslash), which in Python source is '\\'

# So in the file, I want: lines.append('\\' + cmd + '{' + text + '}')

old = "lines.append('\\\\' + cmd + '{' + text + '}')"
new = "lines.append('\\' + cmd + '{' + text + '}')"

# Let me check what's actually in the file
for i, line in enumerate(content.split('\n')):
    if 'lines.append' in line and 'cmd' in line:
        print(f'Line {i}: {repr(line)}')
        if old in line:
            print('  MATCH! Replacing...')
            content = content.replace(line, line.replace(old, new))
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print('  DONE')
        else:
            print('  NO MATCH. Trying alternative...')
            # Try to fix by replacing the first \\\\ with \\
            fixed = line.replace("'\\\\' + cmd", "'\\\\' + cmd")
            print(f'  Fixed: {repr(fixed)}')
