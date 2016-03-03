#! /usr/bin/python
import mcpi.minecraft as minecraft
import server

""" hello world test app

    @author: goldfish"""

mc = minecraft.Minecraft.create( server.address )
mc.postToChat("Hello, Minecraft!")
