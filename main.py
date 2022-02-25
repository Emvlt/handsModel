import bpy 
import random
seed_value = 123456

BONES = bpy.data.objects["Armature"].pose.bones
HAND = bpy.data.objects["Hand Ok"]

## Move Armature 
def armatureMovement(key = 'forearm.L.003'):    
    s = random.randint(95,105)/100
    print(s)
    BONES[key].scale = [s,s,s]

particleDict = {
                'count':20000,
                'emit_from':'VOLUME',
                'distribution':'GRID',
                'frame_start':0,
                'frame_end':0,
                'hexagonal_grid':True,
                'grid_resolution':250
                }
                
## Add Particle_System
def addParticleSytem(particleDict:dict):
    bpy.ops.object.particle_system_remove()
    bpy.ops.object.particle_system_add()
    bpy.context.object.particle_systems.active.seed = seed_value
    bpy.data.particles["ParticleSettings"].frame_start = particleDict['frame_start']
    bpy.data.particles["ParticleSettings"].frame_end = particleDict['frame_end']
    bpy.data.particles["ParticleSettings"].emit_from = particleDict['emit_from']
    bpy.data.particles["ParticleSettings"].distribution = particleDict['distribution']
    bpy.data.particles["ParticleSettings"].hexagonal_grid = particleDict['hexagonal_grid']
    bpy.data.particles["ParticleSettings"].count = particleDict['count']
    bpy.data.particles["ParticleSettings"].grid_resolution = particleDict['grid_resolution']
    bpy.data.particles["ParticleSettings"].display_size = 0.001
    bpy.data.particles["ParticleSettings"].display_size = 0.001
    
armatureMovement()
addParticleSytem(particleDict)
