# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:24:11 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

a = 0
while True:
    mc.postToChat("這是第" + 
                  str(a) + "次")
    a = a+1
    time.sleep(1)