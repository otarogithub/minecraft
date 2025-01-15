import random
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import sys
from terrainGen import terrainGen


app = Ursina()

WORLD_WIDTH = 50

def input(key):
    if key == "escape":
        sys.exit()

class Player():
    def __init__(self):
        self.controller = FirstPersonController(color=color.red, scale=0.8, position=(0, 0, 0), collider='sphere', gravity=False)
        self.controller.cursor = Entity(parent=camera.ui, model='quad', texture='Textures/crosshair.png', scale=0.03)
        self.block_pick = 1
        
    
        


    def update(self):
        print(self.controller.position)
        if held_keys['1']: 
            self.block_pick = 1
        if held_keys['2']: 
            self.block_pick = 2


player = Player()

#
# 
camera.clip_plane_far = 200

#print(camera.clip_plane_far)

'''
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='Textures/images.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0,
            texture=texture,
            color=color.hsv(0, 0, random.uniform(.5, 1.0)),
        )
        #self.visible = False

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)
            if key == 'right mouse down':
                if player.block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal, texture='Textures/images.png')
                if player.block_pick == 2:
                    voxel = Voxel(position=self.position + mouse.normal, texture='Textures/bedrock.png')
                
    def update(self):
        #hit_info = raycast(self.position, Vec3(0, 1, 0), distance=9, debug=False, color=color.black)
        
        if distance(self, player) > 5:
            self.visible = False
            self.collider = None
        else:
            self.visible = True
            self.collider = 'box'
        

noise = PerlinNoise(octaves=5, seed=random.randrange(-1000000, 1000000))
cube_list = []
for x in range(round(-WORLD_WIDTH/2), round(WORLD_WIDTH/2)):
    for z in range(round(-WORLD_WIDTH/2), round(WORLD_WIDTH/2)):
        y = noise([x * .02,z * .02])
        y = math.floor(y * 7.5)
        while (y > -1):
            voxel = Voxel(position=(x, y, z))
            y -= 1
'''            
terrain = terrainGen()



terrain.genTerrain()
def update():
    terrain.update(player.controller.position)

app.run()


