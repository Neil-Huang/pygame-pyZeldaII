
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
from tree import *
from tree2 import *
from dungeonentrance1 import *
from tileroombase import *
from maproomdungeonnorthwall import *
from goblin1 import *
from goblin2 import *
from goblin3 import *
from tilebox import *
from tilemapbox import *
from rope import *
#from snake1 import *
from rubysword import *
from beholder import *
from beholderbat import *
from digdogger import *
from ironknuckle import *
from deeler import *
from daira import *
from koboldwizardgo import *
from ogrego import *
from ghostygo import *
from nerdwizardgo import *
from town1go import *

class Tileroom1(TileroomBase):
    "Room with a (big) map"
    def __init__(self,xx,yy,relx,rely):
        TileroomBase.__init__(self,xx,yy,relx,rely)
###        self.background = pygame.image.load('./pics/bg1-2400x600.bmp').convert()
        # left NOTE : boxes collide so put them after enemies !
        self.tileroomgameobjects.append(KoboldWizardGO(400,665))
        self.tileroomgameobjects.append(Town1GO(280,345))
        self.tileroomgameobjects.append(OgreGO(200,365))
        self.tileroomgameobjects.append(GhostyGO(100,345))
        self.tileroomgameobjects.append(NerdWizardGO(10,345))
        self.tileroomgameobjects.append(TilemapBox(0,0,2400,100))

	self.x = xx
	self.y = yy

	self.tile1 = pygame.image.load('./pics/tile-grass-1.bmp').convert()
	self.tile2 = pygame.image.load('./pics/tile-grass-2.bmp').convert()
	self.tileborder1 = pygame.image.load('./pics/tile-border-1-16x16.bmp').convert()
	self.tileborder2 = pygame.image.load('./pics/tile-border-2-16x16.bmp').convert()
	self.tileborder3 = pygame.image.load('./pics/tile-border-3-16x16.bmp').convert()
	self.tileborder4 = pygame.image.load('./pics/tile-border-4-16x16.bmp').convert()
	self.tileborder5 = pygame.image.load('./pics/tile-border-5-16x16.bmp').convert()
	self.tileborder6 = pygame.image.load('./pics/tile-border-6-16x16.bmp').convert()
	self.tileborder7 = pygame.image.load('./pics/tile-border-7-16x16.bmp').convert()
	self.tileborder8 = pygame.image.load('./pics/tile-border-8-16x16.bmp').convert()
	self.tileborder9 = pygame.image.load('./pics/tile-border-9-16x16.bmp').convert()
	self.tiletree1 = pygame.image.load('./pics/tile-tree-1-16x16.bmp').convert()
	self.tiletree2 = pygame.image.load('./pics/tile-tree-2-16x16.bmp').convert()
	self.tiletree3 = pygame.image.load('./pics/tile-tree-3-16x16.bmp').convert()
	self.tiletree4 = pygame.image.load('./pics/tile-tree-4-16x16.bmp').convert()
	self.WIDTH = 1024 
	self.HEIGHT = 1024 
	self.TILEWIDTH = 16
	self.TILEHEIGHT = 16
       	#### FIX match lengths of table elements 
	#### FIX do not use any number smaller than 2 as this is the gameover value 
	self.tilelist =	[
		[2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,
		2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,
		2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,
		2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,
		2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,
		3.2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,
		3.4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],



		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,3.3,3.4,3.3,3.4,3.3,3.4,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3.1,3.2,3.1,3.2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3.3,3.4,3.3,3.4,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3.1,3.2,3.1,3.2,
		2,2,2,2,2,2,3.1,3.2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3.3,3.4,3.3,3.4,
		2,2,2,2,2,2,3.3,3.4,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],


		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,3.1,3.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2.6,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,3.3,3.4,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],



		[2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
		2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],

		]

    def draw(self,screen,player):
	TileroomBase.draw(self,screen,player)
	for x in range(0, self.HEIGHT / self.TILEHEIGHT):
		for y in range(0, self.WIDTH / self.TILEWIDTH):
			if self.tilelist[y][x] == 1:	
				screen.blit(self.tile1, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 2:	
				screen.blit(self.tile2, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 2.1:	
				screen.blit(self.tileborder1, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 2.2:	
				screen.blit(self.tileborder2, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 2.3:	
				screen.blit(self.tileborder3, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 2.4:	
				screen.blit(self.tileborder4, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 2.5:	
				screen.blit(self.tileborder5, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 2.6:	
				screen.blit(self.tileborder6, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 2.7:	
				screen.blit(self.tileborder7, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 2.8:	
				screen.blit(self.tileborder8, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 2.9:	
				screen.blit(self.tileborder9, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 3.1:	
				screen.blit(self.tiletree1, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 3.2:	
				screen.blit(self.tiletree2, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 3.3:	
				screen.blit(self.tiletree3, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[y][x] == 3.4:	
				screen.blit(self.tiletree4, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))

	for go in self.tileroomgameobjects:
		go.draw(screen,self)

    def isroomdownexit(self):
	###if self.relativex  < -100:
	###	return 1 
	return 0

    def setxyfromdown(self):
        self.relativex = 0
	self.relativey = 0

    def exit(self, game):
	if self.isroomdownexit():
		self.setxyfromdown()
		return 4 
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
	for go in self.tileroomgameobjects:
		if go.collidego(self,player):
			self.undomove()
			return 2	

	r = TileroomBase.collide(self,player)
	# tile 1 
	if r == 2:
		1 #return 2 
	# tile 2 - do not block 
	if r == 2.1:
		1	
	if r == 3.1 or r == 3.2 or r == 3.3 or r == 3.4:
		self.undomove()
		return 2	
	return 0

    def fall(self,player):
	return 2 

    def moveup(self):
	self.direction = "north"
	self.relativey -= 10

    def moveleft(self):
	self.relativex -= 10
	self.direction = "west"
		
    def removeobject(self, o):
        for i in range(0,len(self.tileroomgameobjects)):
            if self.tileroomgameobjects[i] == o:
                self.tileroomgameobjects[i] = None
