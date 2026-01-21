from ursina import *
from random import randrange
from perlin_noise import PerlinNoise

player_pos = None

noise = PerlinNoise(octaves=6, seed=randrange(-1000000, 1000000))

class block:
    block = 'Models/cube.obj'
    texture = 'Textures/block_atlas.png'
    entity = None
    
    def __init__(self):
        self.entity = Entity(model=self.block, collider = 'box', texture=self.texture)
        
    
    def genBlock(self, x, y, z):
        self.entity.position = (x, y, z)
        
    def colliderController(self):
        self.entity._collider = None
        
    

#---------------------------------------------------------------------------------------------------------------------------
class structure:
    def __init__(self):
        self.structure = Entity(model = None, collider = None)
        self.blockList = []
        self.texture = 'Textures/block_atlas.png'
        self.isEnabled = False
    def genBlocks(self, x, y, z):
        structurePos = [x, y, z]
        newY = y
        for i in range(randrange(4, 8)):
            self.blockList.append(block())
            #self.blockList[i].genBlock(x + (self.x * 16), -y, z + (self.z * 16))
            self.blockList[i].entity.parent = self.structure
            self.blockList[i].genBlock(structurePos[0], -(structurePos[1] - i), structurePos[2])
            newY = -(structurePos[1] - i)
        structurePos[1] = newY
        
        randLength = randrange(2, 4)
        for i in range(randrange(3, 6)):
            for j in range(randLength):
                for k in range(randLength):
                    self.blockList.append(block())
                    self.blockList[i].entity.parent = self.structure
                    self.blockList[i].genBlock(structurePos[0] + j, -(structurePos[1] - i), structurePos[2] + k)
        
        
        self.structure.combine()
        self.structure.collider = 'mesh'
        self.structure.texture = self.texture

class chunk:
    chunk_length = 16
    
    def __init__(self, x, z) -> None:
        self.chunk = Entity(model = None, collider = None, position = (x*16, 0, z*16))
        self.chunk.wireframe = False
        self.texture = 'Textures/block_atlas.png'
        self.x = x
        self.z = z
        
        self.blockList = []
        self.isEnabled = False

    def genTerrain(self):
        a = int(self.chunk_length/2)
        
        i = 0
        
        for x in range(-a, a):
            for z in range(-a, a):
                #print(i)
                y = noise([(x + (self.x * 16)) * .02,(z + (self.z * 16)) * .02])
                y = math.floor(y * 7.5)
                '''
                if randrange(0, 100) < 2:
                    structure().genBlocks(x + (self.x * 16), y-1, z + (self.z * 16))
                '''

                while (y < 8):
                    self.blockList.append(block())
                    self.blockList[i].genBlock(x + (self.x * 16), -y, z + (self.z * 16))
                    self.blockList[i].entity.parent = self.chunk
                    self.blockList[i].genBlock(x, -y, z)
         
                    #self.chunk.model.vertices.extend(self.blockList[i].entity.combine().vertices)
                    #self.chunk.model.uvs.extend(self.blockList[i].entity.combine().uvs)
                    #destroy(self.blockList[i].entity)
                    y+=1
                    i += 1
                    
                
        
        self.chunk.combine(auto_destroy=True)
        
        self.chunk.collider = 'mesh'
        self.chunk.texture = self.texture
        #self.chunk.model.generate_normals()
        #self.disableChunk()
    
    
    def disableChunk(self):
        self.isEnabled = False
        self.chunk.disable()
        #for block in self.blockList:
            #block.entity.collision = False
            #block.entity.disable()
    
    def enableChunk(self):
        self.isEnabled = True
        self.chunk.enable()
        #for block in self.blockList:
            #block.entity.collision = True
            #block.entity.enable()
    
    #def updateChunk(self, playercast):



    
#---------------------------------------------------------------------------------------------------------------------------

class terrainGen:
    world_length = 16
    
    def __init__(self):
        self.chunkList = []
        
    def genTerrain(self):
        
        
        a = int(self.world_length/16)
        
        i = 0
        for x in range(-a, a):
            temp = []
            for z in range(-a, a):
                temp.append(chunk(x, z))
                temp[z+a].genTerrain()

                i += 1
            self.chunkList.append(temp)

        
    
    def update(self, p):


        #self.genTerrain(p)
        
        '''for chunk in self.chunkList:
            if (chunk.x - (p.x/16) > 0.5) or (chunk.z - (p.z/16) > 0.5):
                chunk.disableChunk()
            else:
                chunk.enableChunk()
            #loads strips of chunks when moving back and forth??? kinda dumb tbh'''
        '''
        for x in range(0, len(self.chunkList)):
            for z in range(0, len(self.chunkList[x])):
                distX = (x - (p.x / 16)) - (self.world_length/16)
                distZ = (z - (p.z/ 16)) - (self.world_length/16)
                #print(str(distX) + " " + str(distZ))
                
                if (distX > 5 or distX < -5) or (distZ > 5 or distZ < -5):
                    self.chunkList[x][z].disableChunk()
                else:
                    self.chunkList[x][z].enableChunk()
                
                #print("um um um")'''
        
    