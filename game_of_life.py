import random
from tracemalloc import start
import keyboard
import time



def dead_state(height: int, width:int) -> list:
    
    return [[0]*width for i in range(height)]





def random_state(height: int, width:int) -> list:

    state = dead_state(height,width)

    for i in range(height):
        for j in range(width):
            
            if random.random()>=0.5:
                state[i][j] = 1

    return state


def render(state):

    width = len(state[0])
    
    yborder = "_"*(2*width+1)
    
    

    print(yborder)

    for row in state:
        print("|"+' '.join(['*' if x==1 else ' ' for x in row])+"|")
    print(yborder)

    return


def next_board_state(initial):

    height, width = len(initial), len(initial[0])

    next = dead_state(height,width)

    for i in range(height):
        yborder= 0
        if i ==0 or i == height-1:
            yborder = 1

        for j in range(width):
            xborder = 0
            if j==0 or j==width-1:
                xborder = 1

            curr_cell = initial[i][j]
            neighbors = 0

            ystart,yend = int( (i-1)+yborder*(1-(i/(height-1))) ), int( (i+2) - yborder*(i/(height-1)) )
            xstart,xend = int( (j-1)+xborder*(1-(j/(width-1))) ), int( (j+2) - xborder*(j/(width-1)) )

            for y in range(ystart,yend):
                
                for x in range(xstart,xend):

                    if initial[y][x]==1:
                        
                        neighbors+=1

            
            neighbors -= curr_cell

            if curr_cell:
                if 2<=neighbors<=3:
                    next[i][j] = 1
            else:
                if neighbors==3:
                    next[i][j] = 1
    
    return next


def start_life():

    initial = random_state(20,20)

    state = initial

    while(True):
        time.sleep(1)
        if keyboard.is_pressed('space'):
            print("Life has ended...")
            break
        
        render(state)

        state = next_board_state(state)

    return

def main():

    print("Start life?")

    if input() == 'n':
        print("Exiting...")
        return

    else:
        start_life()

main()





    
