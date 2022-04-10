import hashlib
import requests
import os
import sys
os.system('pip install --upgrade pip --quiet')
path = ''
for x in range(0,len(sys.argv)):
    if x != 0:
        path += str(sys.argv[x]) + ' '
path = path.replace("'",'')
os.chdir(path)

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
def update():
    os.system('del modinstaller.bat')
    os.system('curl -s https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/modinstaller.bat -O')
    os.system('cls')
    input('Update complete. Press any key to continue...')
    os.system('exit')
def check_for_update():
    upd_check = input('Update available! Do you want to install it? (Y/N): ').lower()
    if upd_check == 'y':
        update()
    elif upd_check == 'n':
        pass
    else:
        os.system('cls')
        check_for_update()

local = md5Checksum("modinstaller.bat",None)
remote = md5Checksum(None,"https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/modinstaller.bat")
if local != remote:
    check_for_update()





