# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:04:46 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10.5 
y = 10.5 
z = 10.5 
mc.player.setPos(x,y,z)