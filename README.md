# Map_Navigation
Dungeon map is defined in input file. Each line specifies room name and connections to other rooms:

a0 n:a3 
a1 e:a2 s:a3 
a2 s:a5 w:a1 
a3 n:a1 s:a0 w:a4 
a4 e:a3 s:b0 
a5 n:a2 e:a6 
a6 e:a7 s:a8 w:a5 
a7 s:a9 w:a6 
a8 n:a6 e:a9 s:b6 
a9 n:a7 w:a8 
b0 n:a4 w:b1 
b1 e:b0 s:b2 
b2 n:b1 e:b3
b3 e:b4 w:b2
b4 e:b5 w:b3
b5 e:b6 w:b4 
b6 n:a8 w:b5 

a0 to b6 are room names (they can be any 2-character names for simplicity)
n, s, e, w are doors leading to next rooms located north, south, east or west from current room.

Task:
Implement simple game framework that allows you to interactively navigate through the dungeon (room by room) by typing move direction (n, s, e or w).

implementation should display room name you are in, possible move directions and should react on your commands (by typing n, s, e or w)

######################################################
Simple output of minimum version:
######################################################
------------------------------
you are in room a0
possible moves: n
your choice:n
------------------------------
you are in room a3
possible moves: nsw
your choice:w
------------------------------
you are in room a4
possible moves: e
your choice:
