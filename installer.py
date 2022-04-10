import os
import time
import hashlib
import requests


#check system#
if os.name == 'nt':
    pass
else:
    print('Cannot run on linux!')
    quit()

def md5Checksum(filePath,url):
    m = hashlib.md5()
    if url==None:
        with open(filePath, 'rb') as fh:
            m = hashlib.md5()
            while True:
                data = fh.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()
    else:
        r = requests.get(url)
        for data in r.iter_content(8192):
             m.update(data)
        return m.hexdigest()

local = md5Checksum("modinstaller.bat",None)
remote = md5Checksum(None,"https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/modinstaller.bat")
def update():
    os.system('del modinstaller.bat')
    os.system('curl -s https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/modinstaller.bat -O')
    os.system('start modinstaller.bat')
    os.system('exit')


#update modinstaller.bat
if local != remote:
    update()
    quit()
else:
    pass
global lines



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
