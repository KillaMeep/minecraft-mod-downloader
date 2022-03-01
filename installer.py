import os
import time
global dld
global lines
global total
with open('urls.txt') as file:
    lines = [line.rstrip() for line in file]
of = input('Install Optifine? (Y/N): ').lower()
total = len(lines)
if of == 'y':
    total+=1
    os.system('curl -s https://optifine.net/download?f=OptiFine_1.18.1_HD_U_H4.jar --output optifine.jar')
    dld = 1
for x in range (0,len(lines)):
    dld+=1
    os.system(f'curl -s {lines[x]} -O')
    print(f'Downloading {dld}/{total}',end='\r',flush=True)
print(f'Done! Downloaded {dld}/{total} mods!')
time.sleep(5)
