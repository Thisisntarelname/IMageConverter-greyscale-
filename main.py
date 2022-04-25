import PIL
from PIL import Image
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
from IPython.display import display
import numpy as np

import networkx as nx
G = nx.Graph()
xnodes = [] #A list of all x nodes
ynodes = []

photo = open('OHSMapUpNoNames.png', 'rb')  
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
          previous = str(x)+str(y-1)
          #print(output_image.getpixel((x,y)))
          name = str(x)+", "+str(y)
          

          if output_image.getpixel((x,y))== 213: 
              
              output_image.putpixel( (x,y), 0 )
              #G.add_edge(name, previous, weight=1)
              G.add_node(name)
              xnodes.append(x)
              ynodes.append(y)

              print(name)

          else:
              output_image.putpixel( (x,y), 255 )
            
    output_image.save("newimage.png")    
    print("Finished!")

    #Next steps: Fiddle with the threshhold to make hallways, rooms, and walls different colors, and have it determine paths through the school, and create nodes in the graph with networkx
 
binarize(img, 100)

print(G)


#Now we loop through nodes and connect them to each other
i = 0
topleft = []
while i <len(xnodes):
  target = str(xnodes[i])+", "+str(ynodes[i])
  xtest = (xnodes[i])
  ytest = (ynodes[i])
  topleft.append(xtest)
  topleft.append(ytest)
  if xnodes[i-1] and ynodes[i-1]:#top left
    G.add_edge(target, (str(xtest-1)+", "+(str(ytest-1))), weight=1)
  if ynodes[i-1]:#top
    G.add_edge(target, (str(xtest)+", "+(str(ytest-1))), weight=1)
  if xnodes[i+1] and ynodes[i-1]:#top right
    G.add_edge(target, (str(xtest+1)+", "+(str(ytest-1))), weight=1)
  if xnodes[i-1]:#left
    G.add_edge(target, (str(xtest-1)+", "+(str(ytest))), weight=1)
  if xnodes[i+1]:#right
    G.add_edge(target, (str(xtest+1)+", "+(str(ytest))), weight=1)
  if xnodes[i-1] and ynodes[i+1]:#botton left
    G.add_edge(target, (str(xtest-1)+", "+(str(ytest+1))), weight=1)
  if ynodes[i+1]:#bottom
    G.add_edge(target, (str(xtest)+", "+(str(ytest+1))), weight=1)
  if xnodes[i+1] and ynodes[i+1]:#bottom right
    G.add_edge(target, (str(xtest+1)+", "+(str(ytest+1))), weight=1)
  i+=1
print(G)

path = nx.shortest_path(G, "778, 551", "778, 552", weight="weight")
print (path)

#here go through path and highlight it in newimage