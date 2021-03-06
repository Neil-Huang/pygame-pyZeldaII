
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

class Rope:
    "Game object"
    def __init__(self, xx,yy,hh):
	self.x = xx
        self.y = yy 
        self.w = 16 
        self.h = hh
        
        self.image = pygame.image.load('./pics/rope-16x16.bmp').convert()
        self.image.set_colorkey((0,0,0)) 
        self.hitpoints = 999999
        
    def draw(self, screen, room):
	for i in range(self.y/self.w,self.y+self.h/self.w):
        	screen.blit(self.image,(self.x+room.relativex+self.w*2,i*self.w+room.relativey))
	    
	     
    def collidewithrope(self, room, player):
        ###print 'rope x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
        ###print ' %d %d' % (room.relativex,room.relativey)
	if (player.x-room.relativex > self.x and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y and
	player.y-room.relativey < self.y + self.h):
	    print "collision with Rope!"
	    return 1 
	else:
	    return 0
    
    def update(self,room,player):
	1
