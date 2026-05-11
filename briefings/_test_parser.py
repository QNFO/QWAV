import re

def parse_inline(text):
    result = []
    remaining = text
    while remaining:
        # Display math
        m = re.match(r'(.*?)\$\$(.+?)\$\$', remaining, re.DOTALL)
        if m:
            if m.group(1): result.append(('text', m.group(1)))
            result.append(('display_math', m.group(2)))
            remaining = remaining[m.end():]
            continue
        # Inline math
        m = re.match(r'(.*?)(?:(?<!\\)\$)(.+?)(?:(?<!\\)\$)', remaining)
        if m and m.group(2):
            if m.group(1): result.append(('text', m.group(1)))
            result.append(('math', m.group(2)))
            remaining = remaining[m.end():]
            continue
        # Link
        m = re.match(r'(.*?)\[(.+?)\]\((.+?)\)', remaining)
        if m:
            if m.group(1): result.append(('text', m.group(1)))
            result.append(('link', m.group(2), m.group(3)))
            remaining = remaining[m.end():]
            continue
        # Bold
        m = re.match(r'(.*?)\*\*(.+?)\*\*', remaining)
        if m:
            if m.group(1): result.append(('text', m.group(1)))
            result.append(('bold', m.group(2)))
            remaining = remaining[m.end():]
            continue
        # Italic
        m = re.match(r'(.*?)\*(.+?)\*', remaining)
        if m:
            if m.group(1): result.append(('text', m.group(1)))
            result.append(('italic', m.group(2)))
            remaining = remaining[m.end():]
            continue
        # Code
        m = re.match(r'(.*?)`(.+?)`', remaining)
        if m:
            if m.group(1): result.append(('text', m.group(1)))
            result.append(('code', m.group(2)))
            remaining = remaining[m.end():]
            continue
        result.append(('text', remaining))
        break
    return result

# Test with a simplified version
test = 'In a Bruhat-Tits tree encoding of depth $d$ over $\\mathbb{Q}_p$, with physical error rate $p_{\\text{err}}$ per leaf qubit.'
print('Input:', test)
tokens = parse_inline(test)
for tok in tokens:
    print(f'  {tok[0]}: {repr(tok[1]) if len(tok)>1 else ""}')
