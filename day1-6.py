# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:45:32 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("你的位置 - X:" + str(x) +
                  " Y:" + str(y) +
                  " Z:" + str(z))
    time.sleep(0.5)