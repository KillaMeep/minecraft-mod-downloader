import os
import time
import sys
global lines
#check system#
if os.name == 'nt':
    pass
else:
    print('Cannot run on linux!')
    quit()


path = ''
for x in range(0,len(sys.argv)):
    if x != 0:
        path += str(sys.argv[x]) + ' '
path = path.replace("'",'')
dld=0
os.system('cd modinstaller-files && if not exist updater.py curl -s https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/updater.py -O')
os.system(f'cd modinstaller-files && start /wait python updater.py {path}')

with open('urls.txt') as file:
    lines = [line.rstrip() for line in file]
total = len(lines)
def of_check():
    global total
    global dld
    of = input('Install Optifine? (Y/N): ').lower()
    if of == 'y':
        total+=1
        dld+=1
        os.system('curl -s https://optifine.net/download?f=OptiFine_1.18.1_HD_U_H4.jar --output optifine.jar')
    elif of == 'n':
        pass
    else:
        os.system('cls')
        of_check()
of_check()
for x in range (0,len(lines)):
    dld+=1
    os.system(f'curl -s {lines[x]} -O')
    print(f'Downloading {dld}/{total}',end='\r',flush=True)
print(f'Done! Downloaded {dld}/{total} mods!')
time.sleep(5)
