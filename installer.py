import os
with open('urls.txt') as file:
    lines = [line.rstrip() for line in file]
for x in range (0,len(lines)):
    os.system(f'curl -s {lines[x]} -O')