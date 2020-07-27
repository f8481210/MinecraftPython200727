# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:27:40 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z = mc.player.getTilePos()

y = y + 100 
mc.player.setTilePos(x,y,z)
time.sleep(5)

y = y + 100  
mc.player.setTilePos(x,y,z)
time.sleep(5)

y = y + 100  
mc.player.setTilePos(x,y,z)
