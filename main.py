import random
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import sys
from terrainGen import terrainGen
import time

Text.default_resolution = pow(Text.size, 10)
app = Ursina()

WORLD_WIDTH = 50

def input(key):
    if key == "escape":
        sys.exit()

class Player():
    def __init__(self):
        self.controller = FirstPersonController(color=color.red, scale=0.8, position=(0, 0, 0), collider='sphere', gravity=True)
        self.controller.cursor = Entity(parent=camera.ui, model='quad', texture='Textures/crosshair.png', scale=0.03)
        self.block_pick = 1
        self.death_message = Text(parent=camera.ui, text='You Died', scale=20, origin=(0, -0.6),
                                  font="fonts/Minceraft_font.ttf", enabled=False)
        self.respawn_button = Button(parent=camera.ui, text='respawn',
                                    scale=(0.4, 0.1), origin=(0, 0), color=color.gray, on_click=self.respawn, enabled=False)
        self.respawn_button.text_entity.font = "fonts/Minceraft_font.ttf"
        self.respawn_button.text_entity.world_scale = 100
        self.death_sfx = "Sounds/Death.mp3"
        self.walking = Audio("Sounds/Walking.mp3", volume=5)
        
    def update(self):
        #print(self.death_message.resolution)
        if held_keys['1']: 
            self.block_pick = 1
        if held_keys['2']: 
            self.block_pick = 2
        if self.controller.y < -30:
            self.death()
        print(self.controller.y)
        '''
        if self.controller.speed > 5 or self.controller.speed < 5:
            Audio(self.walking_sfx, volume=5)
        print(self.controller.speed)
        '''
        
        if (held_keys["w"] or held_keys["a"] or held_keys["s"] or held_keys["d"]) and self.controller.grounded and not self.walking.playing:
            self.walking.play()
       
    def respawn(self):
        self.controller.enable()
        self.controller.position = Vec3(0, 0.5, 0)
        self.respawn_button.disable()
        self.death_message.disable()
    def death(self):
        if self.controller.enabled == True:
            Audio(self.death_sfx, volume=1)
            
            self.death_message.enable()
            self.respawn_button.enable()
            self.controller.disable()
player = Player()

player.controller.gravity = 0.8
camera.clip_plane_far = 20


    

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
terrain = terrainGen()

Sky()

terrain.genTerrain()
def update():
    terrain.update(player.controller.position)
    player.update()  
        

app.run()


