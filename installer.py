import os
import time
os.system('cls')
global dld
with open('urls.txt') as file:
    lines = [line.rstrip() for line in file]
for x in range (0,len(lines)):
    dld = x+1
    os.system(f'curl -s {lines[x]} -O')
    print(f'Downloading {dld}/{len(lines)}',end='\r',flush=True)
print(f'Done! Downloaded {dld}/{len(lines)} mods!')
time.sleep(5)
