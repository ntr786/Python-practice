
from karel.stanfordkarel import *

def main():
    #initially written codes are commented out here.
    # karel is writing STOP

    # draw S
    pattern_o_red()
    move()
    move()
    turn_right()
    move()
    paint_corner("white")
    pick_beeper()
    move()
    turn_right()
    move()
    paint_corner("red")
    put_beeper()
    move()
    turn_left()
    move()
    paint_corner("white")
    pick_beeper()

    
    """paint_corner("red")
    put_beeper()
    step2()
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()
    turn_left()
    move()
    paint_corner("red")
    put_beeper()
    turn_around()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    step()
    turn_right()
    step()
    step()
    turn_right()
    step()
    step()"""
   # move to T 
    turn_around()
    for i in range(2):
        for j in range(4):
            move()
        turn_right()
    move()
    turn_left()
    
    # draw T
    stick_red()
    turn_around()
    for i in range(3):
        move()
    turn_left()
    stick_red()

    # move to O
    turn_around()
    for i in range(5):
        move()
    turn_right()
    for i in range(4):
        move()
    """step5()
    turn_right()
    step_blank4()
    turn_right()
    move()
    step()
    turn_right()
    step3()
    turn_right()
    step_blank4()
    turn_left()
    #step()
    move()
    turn_right()"""
    pattern_o_red()

    """step()
    step()
    turn_right()
    step()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    step()
    turn_left()
    step2()
    turn_right()
    step2()
    turn_right()
    step3()
    turn_right()"""

    step_blank4()
    pattern_o_red()
    diagonal_red()
    move()
    turn_right()
    for i in range(3):
        move()
        paint_corner("white")
        pick_beeper()
    turn_right()
    move()
    paint_corner("white")
    pick_beeper()
        

    """put_beeper()
    turn_left()
    step()
    turn_right()
    step2()
    turn_right()
    step2()
    turn_right()
    step2()
    turn_left()
    step2()"""

# move to G
    move()
    turn_right()
    for i in range(2):
        for j in range(5):
            move()
        turn_right()
    move()
    turn_left()

    """turn_left()
    step_blank4()
    turn_right()"""

# karel is writing GENOCIDE
# in 2 step:
# 1st step GENO in 20

# draw G
    """put_beeper()
    step2()
    step_blank2()
    turn_left()
    step_blank2()
    turn_left()
    step2()
    turn_left()
    step()
    turn_right()
    step_blank2()
    put_beeper()
    turn_right()
    step3()
    turn_right()
    step2()"""
    pattern_o_black()
    move()
    move()
    turn_right()
    move()
    paint_corner("white")
    pick_beeper()
    move()
    turn_left()
    move()
    paint_corner("black")
    put_beeper()

# move to E    
    move()
    move()
    turn_left()
    move()
    move()
    turn_right()

# draw E
    pattern_o_black()
    move()
    move()
    turn_right()
    for i in range(3):
        move()
        paint_corner("white")
        pick_beeper()
    turn_right()
    move()
    turn_right()
    move()
    paint_corner("black")
    put_beeper()


      
    """step_blank2()
    step3()
    turn_right()
    move()
    turn_right()
    step_blank2()
    put_beeper()
    turn_left()
    step3()
    turn_left()
    step2()
    turn_left()
    step_blank2()
    turn_left()
    step()
    turn_around()"""

# move to N
    move()
    move()
    turn_right()
    for i in range(3):
        move()

# draw N
    turn_right()
    stick_black() # have a straight line 
    turn_around()
    for i in range(5):
        move()
    turn_right()
    for i in range(4):
        diagonal_black()
    turn_left()
    stick_black()

# move to O
    turn_around()
    move()
    turn_left()
    move()
    move()

# draw O
    pattern_o_black()

    """step()
    turn_right()
    step2()
    turn_right()
    move()
    turn_right()
    step_blank4()
    turn_right()
    step()
    turn_right()
    step()
    turn_around()
    move()
    turn_right()
    
    # diagonal line

    for i in range(4):
        diagonal_red()

    
    turn_left()
    step4()
    turn_right()
    step_blank2()
    step2()
    turn_right()
    step4()
    turn_right()
    step2()
    turn_right()
    step4()
    turn_right()
    step_blank4()"""

# 2nd step CIDE in 14


    """ firstly make the pattern of O
    for i in range(2):
        for j in range(2):
            step()

        turn_right()

        for j in range(4):
            step()

        turn_right()"""

    
# move to C
    for i in range(4):
        move()

    # draw C
    pattern_o_black()
    move()
    move()
    turn_right()
    for i in range(3):
        move()
        paint_corner("white")
        pick_beeper()

# move to next letter
    move()
    turn_left()
    move()
    move()
    turn_left()

# draw I

    for i in range(5):
        paint_corner("black")
        put_beeper()
        move()

# move to next letter
    turn_right()
    move()
    move()
    turn_right()
    move()
    turn_left()

# draw D
    pattern_o_black()
    move()
    move()
    paint_corner("white")
    pick_beeper()
    turn_right()

    for i in range(4):
        move()
    paint_corner("white")
    pick_beeper()
    
# move to next letter 
    turn_left()
    move()
    move()
    turn_left()
    for i in range(4):
        move()
    turn_right()

# draw E
    pattern_o_black()
    move()
    move()
    turn_right()
    for i in range(3):
        move()
        paint_corner("white")
        pick_beeper()
    turn_around()
    move()
    turn_left()
    move()
    paint_corner("black")
    put_beeper()
    turn_around()
    while front_is_clear():
        move()

    # go to the next phase of the drawing
    turn_left()
    for i in range(7):
        move()

    turn_left()
    for i in range(26):
        move()
    
    # Draw the left half of the heart
    
    for i in range(9):
        diagonal_red()
    turn_right()
    for i in range(5):
        move()
        paint_corner("red")
        put_beeper()
    
    for i in range(5):
        diagonal_red()
    turn_right()
    for i in range(4):
        diagonal_red()
    turn_left()
    for i in range(4):
        diagonal_red()
    turn_right()
    for i in range(5):
        diagonal_red()
    turn_right()
    for i in range(5):
        move()
        paint_corner("red")
        put_beeper()
    for i in range(9):
        diagonal_red()

    # Go to writing position
    turn_around()
    for i in range (13):
        move()
    turn_left()
    for i in range(9):
        move()
    turn_around()

    #write GAZA
    # G
    pattern_o_black()
    move()
    move()
    turn_right()
    move()
    paint_corner("white")
    pick_beeper()
    move()
    turn_left()
    move()
    paint_corner("black")
    put_beeper()

    #move to A
    turn_right()
    move()
    move()
    move()
    turn_left()
    move()
    move()
    turn_left()

    #write A
    for i in range(4):
        move()
        paint_corner("black")
        put_beeper()
    turn_right()
    move()
    turn_left()
    move()
    paint_corner("black")
    put_beeper()
    turn_right()
    move()
    paint_corner("black")
    put_beeper()
    move()
    turn_right()
    for i in range(4):
        move()
        paint_corner("black")
        put_beeper()
    
    #move to Z
    turn_left()
    move()
    move()

    # draw Z (same code of N)
    stick_black() # have a straight line 
    turn_around()
    for i in range(5):
        move()
    turn_right()
    for i in range(4):
        diagonal_black()
    turn_left()
    stick_black()

    #to remove the last coloumn of Z (to make it short)
    turn_around()
    for i in range(5):
        move()
    paint_corner("white")
    pick_beeper()

    turn_right()
    for i in range(4):
        move()
    paint_corner("white")
    pick_beeper()

    #move to A
    turn_left()
    move()
    turn_left()

    # A
    for i in range(4):
        paint_corner("black")
        put_beeper()
        move()
    turn_right()
    move()
    paint_corner("black")
    put_beeper()
    move()
    paint_corner("black")
    put_beeper()
    move()
    turn_right()
    
    for i in range(4):
        move()
        paint_corner("black")
        put_beeper()


        
    
    """#write A
    for i in range(5):
        diagonal_black()

    turn_right()
    for i in range(4):
        diagonal_black()

    for i in range (4):
        diagonal_black()"""
    
    
    


def turn_around():
    turn_left()
    turn_left()

def step():
    move()
    put_beeper()

def step3():
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

def step4():
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step_blank2():
    move()
    move()

def step5():
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

def step_blank4():
    move()
    move()
    move()
    move()

def step2():
    move()
    put_beeper()
    move()
    put_beeper()

def diagonal_red():
        move()
        turn_right()
        move()
        paint_corner("red")
        put_beeper()
        turn_left()

def diagonal_black():
        move()
        turn_right()
        move()
        paint_corner("black")
        put_beeper()
        turn_left()

def diagonal_white():
        move()
        turn_right()
        move()
        paint_corner("white")
        put_beeper()
        turn_left()

def pattern_o_red():
    for i in range(2):
        for j in range(2):
            paint_corner("red")
            step()

        turn_right()

        for j in range(4):
            paint_corner("red")
            step()

        turn_right()

def pattern_o_black():
    for i in range(2):
        for j in range(2):
            paint_corner("black")
            step()

        turn_right()

        for j in range(4):
            paint_corner("black")
            step()

        turn_right()

def stick_black():
    for i in range(5):
        paint_corner("black")
        put_beeper()
        move()

def stick_red():
    for i in range(5):
        paint_corner("red")
        put_beeper()
        move()
# don't change this code
if __name__ == '__main__':
    main()