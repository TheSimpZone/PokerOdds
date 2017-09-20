from VideoCapture import Device
from PIL import Image
prefix = 'card'
increasing = 0
mainimagename = prefix + str(increasing) +'.jpg'
inde = input()
while inde != 'q':
    Device().saveSnapshot(mainimagename)
    img = Image.open(mainimagename).resize((640,480),Image.BILINEAR)
    img.save(mainimagename)
    img.close()
    increasing+=1
    mainimagename = prefix + str(increasing) +'.jpg'
    inde = input()