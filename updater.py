import hashlib
import requests
import os
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
if local != remote:
    os.system('del modinstaller.bat')
    os.system('curl -s https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/modinstaller.bat -O')
    os.system('modinstaller.bat')
    os.system('exit')
else:
    pass