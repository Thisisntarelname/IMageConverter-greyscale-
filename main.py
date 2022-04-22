import PIL
from PIL import Image
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
from IPython.display import display
import numpy as np

photo = open('OHSMapUp.png', 'rb')  
img = Image.open(BytesIO(photo.read()))
   
print (img.mode)

grayimg = img.convert('L')
grayimg.mode


# image should be 5100 × 3300
# https://predictivehacks.com/iterate-over-image-pixels/

a = img.getpixel((0,0))
print(a)

grayimg.getpixel((0,0))

def binarize(image_to_transform, threshold):

    output_image=image_to_transform.convert("L")

    for x in range(output_image.width):
        for y in range(output_image.height):
          print(output_image.getpixel((x,y)))

          if output_image.getpixel((x,y))< threshold: 
              output_image.putpixel( (x,y), 0 )
          else:
              output_image.putpixel( (x,y), 255 )
    output_image.save("newimage.png")    

    #Next steps: Fiddle with the threshhold to make hallways, rooms, and walls different colors, and have it determine paths through the school, and create nodes in the graph with networkx
 
binarize(img, 100)