import os
import time
with open('urls.txt') as file:
    lines = [line.rstrip() for line in file]
for x in range (0,len(lines)):
    os.system(f'curl -s {lines[x]} -O')
    print(f'Downloading {x}/{len(lines)}',end='',flush=True)
print(f'Done! Downloaded {len(lines)} mods!')
time.sleep(5)
