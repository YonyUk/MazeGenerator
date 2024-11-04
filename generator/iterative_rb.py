import numpy as np
from enum import Enum
import random

class IterativeRB:
    
    """
    rooms: -> tuple with the count of rooms in x-axis and y-axis
    """
    
    def __init__(self,rooms,start_room):
        
        if start_room[0] > rooms[0] - 1 or start_room[0] < 0 or start_room[1] > rooms[1] - 1 or start_room[1] < 0:
            raise Exception(f'{start_room} est fuera del rango')
        
        self._start_room = start_room
        self._rooms = rooms
        
        self._room = 2*start_room[0] + 1,2*start_room[1] + 1
        self._visiteds = []
        x,y = rooms
        self._map = np.ones((2*x + 1,2*y + 1)) * -1
        self._options = []
        
        for i in range(self._map.shape[0]):
            for j in range(self._map.shape[1]):
                if not (i % 2 == 0 or j % 2 == 0):
                    self._map[i,j] = 0
                    pass
                pass
            pass
        
        self._map[self._room[0],self._room[1]] = 1
        
        pass
    
    @property
    def map(self):
        return self._map
    
    def _in_range(self,room):
        return room[0] > -1 and room[0] < self._map.shape[0] and room[1] > -1 and room[1] < self._map.shape[1]
    
    def _get_neigborghs(self,room):
        neigborghs = []
        dirs = [-2,0,2]
        for dir_0 in dirs:
            for dir_1 in dirs:
                if dir_0 * dir_1 == 0 and not dir_0 == dir_1 and self._in_range((room[0] + dir_0,room[1] + dir_1)) and not self._map[room[0] + dir_0,room[1] + dir_1] == 1:
                    neigborghs.append((room[0] + dir_0,room[1] + dir_1))
                    pass
                pass
            pass
        return neigborghs
    
    def _destroy_wall_bettwen(self,room_1,room_2):
        left_right = room_1[0] - room_2[0]
        up_down = room_1[1] - room_2[1]
        self._map[room_1[0] - np.sign(left_right),room_1[1] - np.sign(up_down)] = 1
        pass
    
    def _select_border_pos(self):
        pos = ['up','down','left','right']
        while True:
            start = random.choice(pos)
            x,y = None,None
            if start == 'up':
                x,y = random.randint(0,self._map.shape[0]),0
                pass
            elif start == 'down':
                x,y = random.randint(0,self._map.shape[0]),self._map.shape[1] - 1
                pass
            elif start == 'left':
                x,y = 0,random.randint(0,self._map.shape[1])
                pass
            else:
                x,y = self._map.shape[1] - 1,random.randint(0,self._map.shape[1])
                pass
            dirs = [-1,0,1]
            for dir_0 in dirs:
                for dir_1 in dirs:
                    if dir_0 * dir_1 == 0 and not dir_0 == dir_1 and self._in_range((x + dir_0,y + dir_1)) and self._map[x + dir_0,y + dir_1] == 1:
                        return x,y
                    pass
                pass
            pass
        pass

    @property
    def next(self):
        options = self._get_neigborghs(self._room)
        if len(options) > 0:
            self._visiteds.append(self._room)
            new_room = random.choice(options)
            self._destroy_wall_bettwen(self._room,new_room)
            self._room = new_room
            self._map[self._room[0],self._room[1]] = 1
            return True
        elif len(self._visiteds) > 0:
            while len(self._visiteds) > 0:
                option = self._visiteds.pop()
                if len(self._get_neigborghs(option)) > 0:
                    self._room = option
                    return True
                pass
            pass
        s_x,s_y = self._select_border_pos()
        e_x,e_y = self._select_border_pos()
        self._map[s_x,s_y] = 1
        self._map[e_x,e_y] = 1
        return False
    
    pass

class IterativeRBv2(IterativeRB):
    
    def __init__(self,rooms,start_room):
        super().__init__(rooms,start_room)
        pass
    
    def _get_visited_neigborghs(self,room):
        neigborghs = []
        dirs = [-2,0,2]
        for dir_0 in dirs:
            for dir_1 in dirs:
                if dir_0 * dir_1 == 0 and not dir_0 == dir_1 and self._in_range((room[0] + dir_0,room[1] + dir_1)) and self._map[room[0] + dir_0,room[1] + dir_1] == 1:
                    neigborghs.append((room[0] + dir_0,room[1] + dir_1))
                    pass
                pass
            pass
        return neigborghs
    
    def _get_blocks_around(self,pos):
        x,y = pos
        blocks = []
        dirs = [-1,0,1]
        for dir_0 in dirs:
            for dir_1 in dirs:
                if dir_0 * dir_1 == 0 and not dir_0 == dir_1 and self._in_range((x + dir_0,y + dir_1)) and self._map[x + dir_0,y + dir_1] == -1:
                    blocks.append((x + dir_0,y + dir_1))
                    pass
                pass
            pass
        return blocks
    
    def _kill_loner_walls_around(self,pos):
        dirs = [-1,1]
        for dir_0 in dirs:
            for dir_1 in dirs:
                if self._in_range((pos[0] + dir_0,pos[1] + dir_1)) and self._map[pos[0] + dir_0,pos[1] + dir_1] == -1:
                    temp = self._get_blocks_around((pos[0] + dir_0,pos[1] + dir_1))
                    if len(temp) == 0:
                        self._map[pos[0] + dir_0,pos[1] + dir_1] = 1
                        pass
                    pass
                pass
            pass
        pass
    
    @property
    def next(self):
        options = self._get_neigborghs(self._room)
        if len(options) > 0:
            self._visiteds.append(self._room)
            new_room = random.choice(options)
            self._destroy_wall_bettwen(self._room,new_room)
            self._room = new_room
            self._map[self._room[0],self._room[1]] = 1
            return True
        elif len(self._visiteds) > 0:
            visited_options = self._get_visited_neigborghs(self._room)
            probability = (len(visited_options) - 1) / 4
            r_val = random.random()
            if r_val <= probability:
                new_room = random.choice(visited_options)
                self._destroy_wall_bettwen(self._room,new_room)
                self._kill_loner_walls_around(self._room)
                pass
            while len(self._visiteds) > 0:
                option = self._visiteds.pop()
                if len(self._get_neigborghs(option)) > 0:
                    self._room = option
                    return True
                pass
            pass
        s_x,s_y = self._select_border_pos()
        e_x,e_y = self._select_border_pos()
        self._map[s_x,s_y] = 1
        self._map[e_x,e_y] = 1
        return False
    
    pass