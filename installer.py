import os
import time
import sys
import socket
#update the shit
path = ''
for x in range(0,len(sys.argv)):
    if x != 0:
        path += str(sys.argv[x]) + ' '
path = path.replace("'",'')
os.system('cd modinstaller-files && if not exist updater.py curl -s https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/updater.py -O')
os.system(f'cd modinstaller-files && start /wait /b python updater.py {path}')

#actually start code here, so it doesnt conflict with the updater!!!!!





global lines
import progressbar
#check system#
if os.name == 'nt':
    pass
else:
    print('Cannot run on linux!')
    quit()
dld=0
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
        os.system('curl -s https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/mods/OptiFine_1.19.2_HD_U_H9_MOD.jar --output optifine.jar')
    elif of == 'n':
        pass
    else:
        os.system('cls')
        of_check()
def backup_old():
    backup = input('Backup old mods? (Y/N): ').lower()
    if backup == 'y':
        filename = time.strftime("%Y%m%d%H%M%S")
        os.system(f'if exist *.jar mkdir mods-old-{filename} && copy *.jar mods-old-{filename} && del *.jar && cls')
        print(f'Backup successful. Saved mods to "mods-old-{filename}"')
    elif backup == 'n':
        os.system('if exist *.jar del *.jar && cls')
    else:
        os.system('cls')
        backup_old()
backup_old()
of_check()
with progressbar.ProgressBar(max_value=total) as bar:
    for x in range (0,len(lines)):
        dld+=1
        bar.update(dld)
        os.system(f'curl -s {lines[x]} -O')
print(f'Done! Downloaded {dld}/{total} mods!')
addr = socket.gethostbyname('polar.crabdance.com')+":25565"
print("Current Server IP: "+addr)
time.sleep(10)
