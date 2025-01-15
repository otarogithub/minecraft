from ursina import *
from perlin_noise import PerlinNoise

player_pos = None

class block:
    block = load_model('cube.obj')
    texture = 'Textures/images.png'
    entity = None
    
    def __init__(self):
        self.entity = Entity(model='cube', texture=self.texture)
    
    def genBlock(self, x, y, z):
        self.entity.position = (x, -30, z)
        
    def colliderController(self):
        self.entity._collider = None

#---------------------------------------------------------------------------------------------------------------------------

class chunk:
    chunk_length = 16
    
    def __init__(self, x, z) -> None:
        self.x = x
        self.z = z
        
        self.blockList = []

    def genTerrain(self):
        a = int(self.chunk_length/2)
        
        i = 0
        
        for x in range(-a, a):
            for z in range(-a, a):
                #print(i)
                self.blockList.append(block())
                self.blockList[i].genBlock(x + (self.x * 16), -i, z + (self.z * 16))
                i += 1
        #self.disableChunk()
    
    def disableChunk(self):
        for block in self.blockList:
            block.entity.disable()
    
    def enableChunk(self):
        for block in self.blockList:
            block.entity.enable()
            

    
#---------------------------------------------------------------------------------------------------------------------------

class terrainGen:
    world_length = 32
    
    def __init__(self):
        self.chunkList = []
        
    def genTerrain(self):
        a = int(self.world_length/16)
        
        i = 0
        for x in range(-a, a):
            temp = []
            for z in range(-a, a):
                #print(i)
                temp.append(chunk(x, z))
                temp[z+a].genTerrain()
                i += 1
            self.chunkList.append(temp)
    
    def update(self, p):
        print(p)
        '''for chunk in self.chunkList:
            if (chunk.x - (p.x/16) > 0.5) or (chunk.z - (p.z/16) > 0.5):
                chunk.disableChunk()
            else:
                chunk.enableChunk()
            #loads strips of chunks when moving back and forth??? kinda dumb tbh'''
            
        for x in range(0, len(self.chunkList)):
            for z in range(0, len(self.chunkList[x])):
                if (((x - p.x)/(z - p.z)) > 3 ):
                    self.chunkList[x][z].disableChunk()
                else:
                    self.chunkList[x][z].enableChunk()
                #print("um um um")
            
            
                    

'''
class terrainGen:
    def __init__(self):
        #self.block = load_model('cube.obj')
        self.texture = 'Textures/images.png'
        
        self.blockList = []
        self.worldLength = 64
        for i in range(0, pow(self.worldLength, 2)):
            e = Entity(model='cube',
                       texture=self.texture)
            self.blockList.append(e)
            
    
    
    def genBlock(self, x, y, z, i):
        model = self.blockList[i]
        model.position = (x, 0, z)
        
        #model.vertices.extend([Vec3(x,y,z) + v for v in self.block.vertices])

            
    def genTerrain(self):
        a = int(self.worldLength/2)
        
        i = 0
        for x in range(-a, a):
            for z in range(-a, a):
                print(i)
                self.genBlock(x, -i, z, i)
                if i < pow(self.worldLength, 2):
                    i += 1
                    
        #self.blockList[0].model.generate()
        '''