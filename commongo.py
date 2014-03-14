
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
from gameobject import *
from stateimagelibrary import *
from random import *

class CommonGO(Gameobject):
    "Game object"
    def __init__(self, xx,yy):
	self.x = xx 
        self.y = yy
        self.direction = "south" 
	# default width and height 
        self.w = 80
        self.h = 80 
        self.SCREENH = 640 
        self.SCREENW = 480 
        ## dungeon statue as default picture
	self.stimlib = Stateimagelibrary()	
        self.hitpoints = 1000000000
        # NOTE : decrease 1 hitpoint with default sword
        self.hitf = self.hit1
       	self.changeroomnumber = 0
 
    def draw(self, screen, room):
	r = randint(0,100)
	if r == 0:
		self.direction = "west"
	if r == 25:
		self.direction = "east"
	if r == 50:
		self.direction = "north"
	if r == 75:
		self.direction = "south"

	if self.direction == "west":
		self.x -= 5
	elif self.direction == "east":
		self.x += 5
	elif self.direction == "north":
		self.y -= 5
	elif self.direction == "south":
		self.y -= 5
        self.stimlib.draw(screen, self.x+room.relativex,self.y+room.relativey)    
    def collidewithsword(self, room, player):
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x and#-self.w  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y and#-self.h and 
	player.y-room.relativey < self.y + self.h):
	    #print "collision with Game Object!"
	    return 1 
	else:
	    return 0

    def collidewithswordlow(self, room, player):
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x and#-self.w  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y and#-self.h and 
	player.y-room.relativey < self.y + self.h/2):
	    #print "collision with Game Object!"
	    return 1 
	else:
	    return 0

    def collideup(self, room, player):
	    return 0

    def collide(self, room, player):
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y and 
	player.y-room.relativey < self.y + self.h):
	    print "collision with CommonGO"
	    return 1 
	else:
	    return 0 ## for game self.talker

    def collidego(self, room, player):
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y and 
	player.y-room.relativey < self.y + self.h):
	    print "collision with CommonGO (collidego)"
	    room.changeroom(self.changeroomnumber)
	    return 1 
	else:
	    return 0 ## for game self.talker

    def fall(self, player):
	return 0 

    def fallcollide(self, room, player):
	return 0 ## for game self.talker


    def collidepickup(self, room, player):
        # FIX BUG
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y+self.h and 
	player.y-room.relativey < self.y+ self.h):
	    #print "pickup collision!"	
	    return 3 
	else:
	    return 0 
    
    def collideobjectX(self, room):
	for i in room.gameobjects:
	    if i != None:	
	        if (self.x > i.x  and 
		    self.x < i.x+i.w):
	            return 1 
	return 0

    def collideobjectY(self, room):
	for i in room.gameobjects:
	    if i != None:	
	        if (self.y > i.y  and 
		    self.y < i.y+i.h):
	            return 1 
	return 0
 
    def collideobjectXY(self, room):
	for i in room.gameobjects:
	    if i:		
	        if (self.x > i.x  and 
	 	    self.x < i.x+i.w and 
	            self.y > i.y and 
	            self.y < i.y+i.h):
	            return 1 
	return 0 
    
    def update(self,room,player):
	1

    def pickup(self, room):
        return 0

    def hit1(self):## NOTE decreases hitpoints
        self.hitpoints -= 1
        return self.hitpoints

    def hit2(self):## NOTE decreases hitpoints
        self.hitpoints -= 2
        return self.hitpoints

    def hitwithweapon(self,damage):
	if damage > 0:
            print 'enemy is hit!'
        self.hitpoints -= damage

    def fight(self,room,player,keydown):
	1
    
    def undomove(self):
	1
