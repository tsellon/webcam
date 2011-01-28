from VideoCapture import Device
from time import sleep
import Image
import ImageFilter
import ImageChops

cam = Device()
cam.setResolution(640,480)

for ii in range(10):
    im = cam.getImage()
    im2 = im.filter(ImageFilter.FIND_EDGES)
    im2 = im2.filter(ImageFilter.BLUR)
    im = ImageChops.darker(im,im2)
    im.save('%i.jpg' % ii)
    sleep(1)
