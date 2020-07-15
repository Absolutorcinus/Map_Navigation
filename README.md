# Map_Navigation
Dungeon map is defined in input file. Each line specifies room name and connections to other rooms:

<p>a0 n:a3 <br>
a1 e:a2 s:a3 <br>
a2 s:a5 w:a1 </p>
<p>a3 n:a1 s:a0 w:a4 </p>
<p>a4 e:a3 s:b0 </p>
<p>a5 n:a2 e:a6 </p>
<p>a6 e:a7 s:a8 w:a5 </p>
<p>a7 s:a9 w:a6 </p>
<p>a8 n:a6 e:a9 s:b6 </p>
<p>a9 n:a7 w:a8 </p>
<p>b0 n:a4 w:b1 </p>
<p>b1 e:b0 s:b2 </p>
<p>b2 n:b1 e:b3</p>
<p>b3 e:b4 w:b2</p>
<p>b4 e:b5 w:b3</p>
<p>b5 e:b6 w:b4 </p>
<p>b6 n:a8 w:b5 </p>

<p>a0 to b6 are room names (they can be any 2-character names for simplicity)
n, s, e, w are doors leading to next rooms located north, south, east or west from current room.</p>

<h>Task:</h>
<p>Implement simple game framework that allows you to interactively navigate through the dungeon (room by room) by typing move direction (n, s, e or w).</p>

<p>implementation should display room name you are in, possible move directions and should react on your commands (by typing n, s, e or w)</p>


<h>*****Example of the output version:*****</h>

<p>you are in room a0</p>
<p>possible moves: n</p>
<p>your choice:n</p>
<p>------------------------------</p>
<p>you are in room a3</p>
<p>possible moves: nsw</p>
<p>your choice:w</p>
<p>------------------------------</p>
<p>you are in room a4</p>
<p>possible moves: e</p>
<p>your choice:</p>
