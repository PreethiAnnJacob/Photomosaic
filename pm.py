from skimage.io import * #read and write images in various formats
import sys # for runtime environment
import photomosaic as pm
from skimage import data #standard test images (image processing)

image = data.chelsea()# get chelsea.png #change the img as needed
imsave('image.png',image)
mosaicSize=(int (sys.argv[1]),int(sys.argv[2]))
pm.rainbow_of_squares('square/') #Generate 5832 small solid-color tiles for experimentation and testing into folder 'square/'
squarePool=pm.make_pool('square/*.png')
mosaic=pm.basic_mosaic(image,squarePool,mosaicSize)
outputFile=  sys.argv[3] if len(sys.argv)==4 else 'mosaic.png'	
imsave(outputFile,mosaic)
