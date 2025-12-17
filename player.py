from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Player():
    def __init__(self):
        self.controller = FirstPersonController(color=color.red, model="cube", scale=0.8, position=(0, 0, 0), collider='sphere', gravity=True)
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
        self.respawn_pos = (0, 0.5, 0)
        self.dead = False
        self.third_person = False
    def update(self):
        #hit_info = raycast((0,5,0), camera.rotation_directions, ignore=(self.controller,), distance=9, debug=True, color=color.black)
        '''
        if hit_info.hit:
            print(hit_info.entity)
        '''
        if held_keys['1']: 
            self.block_pick = 1
        if held_keys['2']: 
            self.block_pick = 2
        if self.controller.y < -30:
            self.death()

        
        if mouse.collision != None and not self.dead:
            #print(mouse.collision)
            print(mouse.collision.entity.position)
            
            if mouse.left and not self.dead and mouse.hovered_entity != self.controller:
                mouse.hovered_entity.disable()
            

        '''
        if self.controller.speed > 5 or self.controller.speed < 5:
            Audio(self.walking_sfx, volume=5)
        print(self.controller.speed)
        '''
        
        if (held_keys["w"] or held_keys["a"] or held_keys["s"] or held_keys["d"]) and self.controller.grounded and not self.walking.playing:
            self.walking.play()


    def input(self, key):
        if key == "p" and self.controller.grounded:
            self.respawn_pos = self.controller.position
        if key == "f" and not self.dead:
            if self.third_person:
                print("first person")
                camera.parent = self.controller.camera_pivot
                self.third_person = False
            else:
                print("third person")
                camera.parent = self.controller
                self.third_person = True

    def respawn(self):
        self.controller.enable()
        self.dead = False
        self.controller.position = self.respawn_pos
        self.respawn_button.disable()
        self.death_message.disable()
        self.controller.land()

    def death(self):
        if self.controller.enabled == True:
            Audio(self.death_sfx, volume=1)
            self.dead = True
            self.death_message.enable()
            self.respawn_button.enable()
            self.controller.disable()
            

    
