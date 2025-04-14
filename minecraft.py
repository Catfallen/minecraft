from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random 
from utils import mapTree
invetory = {
  "1":"./blocks/grass.png",
  "2":"./blocks/bedrock.png",
  "3":'./blocks/wood1.jpg',
  '4':'./blocks/leaf.png'
}

blocks = {
  "1":"./blocks/grass.png",
  "2":"./blocks/bedrock.png",
  "3":'./blocks/wood1.jpg',
  '4':'./blocks/leaf.png',
  '5':'./blocks/dirt1.jpg'
}




texture = blocks['1']
app = Ursina()
player = FirstPersonController()
Sky()
minx = 0
minz = 0
maxx = 25
maxz = 25


mapteste = mapTree(minx,minz,maxx,maxz)


boxes = []
def ilha():
  global texture
  for y in range(0,-1,-1):
    for x in range(maxx+1):
      for z in range(maxz+1):
        box = Button(color=color.white, model='cube', position=(x,y,z),
          texture=texture, parent=scene, origin_y=0.5)
        boxes.append(box)
        texture = blocks['1']

def tree():
  #Column
  for tronco in mapteste:
    texture = blocks['3']
    x = tronco[0]
    z = tronco[1]
    for y in range(tronco[2],tronco[3]+1):
      box = Button(color=color.white, model='cube', position=(x,y,z),
          texture=texture, parent=scene, origin_y=0.5)
      boxes.append(box)

ilha()
tree()



transparent = ['leaf.png']


def input(key):
  global texture
  if key in '123456789': #Se a key for um numero do inventario
    if key in invetory.keys():
      texture = invetory[key]
    print(key,texture)
  
  
  for box in boxes:
    if box.hovered:
      if key == 'right mouse down' and texture != "":
        new = Button(color=color.rgba(255,255,255,100), model='cube', position=box.position + mouse.normal,
                    texture=texture, parent=scene, origin_y=0.5)
        
        #Transparência
        if texture in transparent:
          new.set_shader_input("alpha_cutoff",0.05)
        boxes.append(new)
      if key == 'left mouse down':
        boxes.remove(box)
        destroy(box)
  if key == "escape hold":
    quit()
    #exit()
    
app.run()