INCLUDE Irvine32.inc
main	EQU start@0
MazeWidth =21
MazeHeight =21
MazeWidth2=41
MazeHeight2 =41
MazeWidth3=61
MazeHeight3 =61
.data

consoleHandle    DWORD ?
xyPos COORD <0,19> ; 

outputHandle DWORD 0
bytesWritten DWORD 0
count DWORD 0
mapPosition COORD <0,0>
cellsWritten DWORD ?
color word 61 dup(0eh)
color2 word 61 dup(0Ah)
color3 word 61 dup(0bh)

MazeBlank  BYTE MazeWidth*MazeHeight DUP(210)
MazeBlank2  BYTE MazeWidth2*MazeHeight2 DUP(210)
MazeBlank3  BYTE MazeWidth3*MazeHeight3 DUP(210)
MazeClear  BYTE (210)

Maze	BYTE 21 DUP(219)
      	BYTE 219,3 DUP(0),219,5 DUP(0),219,0,219,7 DUP(0),177
		BYTE 3 DUP(219),0,5 DUP(219),0,219,0,3 DUP(219),0,5 DUP(219)
      	BYTE 219,0,219,3 DUP(0),219,0,219,7 DUP(0),219,3 DUP(0),219
		BYTE 219,0,219,0,3 DUP(219),0,7 DUP(219),0,219,0,219,0,219
      	BYTE 219,0,219,9 DUP(0),219,3 DUP(0),219,0,219,0,219
      	BYTE 219,0,9 DUP(219),0,219,0,219,0,219,0,219,0,219
		BYTE 219,11 DUP(0),219,0,219,3 DUP(0),219,0,219
		BYTE 7 DUP(219),0,219,0,3 DUP(219),0,219,0,5 DUP(219)
		BYTE 219,0,219,0,219,0,219,0,219,3 DUP(0),219,0,219,0,219,0,219,0,219
      	BYTE 219,0,219,0,219,0,219,0,3 DUP(219),0,3 DUP(219),0,219,0,219,0,219
		BYTE 219,0,219,7 DUP(0),219,0,219,7 DUP(0),219
		BYTE 219,0,7 DUP(219),0,3 DUP(219),0,3 DUP(219),0,3 DUP(219)
		BYTE 219,7 DUP(0),219,3 DUP(0),219,0,219,0,219,0,219,0,219
		BYTE 219,0,9 DUP(219),0,219,0,219,0,3 DUP(219),0,219
		BYTE 219,19 DUP(0),219
		BYTE 219,0,219,0,219,0,3 DUP(219),0,3 DUP(219),0,5 DUP(219),0,219
		BYTE 219,0,219,0,219,0,219,0,219,3 DUP(0),219,0,219,3 DUP(0),219,0,219
		BYTE 5 DUP(219),0,219,0,5 DUP(219),0,3 DUP(219),0,219,0,219
		BYTE 177,5 DUP(0),219,9 DUP(0),219,3 DUP(0),219
      	BYTE 21 DUP(219)

Maze2	BYTE 3 DUP(219),177,37 DUP(219)
		BYTE 219,0,219,19 DUP(0),219,7 DUP(0),219,3 DUP(0),219,5 DUP(0),219
		BYTE 219,0,7 DUP(219),0,3 DUP(219),0,5 DUP(219),0,7 DUP(219),0,219,0,219,0,219,0,219,0,5 DUP(219)
		BYTE 219,11 DUP(0),219,0,219,5 DUP(0),219,5 DUP(0),219,0,219,3 DUP(0),219,5 DUP(0),219,0,219
		BYTE 9 DUP(219),0,7 DUP(219),0,5 DUP(219),0,219,0,3 DUP(219),0,7 DUP(219),0,219,0,219
		BYTE 219,7 DUP(0),219,0,219,3 DUP(0),219,0,219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219,0,219,5 DUP(0),219
		BYTE 5 DUP(219),0,219,0,219,0,219,0,219,0,219,0,5 DUP(219),0,5 DUP(219),0,3 DUP(219),0,219,0,219,0,3 DUP(219),0,219
		BYTE 219,5 DUP(0),219,0,219,0,219,0,219,0,219,0,219,7 DUP(0),219,5 DUP(0),219,0,219,3 DUP(0),219,0,219,0,219
		BYTE 219,0,7 DUP(219),0,219,0,219,0,219,0,219,0,3 DUP(219),0,7 DUP(219),0,219,0,219,0,3 DUP(219),0,3 DUP(219)
		BYTE 219,9 DUP(0),219,0,219,7 DUP(0),219,5 DUP(0),219,0,219,3 DUP(0),219,3 DUP(0),219,0,3 DUP(219)
		BYTE 219,0,5 DUP(219),0,13 DUP(219),0,3 DUP(219),0,219,0,3 DUP(219),0,3 DUP(219),0,219,0,219,0,219
		BYTE 219,5 DUP(0),219,0,219,3 DUP(0),219,5 DUP(0),219,0,219,3 DUP(0),219,0,219,3 DUP(0),219,0,219,5 DUP(0),219,0,219
		BYTE 219,0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219,0,5 DUP(219),0,219,0,219,0,7 DUP(219),0,219,0,219
		BYTE 219,0,219,3 DUP(0),219,7 DUP(0),219,0,219,9 DUP(0),219,0,219,3 DUP(0),219,0,219,5 DUP(0),219
		BYTE 3 DUP(219),0,7 DUP(219),0,3 DUP(219),0,11 DUP(219),0,5 DUP(219),0,3 DUP(219),0,219,0,219
		BYTE 219,11 DUP(0),219,11 DUP(0),219,7 DUP(0),219,5 DUP(0),219,0,219
		BYTE 219,0,11 DUP(219),0,9 DUP(219),0,5 DUP(219),0,3 DUP(219),0,7 DUP(219)
		BYTE 219,0,219,13 DUP(0),219,5 DUP(0),219,0,219,3 DUP(0),219,0,219,0,219,0,219,5 DUP(0),219
		BYTE 5 DUP(219),0,3 DUP(219),0,11 DUP(219),0,219,0,219,0,219,0,219,0,219,0,219,0,5 DUP(219),0,219
		BYTE 219,0,219,5 DUP(0),219,0,219,5 DUP(0),219,3 DUP(0),219,5 DUP(0),219,5 DUP(0),219,0,219,5 DUP(0),219
		BYTE 219,0,5 DUP(219),0,5 DUP(219),0,5 DUP(219),0,219,0,219,0,3 DUP(219),0,219,0,219,0,219,0,219,0,219,0,3 DUP(219)
		BYTE 219,5 DUP(0),219,3 DUP(0),219,5 DUP(0),219,5 DUP(0),219,3 DUP(0),219,0,219,0,219,0,219,3 DUP(0),219,3 DUP(0),219
		BYTE 219,0,3 DUP(219),0,3 DUP(219),0,219,0,15 DUP(219),0,5 DUP(219),0,5 DUP(219),0,219
		BYTE 219,3 DUP(0),219,5 DUP(0),219,3 DUP(0),219,9 DUP(0),219,5 DUP(0),219,5 DUP(0),219,3 DUP(0),219
		BYTE 219,0,219,0,3 DUP(219),0,5 DUP(219),0,219,0,7 DUP(219),0,219,0,3 DUP(219),0,5 DUP(219),0,219,0,3 DUP(219)
		BYTE 219,0,219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219,0,219,5 DUP(0),219,0,219,3 DUP(0),219,0,219,3 DUP(0),219,0,219,3 DUP(0),219
		BYTE 219,0,3 DUP(219),0,219,0,3 DUP(219),0,219,0,219,0,5 DUP(219),0,219,0,7 DUP(219),0,219,0,3 DUP(219),0,3 DUP(219)
		BYTE 219,0,219,3 DUP(0),219,3 DUP(0),219,0,219,0,219,0,219,0,219,3 DUP(0),219,5 DUP(0),219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219
		BYTE 3 DUP(219),0,7 DUP(219),0,219,0,219,0,219,0,219,0,219,0,219,0,9 DUP(219),0,5 DUP(219),0,219
		BYTE 219,11 DUP(0),219,0,219,5 DUP(0),219,0,219,5 DUP(0),219,7 DUP(0),219,0,219,0,219
		BYTE 3 DUP(219),0,219,0,3 DUP(219),0,7 DUP(219),0,7 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219,0,219,0,219,0,219
		BYTE 219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219,0,219,0,219,0,219,3 DUP(0),219,0,219,3 DUP(0),219,3 DUP(0),219,0,219,0,219,0,219,0,219
		BYTE 3 DUP(219),0,5 DUP(219),0,3 DUP(219),0,219,0,219,0,219,0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219,0,219,0,219,0,219,0,219
		BYTE 219,7 DUP(0),219,3 DUP(0),219,5 DUP(0),219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219,0,219,0,219,3 DUP(0),219,0,219
		BYTE 3 DUP(219),0,7 DUP(219),0,219,0,5 DUP(219),0,219,0,3 DUP(219),0,219,0,3 DUP(219),0,7 DUP(219),0,219
		BYTE 219,7 DUP(0),219,0,219,5 DUP(0),219,3 DUP(0),219,5 DUP(0),219,3 DUP(0),219,5 DUP(0),219,3 DUP(0),219
		BYTE 219,0,219,0,5 DUP(219),0,7 DUP(219),0,5 DUP(219),0,5 DUP(219),0,219,0,3 DUP(219),0,219,0,3 DUP(219)
		BYTE 219,0,219,0,219,5 DUP(0),219,0,219,0,219,0,219,0,219,0,219,0,219,0,219,0,219,0,219,5 DUP(0),219,0,219,3 DUP(0),219
		BYTE 3 DUP(219),0,219,0,3 DUP(219),0,219,0,219,0,219,0,219,0,219,0,219,0,219,0,219,0,219,0,7 DUP(219),0,219,0,3 DUP(219)
		BYTE 219,5 DUP(0),219,11 DUP(0),219,13 DUP(0),219,7 DUP(0),219
		BYTE 31 DUP(219),177,9 DUP(219)


Maze3 BYTE 41 DUP(219),177,19 DUP(219)
BYTE 219,9 DUP(0),219,13 DUP(0),219,0,219
BYTE 5 DUP(0),219,17 DUP(0),219,0,219,5 DUP(0),219,0,219
BYTE 9 DUP(219),0,5 DUP(219),0,7 DUP(219),0,219,0,3 DUP(219),0,219
BYTE 0,219,0,5 DUP(219),0,3 DUP(219),0,5 DUP(219),0,219,0,219,0,3 DUP(219),0,219,0,219
BYTE 219,7 DUP(0),219,5 DUP(0),219,5 DUP(0),219,0,219,3 DUP(0),219,0,219,0,219
BYTE 0,219,5 DUP(0),219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219,5 DUP(0),219
BYTE 219,0,219,0,9 DUP(219),0,5 DUP(219),0,219,0,3 DUP(219),0,219,0,3 DUP(219)
BYTE 0,219,0,3 DUP(219),0,3 DUP(219),0,7 DUP(219),0,3 DUP(219),0,219,0,219,0,3 DUP(219)
BYTE 219,0,219,9 DUP(0),219,5 DUP(0),219,0,219,7 DUP(0),219,7 DUP(0),219,0
BYTE 219,3 DUP(0),219,3 DUP(0),219,0,219,3 DUP(0),219,0,219,0,219,3 DUP(0),219
BYTE 219,0,3 DUP(219),0,11 DUP(219),0,219,0,7 DUP(219),0,5 DUP(219),0,5 DUP(219)
BYTE 0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219
BYTE 219,3 DUP(0),219,0,219,3 DUP(0),219,5 DUP(0),219,3 DUP(0),219,0,219,5 DUP(0)
BYTE 219,3 DUP(0),219,0,219,0,219,3 DUP(0),219,9 DUP(0),219,3 DUP(0),219,0,219,3 DUP(0),219
BYTE 219,0,3 DUP(219),0,219,0,219,0,219,0,219,0,219,0,5 DUP(219),0,3 DUP(219),0
BYTE 3 DUP(219),0,219,0,3 DUP(219),0,219,0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219,0,5 DUP(219)
BYTE 219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219,0,219,3 DUP(0),219,5 DUP(0),219,0,219
BYTE 3 DUP(0),219,7 DUP(0),219,0,219,0,219,3 DUP(0),219,0,219,3 DUP(0),219,0,219,5 DUP(0),219
BYTE 219,0,11 DUP(219),0,5 DUP(219),0,3 DUP(219),0,219,0,3 DUP(219),0,5 DUP(219)
BYTE 0,3 DUP(219),0,219,0,3 DUP(219),0,219,0,5 DUP(219),0,5 DUP(219),0,219
BYTE 219,0,219,5 DUP(0),219,7 DUP(0),219,0,219,0,219,3 DUP(0),219,0,219,0,219,3 DUP(0)
BYTE 219,3 DUP(0),219,0,219,5 DUP(0),219,0,219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219,0,219
BYTE 3 DUP(219),0,3 DUP(219),0,219,0,219,0,5 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219,0
BYTE 219,0,219,0,3 DUP(219),0,219,0,219,0,3 DUP(219),0,219,0,219,0,219,0,219,0,3 DUP(219),0,219,0,219,0,219
BYTE 219,3 DUP(0),219,3 DUP(0),219,0,219,3 DUP(0),219,5 DUP(0),219,3 DUP(0),219,0
BYTE 219,3 DUP(0),219,0,219,3 DUP(0),219,3 DUP(0),3 DUP(219),0,219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219,0,219,0,219
BYTE 219,0,3 DUP(219),0,3 DUP(219),0,219,0,5 DUP(219),0,3 DUP(219),0,219,0,219,0
BYTE 3 DUP(219),0,219,0,5 DUP(219),0,5 DUP(219),0,9 DUP(219),0,3 DUP(219),0,219,0,219
BYTE 219,0,219,7 DUP(0),219,9 DUP(0),219,0,219,3 DUP(0),219,3 DUP(0),219,5 DUP(0),219
BYTE 0,219,0,219,0,219,3 DUP(0),219,3 DUP(0),219,5 DUP(0),219,3 DUP(0),219
BYTE 219,0,13 DUP(219),0,219,0,3 DUP(219),0,7 DUP(219),0,3 DUP(219),0,219,0,3 DUP(219),0
BYTE 219,0,219,0,5 DUP(219),0,219,0,5 DUP(219),0,3 DUP(219)
BYTE 219,9 DUP(0),219,5 DUP(0),219,0,219,5 DUP(0),219,7 DUP(0),219,0,219,3 DUP(0),219
BYTE 3 DUP(0),219,0,219,7 DUP(0),219,0,219,0,219,3 DUP(0),219
BYTE 7 DUP(219),0,5 DUP(219),0,5 DUP(219),0,13 DUP(219),0,3 DUP(219),0
BYTE 219,0,3 DUP(219),0,3 DUP(219),0,219,0,3 DUP(219),0,219,0,219,0,3 DUP(219)
BYTE 219,5 DUP(0),219,5 DUP(0),219,0,219,0,219,5 DUP(0),219,7 DUP(0),219,3 DUP(0)
BYTE 219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219,0,219,0,219,5 DUP(0),219,3 DUP(0),219
BYTE 219,0,219,0,219,0,5 DUP(219),0,219,0,219,0,3 DUP(219),0,3 DUP(219),0,219,0,3 DUP(219)
BYTE 0,3 DUP(219),0,219,0,3 DUP(219),0,219,0,3 DUP(219),0,219,0,5 DUP(219),0,3 DUP(219),0,3 DUP(219)
BYTE 219,0,219,0,219,3 DUP(0),219,3 DUP(0),219,0,219,3 DUP(0),219,3 DUP(0),219,0,219,0,219
BYTE 0,219,3 DUP(0),219,0,219,0,219,3 DUP(0),219,5 DUP(0),219,5 DUP(0),219,3 DUP(0),219,3 DUP(0),219
BYTE 219,0,219,0,3 DUP(219),0,219,0,219,0,219,0,219,0,3 DUP(219),0
BYTE 5 DUP(219),0,219,0,3 DUP(219),0,3 DUP(219),0,219,0,13 DUP(219),0,219,0,5 DUP(219),0,219
BYTE 219,0,219,0,219,5 DUP(0),219,0,219,0,219,3 DUP(0),219,7 DUP(0),219
BYTE 3 DUP(0),219,3 DUP(0),219,0,219,11 DUP(0),219,0,219,0,219,7 DUP(0),219
BYTE 219,0,11 DUP(219),0,219,0,219,0,9 DUP(219),0,219,0,3 DUP(219),0
BYTE 219,0,9 DUP(219),0,3 DUP(219),0,219,0,219,0,219,0,219,0,3 DUP(219)
BYTE 219,9 DUP(0),219,0,219,3 DUP(0),219,7 DUP(0),219,3 DUP(0),219,3 DUP(0)
BYTE 219,3 DUP(0),219,0,219,5 DUP(0),219,0,219,0,219,3 DUP(0),219,0,219,0,219,3 DUP(0),219
BYTE 3 DUP(219),0,5 DUP(219),0,219,0,9 DUP(219),0,3 DUP(219),0,219,0,9 DUP(219)
BYTE 0,5 DUP(219),0,219,0,219,0,219,0,5 DUP(219),0,5 DUP(219)
BYTE 219,5 DUP(0),219,5 DUP(0),219,3 DUP(0),219,3 DUP(0),219,0,219,0,219
BYTE 0,219,11 DUP(0),219,5 DUP(0),219,5 DUP(0),219,3 DUP(0),219,3 DUP(0),219,0,219
BYTE 3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219,0,219,0,219,0
BYTE 219,0,5 DUP(219),0,219,0,7 DUP(219),0,219,0,9 DUP(219),0,219,0,3 DUP(219),0,219,0,219
BYTE 219,3 DUP(0),219,0,219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219,7 DUP(0)
BYTE 219,3 DUP(0),219,7 DUP(0),219,0,219,5 DUP(0),219,3 DUP(0),219,0,219,3 DUP(0),219,0,219,0,219
BYTE 3 DUP(219),0,219,0,5 DUP(219),0,13 DUP(219),0,219,0,9 DUP(219)
BYTE 0,5 DUP(219),0,219,0,3 DUP(219),0,5 DUP(219),0,219,0,219,0,219
BYTE 219,0,219,5 DUP(0),219,3 DUP(0),219,5 DUP(0),219,3 DUP(0),219,0,219,0
BYTE 219,5 DUP(0),219,5 DUP(0),5 DUP(219),0,219,0,219,5 DUP(0),219,3 DUP(0),219,3 DUP(0),219
BYTE 219,0,5 DUP(219),0,3 DUP(219),0,3 DUP(219),0,5 DUP(219),0,219,0,219,0,219
BYTE 0,219,0,3 DUP(219),0,3 DUP(219),0,5 DUP(219),0,219,0,219,0,3 DUP(219),0,219,0,3 DUP(219),0,3 DUP(219)
BYTE 219,0,219,0,219,5 DUP(0),219,5 DUP(0),219,3 DUP(0),219,3 DUP(0),219,0,219,0,219
BYTE 3 DUP(0),219,0,219,5 DUP(0),219,3 DUP(0),219,3 DUP(0),219,5 DUP(0),219,3 DUP(0),219,0,219
BYTE 219,0,219,0,219,0,7 DUP(219),0,3 DUP(219),0,219,0,219,0,3 DUP(219),0,3 DUP(219)
BYTE 0,7 DUP(219),0,5 DUP(219),0,5 DUP(219),0,219,0,3 DUP(219),0,3 DUP(219),0,219
BYTE 219,3 DUP(0),219,0,219,0,219,5 DUP(0),219,3 DUP(0),219,0,219,0,219,3 DUP(0),219
BYTE 9 DUP(0),219,0,219,5 DUP(0),219,3 DUP(0),219,0,219,0,219,3 DUP(0),219,3 DUP(0),219
BYTE 219,0,3 DUP(219),0,219,0,219,0,5 DUP(219),0,219,0,219,0,219,0,219,0
BYTE 9 DUP(219),0,219,0,3 DUP(219),0,3 DUP(219),0,219,0,219,0,5 DUP(219),0,3 DUP(219),0,219,0,219
BYTE 219,5 DUP(0),219,0,219,7 DUP(0),219,0,219,0,219,9 DUP(0),219,3 DUP(0),219
BYTE 3 DUP(0),219,0,219,0,219,3 DUP(0),219,7 DUP(0),219,3 DUP(0),219,0,219
BYTE 219,0,5 DUP(219),0,11 DUP(219),0,3 DUP(219),0,5 DUP(219),0,219,0
BYTE 5 DUP(219),0,219,0,219,0,13 DUP(219),0,3 DUP(219),0,219
BYTE 219,5 DUP(0),219,0,219,7 DUP(0),219,0,219,3 DUP(0),219,0,219,3 DUP(0),219,0,219,0,219
BYTE 3 DUP(0),219,0,219,3 DUP(0),219,9 DUP(0),219,0,219,3 DUP(0),219,0,219
BYTE 5 DUP(219),0,219,0,3 DUP(219),0,5 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219,0
BYTE 219,0,219,0,219,0,219,0,219,0,3 DUP(219),0,3 DUP(219),0,5 DUP(219),0,219,0,5 DUP(219),0,219
BYTE 219,3 DUP(0),219,3 DUP(0),219,5 DUP(0),219,0,219,3 DUP(0),219,3 DUP(0),219,0
BYTE 219,5 DUP(0),219,0,219,0,219,0,219,3 DUP(0),219,7 DUP(0),219,5 DUP(0),219,3 DUP(0),219
BYTE 219,0,219,0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219,0,219,0,219
BYTE 0,219,0,5 DUP(219),0,219,0,3 DUP(219),0,3 DUP(219),0,5 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219,0,219
BYTE 219,0,219,0,219,0,219,3 DUP(0),219,0,219,7 DUP(0),219,0,219,0,219,0,219,0,219
BYTE 3 DUP(0),219,0,219,7 DUP(0),219,0,219,0,219,3 DUP(0),219,7 DUP(0),219,0,219
BYTE 219,0,3 DUP(219),0,219,0,3 DUP(219),0,3 DUP(219),0,7 DUP(219),0
BYTE 7 DUP(219),0,219,0,9 DUP(219),0,219,0,219,0,3 DUP(219),0,5 DUP(219),0,219,0,219
BYTE 219,0,219,3 DUP(0),219,11 DUP(0),219,0,219,5 DUP(0),219,5 DUP(0),219
BYTE 7 DUP(0),3 DUP(219),3 DUP(0),219,0,219,3 DUP(0),219,5 DUP(0),219,0,219
BYTE 219,0,219,0,11 DUP(219),0,3 DUP(219),0,5 DUP(219),0,5 DUP(219),0,5 DUP(219)
BYTE 0,7 DUP(219),0,219,0,7 DUP(219),0,5 DUP(219)
BYTE 219,3 DUP(0),219,3 DUP(0),219,0,219,0,219,3 DUP(0),219,0,219,3 DUP(0)
BYTE 219,5 DUP(0),219,7 DUP(0),219,0,219,5 DUP(0),219,0,219,0,219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219
BYTE 219,0,219,0,219,0,219,0,219,0,219,0,3 DUP(219),0,219,0,3 DUP(219),0,3 DUP(219)
BYTE 0,3 DUP(219),0,219,0,5 DUP(219),0,3 DUP(219),0,219,0,3 DUP(219),0,219,0,3 DUP(219),0,3 DUP(219),0,219,0,219
BYTE 219,0,219,3 DUP(0),219,0,219,5 DUP(0),219,5 DUP(0),219,5 DUP(0),219,3 DUP(0)
BYTE 219,0,219,0,219,5 DUP(0),219,0,219,5 DUP(0),219,5 DUP(0),219,3 DUP(0),219,0,219
BYTE 3 DUP(219),0,3 DUP(219),0,219,0,219,0,3 DUP(219),0,3 DUP(219),0,3 DUP(219)
BYTE 0,3 DUP(219),0,5 DUP(219),0,219,0,3 DUP(219),0,5 DUP(219),0,5 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219
BYTE 219,3 DUP(0),219,0,219,3 DUP(0),219,5 DUP(0),219,5 DUP(0),219
BYTE 7 DUP(0),219,5 DUP(0),219,7 DUP(0),219,0,219,0,219,3 DUP(0),219,3 DUP(0),219,3 DUP(0),219
BYTE 219,0,3 DUP(219),0,219,0,3 DUP(219),0,13 DUP(219),0,7 DUP(219)
BYTE 0,9 DUP(219),0,219,0,219,0,219,0,3 DUP(219),0,219,0,219,0,3 DUP(219)
BYTE 219,0,219,0,219,5 DUP(0),219,5 DUP(0),219,5 DUP(0),219,0,219,7 DUP(0)
BYTE 219,0,219,5 DUP(0),219,5 DUP(0),219,3 DUP(0),219,3 DUP(0),219,0,219,0,219,0,219
BYTE 219,0,219,0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219,0,219,0
BYTE 7 DUP(219),0,219,0,5 DUP(219),0,5 DUP(219),0,219,0,5 DUP(219),0,219,0,219,0,219,0,219
BYTE 219,3 DUP(0),219,0,219,0,219,0,219,0,219,5 DUP(0),219,0,219,7 DUP(0)
BYTE 219,0,219,11 DUP(0),219,3 DUP(0),219,5 DUP(0),219,0,219,0,219,3 DUP(0),219
BYTE 3 DUP(219),0,219,0,3 DUP(219),0,7 DUP(219),0,219,0,5 DUP(219),0,3 DUP(219)
BYTE 0,3 DUP(219),0,5 DUP(219),0,3 DUP(219),0,7 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219
BYTE 219,5 DUP(0),219,5 DUP(0),219,5 DUP(0),219,0,219,11 DUP(0),219,0,219
BYTE 3 DUP(0),219,0,219,7 DUP(0),219,5 DUP(0),219,0,219,3 DUP(0),219
BYTE 3 DUP(219),0,5 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219,0,3 DUP(219),0
BYTE 5 DUP(219),0,3 DUP(219),0,3 DUP(219),0,7 DUP(219),0,3 DUP(219),0,3 DUP(219),0,219,0,3 DUP(219),0,219
BYTE 219,5 DUP(0),219,9 DUP(0),219,3 DUP(0),3 DUP(219),3 DUP(0),219,3 DUP(0)
BYTE 219,9 DUP(0),219,7 DUP(0),219,0,219,5 DUP(0),219,3 DUP(0),177
BYTE 61 DUP(219)


.code
main PROC
	; Get the Console standard output handle:
	INVOKE GetStdHandle, STD_OUTPUT_HANDLE
	mov consoleHandle,eax    
	INVOKE GetStdHandle, STD_OUTPUT_HANDLE ; Get the console ouput handle
    mov outputHandle, eax ; save console handle
DRAW: 
	mov mapPosition.x,0
	mov mapPosition.y,0
	call Clrscr
      
    mov ecx,MazeHeight    ; number of lines in body
    mov edi,offset MazeBlank
L1: push ecx  ; 
    INVOKE WriteConsoleOutputAttribute,
      outputHandle,
      addr color,
      MazeWidth,
      mapPosition,
      ADDR count
    INVOKE WriteConsoleOutputCharacter,
       outputHandle,   ; console output handle
       edi,   ; pointer to the top Maze line
       MazeWidth,   ; size of Maze line
       mapPosition,   ; coordinates of first char
       ADDR bytesWritten    ; output count
    inc mapPosition.y   ; next line
    add edi,MazeWidth
    pop ecx   ; restore counter
loop L1



START:
	INVOKE SetConsoleCursorPosition, consoleHandle , xyPos
	call ReadChar
UP:
	cmp ax,4800h ;UP
		jne DOWN
		sub xyPos.y,1
		mov esi,offset Maze
		mov ax,xyPos.y
		movzx ecx,ax
UPDOWN1:
		add esi,MazeWidth
loop UPDOWN1
		mov ax,xyPos.x
		add si,ax
		mov al,[esi]
		cmp al,219
		jne Blind
		add xyPos.y,1
		jmp Blind
DOWN:
	cmp ax,5000h ;DOWN
		jne LEFT
		add xyPos.y,1
		mov esi,offset Maze
		mov ax,xyPos.y
		movzx ecx,ax
UPDOWN2:
		add esi,MazeWidth
		loop UPDOWN2
		mov ax,xyPos.x
		add si,ax
		mov al,[esi]
		cmp al,219
		jne Blind
		sub xyPos.y,1
		jmp Blind
LEFT:
	cmp ax,4B00h ;LEFT
		jne RIGHT
		sub xyPos.x,1
		mov esi,offset Maze
		mov ax,xyPos.y
		movzx ecx,ax
UPDOWN3:
		add esi,MazeWidth
		loop UPDOWN3
		mov ax,xyPos.x
		add si,ax
		mov al,[esi]
		cmp al,219
		jne Blind
		add xyPos.x,1
		jmp Blind
RIGHT:
	cmp ax,4D00h ;RIGHT
		jne BYE
		add xyPos.x,1
		mov esi,offset Maze
		mov ax,xyPos.y
		movzx ecx,ax
UPDOWN4:
		add esi,MazeWidth
		loop UPDOWN4
		mov ax,xyPos.x
		add si,ax
		mov al,[esi]
		cmp al,219
		jne Blind
		sub xyPos.x,1
		jmp Blind
BYE:
	cmp ax,011Bh ;ESC
		je END_FUNC
	

Blind:
	movzx eax , xyPos.x
	movzx ecx , xyPos.y
	mov esi , OFFSET MazeBlank
	mov edi , OFFSET Maze
	ADD esi , eax
	ADD edi , eax
MU:
	ADD esi , MazeWidth
	ADD edi , MazeWidth
loop MU
	mov al , [edi]	;mid
	mov [esi] , al

	mov al , [edi+1];right
	mov [esi+1] , al

	mov al , [edi-1];left
	mov [esi-1] , al

	mov al , [edi+MazeWidth];down
	mov [esi+MazeWidth] , al

	mov al , [edi-MazeWidth];up
	mov [esi-MazeWidth] , al

	mov al , [edi+MazeWidth-1]
	mov [esi+MazeWidth-1] , al

	mov al , [edi-MazeWidth-1]
	mov [esi-MazeWidth-1] , al

	mov al , [edi+MazeWidth+1]
	mov [esi+MazeWidth+1] , al

	mov al , [edi-MazeWidth+1]
	mov [esi-MazeWidth+1] , al
	
	mov mapPosition.x , 0
	mov mapPosition.y , 0

	mov ecx, MazeHeight
	mov esi , OFFSET MazeBlank
PrintA:
	push ecx
	INVOKE WriteConsoleOutputAttribute,
	 outputHandle,
	 ADDR color,
	 MazeWidth,
	 mapPosition,
	 ADDR count
	INVOKE WriteConsoleOutputCharacter,
	 outputHandle,   ; console output handle
	 esi,   ; pointer to the top Maze line
	 MazeWidth,   ; size of Maze line
	 mapPosition,   ; coordinates of first char
	 ADDR cellsWritten    ; output count
	
	ADD esi , MazeWidth
	inc mapPosition.y
	pop ecx
loop PrintA

	cmp xyPos.x,20
	jne START
	cmp xyPos.y,1
	jne START
	call Clrscr
	
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;<<<<<<<<<<<<<<<<<<<<<<second
	mov bytesWritten , 0
	mov count , 0
	mov cellsWritten , 0

	mov ecx,MazeHeight*MazeWidth
	mov esi, OFFSET MazeBlank
	mov edi, OFFSET MazeClear
	mov al, [edi]
CLEAN:
	mov[esi],al
	inc esi
LOOP CLEAN

DRAWQ: 
	mov mapPosition.x,0
	mov mapPosition.y,0
	mov xyPos.x , 3
	mov xyPos.y , 0

      
    mov ecx,MazeHeight2    ; number of lines in body
    mov edi,offset MazeBlank2
L1Q: push ecx 
    INVOKE WriteConsoleOutputAttribute,
      outputHandle,
      addr color2,
      MazeWidth2,
      mapPosition,
      ADDR count
    INVOKE WriteConsoleOutputCharacter,
       outputHandle,   ; console output handle
       edi,  
       MazeWidth2,   ; size of Maze line
       mapPosition,   ; coordinates of first char
       ADDR bytesWritten    ; output count
    inc mapPosition.y   ; next line
    add edi,MazeWidth2
    pop ecx   ; restore counter
loop L1Q



STARTQ:
	INVOKE SetConsoleCursorPosition, consoleHandle , xyPos
	call ReadChar
UPQ:
	cmp ax,4800h ;UP
		jne DOWNQ
		sub xyPos.y,1
		mov esi,OFFSET Maze2
		mov ax,xyPos.y
		movzx ecx,ax
UPDOWN1Q:
		add esi,MazeWidth2
loop UPDOWN1Q
		mov ax,xyPos.x
		add si,ax
		mov al,[esi]
		cmp al,219
		jne BlindQ
		add xyPos.y,1
		jmp BlindQ
DOWNQ:
	cmp ax,5000h ;DOWN
		jne LEFTQ
		add xyPos.y,1
		mov esi,offset Maze2
		mov ax,xyPos.y
		movzx ecx,ax
UPDOWN2Q:
		add esi,MazeWidth2
loop UPDOWN2Q
		mov ax,xyPos.x
		add si,ax
		mov al,[esi]
		cmp al,219
		jne BlindQ
		sub xyPos.y,1
		jmp BlindQ
LEFTQ:
	cmp ax,4B00h ;LEFT
		jne RIGHTQ
		sub xyPos.x,1
		mov esi,offset Maze2
		mov ax,xyPos.y
		movzx ecx,ax
UPDOWN3Q:
		add esi,MazeWidth2
	loop UPDOWN3Q
		mov ax,xyPos.x
		add si,ax
		mov al,[esi]
		cmp al,219
		jne BlindQ
		add xyPos.x,1
		jmp BlindQ
RIGHTQ:
	cmp ax,4D00h ;RIGHT
		jne BYEQ
		add xyPos.x,1
		mov esi,offset Maze2
		mov ax,xyPos.y
		movzx ecx,ax
UPDOWN4Q:
		add esi,MazeWidth2
	loop UPDOWN4Q
		mov ax,xyPos.x
		add si,ax
		mov al,[esi]
		cmp al,219
		jne BlindQ
		sub xyPos.x,1
		jmp BlindQ
BYEQ:
	cmp ax,011Bh ;ESC
		je END_FUNC
	

BlindQ:
	movzx eax , xyPos.x
	movzx ecx , xyPos.y
	mov esi , OFFSET MazeBlank2
	mov edi , OFFSET Maze2
	ADD esi , eax
	ADD edi , eax
MUQ:
	ADD esi , MazeWidth2
	ADD edi , MazeWidth2
loop MUQ
	mov al , [edi]	;mid
	mov [esi] , al

	mov al , [edi+1];right
	mov [esi+1] , al

	mov al , [edi-1];left
	mov [esi-1] , al

	mov al , [edi+MazeWidth2];down
	mov [esi+MazeWidth2] , al

	mov al , [edi-MazeWidth2];up
	mov [esi-MazeWidth2] , al

	mov al , [edi+MazeWidth2-1]
	mov [esi+MazeWidth2-1] , al

	mov al , [edi-MazeWidth2-1]
	mov [esi-MazeWidth2-1] , al

	mov al , [edi+MazeWidth2+1]
	mov [esi+MazeWidth2+1] , al

	mov al , [edi-MazeWidth2+1]
	mov [esi-MazeWidth2+1] , al
	
	mov mapPosition.x , 0
	mov mapPosition.y , 0

	mov ecx, MazeHeight2
	mov esi , OFFSET MazeBlank2
PrintAQ:
	push ecx
	INVOKE WriteConsoleOutputAttribute,
	 outputHandle,
	 ADDR color2,
	 MazeWidth2,
	 mapPosition,
	 ADDR count
	INVOKE WriteConsoleOutputCharacter,
	 outputHandle,   ; console output handle
	 esi,   ; pointer to the top Maze line
	 MazeWidth2,   ; size of Maze line
	 mapPosition,   ; coordinates of first char
	 ADDR cellsWritten    ; output count
	
	ADD esi , MazeWidth2
	inc mapPosition.y
	pop ecx
loop PrintAQ

	cmp xyPos.x,31
	jne STARTQ
	cmp xyPos.y,40
	jne STARTQ
	call Clrscr
;;;;;;;;;;;;;;;;;;<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<third
	mov bytesWritten , 0
	mov count , 0
	mov cellsWritten , 0

	mov ecx,MazeHeight2*MazeWidth2
	mov esi, OFFSET MazeBlank2
	mov edi, OFFSET MazeClear
	mov al, [edi]
CLEANP:
	mov [esi],al
	inc esi
LOOP CLEANP

DRAWQP: 
	mov mapPosition.x,0
	mov mapPosition.y,0
	mov xyPos.x , 41
	mov xyPos.y , 0

      
    mov ecx,MazeHeight3    ; number of lines in body
    mov edi,offset MazeBlank3
L1QP: push ecx 
    INVOKE WriteConsoleOutputAttribute,
      outputHandle,
      addr color3,
      MazeWidth3,
      mapPosition,
      ADDR count
    INVOKE WriteConsoleOutputCharacter,
       outputHandle,   ; console output handle
       edi,  
       MazeWidth3,   ; size of Maze line
       mapPosition,   ; coordinates of first char
       ADDR bytesWritten    ; output count
    inc mapPosition.y   ; next line
    add edi,MazeWidth3
    pop ecx   ; restore counter
loop L1QP



STARTQP:
	INVOKE SetConsoleCursorPosition, consoleHandle , xyPos
	call ReadChar
UPQP:
	cmp ax,4800h ;UP
		jne DOWNQP
		sub xyPos.y,1
		mov esi,OFFSET Maze3
		mov ax,xyPos.y
		movzx ecx,ax
UPDOWN1QP:
		add esi,MazeWidth3
loop UPDOWN1QP
		mov ax,xyPos.x
		add si,ax
		mov al,[esi]
		cmp al,219
		jne BlindQP
		add xyPos.y,1
		jmp BlindQP
DOWNQP:
	cmp ax,5000h ;DOWN
		jne LEFTQP
		add xyPos.y,1
		mov esi,offset Maze3
		mov ax,xyPos.y
		movzx ecx,ax
UPDOWN2QP:
		add esi,MazeWidth3
loop UPDOWN2QP
		mov ax,xyPos.x
		add si,ax
		mov al,[esi]
		cmp al,219
		jne BlindQP
		sub xyPos.y,1
		jmp BlindQP
LEFTQP:
	cmp ax,4B00h ;LEFT
		jne RIGHTQP
		sub xyPos.x,1
		mov esi,offset Maze3
		mov ax,xyPos.y
		movzx ecx,ax
UPDOWN3QP:
		add esi,MazeWidth3
	loop UPDOWN3QP
		mov ax,xyPos.x
		add si,ax
		mov al,[esi]
		cmp al,219
		jne BlindQP
		add xyPos.x,1
		jmp BlindQP
RIGHTQP:
	cmp ax,4D00h ;RIGHT
		jne BYEQP
		add xyPos.x,1
		mov esi,offset Maze3
		mov ax,xyPos.y
		movzx ecx,ax
UPDOWN4QP:
		add esi,MazeWidth3
	loop UPDOWN4QP
		mov ax,xyPos.x
		add si,ax
		mov al,[esi]
		cmp al,219
		jne BlindQP
		sub xyPos.x,1
		jmp BlindQP
BYEQP:
	cmp ax,011Bh ;ESC
		je END_FUNC
	

BlindQP:
	movzx eax , xyPos.x
	movzx ecx , xyPos.y
	mov esi , OFFSET MazeBlank3
	mov edi , OFFSET Maze3
	ADD esi , eax
	ADD edi , eax
MUQP:
	ADD esi , MazeWidth3
	ADD edi , MazeWidth3
loop MUQP
	mov al , [edi]	;mid
	mov [esi] , al

	mov al , [edi+1];right
	mov [esi+1] , al

	mov al , [edi-1];left
	mov [esi-1] , al

	mov al , [edi+MazeWidth3];down
	mov [esi+MazeWidth3] , al

	mov al , [edi-MazeWidth3];up
	mov [esi-MazeWidth3] , al

	mov al , [edi+MazeWidth3-1]
	mov [esi+MazeWidth3-1] , al

	mov al , [edi-MazeWidth3-1]
	mov [esi-MazeWidth3-1] , al

	mov al , [edi+MazeWidth3+1]
	mov [esi+MazeWidth3+1] , al

	mov al , [edi-MazeWidth3+1]
	mov [esi-MazeWidth3+1] , al
	
	mov mapPosition.x , 0
	mov mapPosition.y , 0

	mov ecx, MazeHeight3
	mov esi , OFFSET MazeBlank3
PrintAQP:
	push ecx
	INVOKE WriteConsoleOutputAttribute,
	 outputHandle,
	 ADDR color3,
	 MazeWidth3,
	 mapPosition,
	 ADDR count
	INVOKE WriteConsoleOutputCharacter,
	 outputHandle,   ; console output handle
	 esi,   ; pointer to the top Maze line
	 MazeWidth3,   ; size of Maze line
	 mapPosition,   ; coordinates of first char
	 ADDR cellsWritten    ; output count
	
	ADD esi , MazeWidth3
	inc mapPosition.y
	pop ecx
loop PrintAQP

	cmp xyPos.x,60
	jne STARTQP
	cmp xyPos.y,59
	jne STARTQP
	call Clrscr
;;;;;;;;;;;;;;;;;;;;;

END_FUNC:

	call WaitMsg
	exit

main ENDP
END main