from VideoCapture import Device
from time import sleep
import Image
import ImageFilter
import ImageChops
import ImageOps

cam = Device()
cam.setResolution(640,480)

def main():
    for ii in range(10):
        im = cam.getImage()
        im = ApplyFilterSet2(im)
        im.save('%i.jpg' % ii)
        sleep(1)

def ApplyFilterSet1(im):
    im2 = im.filter(ImageFilter.FIND_EDGES)
    im2 = im2.filter(ImageFilter.BLUR)
    im = ImageChops.multiply(im,im2)
    return im

def ApplyFilterSet2(im):
    im2 = im.filter(ImageFilter.FIND_EDGES)
    im = ImageOps.solarize(im)
    im = ImageChops.difference(im,im2)
    return im

if __name__ == "__main__":
    main()
