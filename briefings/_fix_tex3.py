path = r"G:\My Drive\projects\QWAV\briefings\convert_agenda.py"
with open(path, 'rb') as f:
    content = f.read()

# The problematic bytes are: 27 5c 27 which is '\' (broken)
# We need: 27 5c 5c 27 which is '\\' (correct Python escaping for string '\')
# Pattern to find: lines.append('  \  ' + cmd + '{' + text + '}')
# Need to replace: lines.append('  \  \  ' + cmd + '{' + text + '}')

old = b"lines.append('\\' + cmd + '{' + text + '}')"
new = b"lines.append('\\\\' + cmd + '{' + text + '}')"

print(f"Old bytes: {old.hex()}")
print(f"New bytes: {new.hex()}")

if old in content:
    content = content.replace(old, new)
    with open(path, 'wb') as f:
        f.write(content)
    print("Replaced successfully")
else:
    print(f"Old pattern not found. Searching for alternatives...")
    # Search for the line
    for i, line in enumerate(content.split(b'\n')):
        if b'cmd' in line and b'lines' in line:
            print(f"Line {i}: {line}")
