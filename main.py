import random
from ursina import *
import sys
import player
from terrainGen import terrainGen
import time

app = Ursina()

scene.fog_density = .01
scene.fog_density = (1, 100)
scene.fog_color = color.white

Sky()
WORLD_WIDTH = 50
terrain = terrainGen()


player = player.Player()
player.controller.gravity = 0.8
player.controller.speed = 5
app.entity_counter = True
camera.clip_plane_far = 110



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
        
y
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



terrain.genTerrain()

def update():
    print(camera.parent)
    terrain.update(player.controller.position)
    player.update()  

def input(key):
    if key == "escape":
        sys.exit()
    player.input(key)

app.run()