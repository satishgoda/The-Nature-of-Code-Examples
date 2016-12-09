"""
Vectors, You Complete Me
"""

import bpy


def pre_frame_change(scene):
    width, height = scene['width'], scene['height']
    xspeed, zspeed = scene['xspeed'], scene['zspeed']

    actor = scene.objects['Actor']
    
    if scene.frame_current == 0:
        actor.location = (0, 0, 0)
        return

    x, y, z = actor.location

    x += xspeed
    z += zspeed

    if (x > width) or (x < 0):
        scene['xspeed'] *= -1
    
        if x > width:
            x = width
        if x < 0:
            x = 0

    if (-z  > height) or (z > 0):
        scene['zspeed'] *= -1

        if -z > height:
            z = -height
        if z > 0:
            z = 0

    actor.location = (x, y, z)

def add_handler():
    """
    import Chapter1
    Chapter1.add_handler()
    """
    print("Adding handler : {0}".format(pre_frame_change))
    bpy.app.handlers.frame_change_pre.append(pre_frame_change)

def remove_handler():
    """
    import Chapter1
    Chapter1.remove_handler()
    """
    print("Removing handler : {0}".format(bpy.app.handlers.frame_change_pre[0]))
    bpy.app.handlers.frame_change_pre.remove(pre_frame_change)

scene = bpy.context.scene

scene['xspeed'] = 15.3
scene['zspeed'] = -30.3
scene['width'] = 640
scene['height'] = 360


add_handler()
bpy.ops.screen.animation_play()
