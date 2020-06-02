from ppadb.client import Client
import numpy
from PIL import Image, ImageGrab


adb=Client(host="127.0.0.1", port=5037)
devices=adb.devices()

device=devices[0]

#device.shell("input tap 500 500")
while(True):
    image=ImageGrab.grab(bbox=None)

    #im=numpy.array(image, dtype=numpy.uint8)
    #for i in im:
     #   print (i)


   # with open('image.png', 'wb') as file:
    #   file.write(image)

    #image=Image.open('image.png')
    image=numpy.array(image, dtype=numpy.uint8)
    #print (image)
    

    pixels=[list(i[:3]) for i in image[800]]

    for i, pixel in enumerate(pixels):
        r, b,g=[int(i) for i in pixel]
        #print (r, g, b)
        if(r+g+b==0):
            print("In if")
            device.shell("input tap "+str(i)+" 800")
            break
