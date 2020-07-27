# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:15:19 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 100
y = 100
z = 100
mc.player.setTilePos(x,y,z)