
# Copyright (C) Johan Ceuppens 2010
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
from pygame.locals import *
from maproom import *
from maproomdungeon import *
from maproomdungeonnorthwall import *
from tilebox import *
from rope import *
#from snake1 import *
from rubysword import *
from digdogger import *
from ironknuckle import *
from deeler import *
from daira import *

class TileroomBase:
    "Room with a (big) map"
    def __init__(self,xx,yy,relx,rely):
	self.x = xx
	self.y = yy
	self.relativex = relx
	self.relativey = rely
	self.relativex = 0
	self.relativey = 0
	self.WIDTH = 0
	self.HEIGHT = 0
	self.TILEWIDTH = 16
	self.TILEHEIGHT = 16
	self.direction = "south"         
	self.tilelist =	[]
	self.gameobjects = [] ### NOTE leavs this empty
	self.tileroomgameobjects = []
	self.changeroomnumber = 0 
 
    def draw(self,screen,player):
	1
		
    def isroomdownexit(self):
	if self.relativex  < -500:
		return 1
	return 0

    def setxyfromdown(self):
        self.relativex = 0
	self.relativey = 0

    def exit(self, game):
	if self.isroomdownexit():
		self.setxyfromdown()
		return 2 
	return 0 
 
    def collidesword(self,player):
	return None

    def collideswordlow(self,player):
	return None

    def collideup(self,player):
	return None

    def collidewithropes(self,player):
	return None

    def collide(self,player):
	px = player.x % self.WIDTH
	py = player.y % self.HEIGHT
	px /= self.TILEWIDTH
	py /= self.TILEHEIGHT
	prelx = player.x - self.relativex
	prely = player.y - self.relativey
	prelxx = prelx % self.WIDTH
	prelyy = prely % self.HEIGHT
	prelxxx = prelxx / self.TILEWIDTH
	prelyyy = prelyy / self.TILEHEIGHT
	###tn = self.tilelist[py][px]	
	tn = self.tilelist[prelyyy][prelxxx]	
	###print ">>> %d >>> %d tn=%f" % (prelxxx,prelyyy,tn)	
	# FIX make function ?
	##if tn >= 2:
	##	return tn 
	#return 0	
	return tn 

    def undomove(self):
        if self.direction == "north":
            self.movedown()
            #self.movedown()
        elif self.direction == "south":
            self.moveup()
            #self.moveup()
        elif self.direction == "west":
            self.moveright()
            #self.moveright()
        elif self.direction == "east":
            self.moveleft()
            #self.moveleft()

    def fall(self,player):
	return 2 

    def moveleft(self):
	self.relativex -= 10
	self.direction = "west"
	if self.relativex <= - self.WIDTH + 640: ### NOTE 640 screenwidth
		self.relativex += 10 
		
    def moveright(self):
	self.relativex += 10
	self.direction = "east"
	if self.relativex >= 0:
		self.relativex -= 10 

    def moveup(self):
	self.direction = "north"
	self.relativey -= 10
	if self.relativey <= - self.HEIGHT + 480: ### NOTE 480 screenheight
		self.relativey += 10

    def movedown(self):
	self.direction = "south"
	self.relativey += 10
	if self.relativey >= 0:### NOTE 480 screenheight
		self.relativey -= 10

    def MOVEDOWN(self,room,player):
	##self.relativey += 10
	self.movedown()

    def MOVEUP(self,room,player):
##	self.relativey -= 10
	self.moveup()

    def changeroom(self, n):
	self.changeroomnumber = n


    def removeobject(self, o):
        for i in range(0,len(self.tileroomgameobjects)):
            if self.tileroomgameobjects[i] == o:
                self.tileroomgameobjects[i] = None
