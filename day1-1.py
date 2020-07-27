# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:54:37 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

print(mc.player.getTilePos())