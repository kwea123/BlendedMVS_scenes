import os

s = '|'
for i, img in enumerate(sorted(os.listdir('sculpture'))):
    s += img.split('.')[0]+f'![](sculpture/{img})|'
    if i%8==7:
        print(s)
        s = '|'
print(s)
