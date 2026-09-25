import re

with open('lh_parseserver_real.c', encoding='utf-8') as f:
    txt = f.read()

fields = sorted(list(set(re.findall(r'"([a-zA-Z0-9_]+)"', txt))))
print('Fields in parseServer:')
for f in fields:
    print(' -', f)
