lines = open(r'G:\My Drive\QWAV\BACKLOG.md', 'r', encoding='utf-8').readlines()
for i, l in enumerate(lines):
    if 'P50' in l and 'D13' in l:
        # Strip emoji for console safety
        out = l.rstrip().encode('ascii', errors='replace').decode('ascii')
        print(f'Line {i+1}: {out[:200]}')

