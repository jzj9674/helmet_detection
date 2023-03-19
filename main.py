from detect import main as detect_main
import shutil
import os

for path in os.listdir('./input'):
    os.remove('./input/{}'.format(path))
for path in os.listdir('./res'):
    os.remove('./res/{}'.format(path))
img = '1.jpg'
shutil.copyfile(img,'./input/input.jpg')
detect_main()