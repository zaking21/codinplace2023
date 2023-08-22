import graphics

import time

import random

import math

CANVAS_WIDTH = 500

CANVAS_HEIGHT = 600

PADDLE_Y = CANVAS_HEIGHT - 100

PADDLE_WIDTH = 80

PADDLE_HEIGHT = 15

BALL_RADIUS = 10

BRICK_GAP = 5

BRICK_WIDTH = (CANVAS_WIDTH-BRICK_GAP*9) / 10

BRICK_HEIGHT = 10

canvas = graphics.Canvas(500, 600)

DELAY=.01

ball_x = 245
    
ball_y = 295


paddle_z = canvas.create_rectangle(0, 500, 0, 500)

def main():

    canvas

    # TODO: your code here
    
    
    
    create_bricks()

    change_x=random.randint(2,4)

    change_y=random.randint(7, 10)
    

    
    blocks = 100

    ball = canvas.create_oval(ball_x, ball_y, ball_x + BALL_RADIUS, ball_y + BALL_RADIUS)
    
    paddle_thick = canvas.create_rectangle(210, PADDLE_Y, 290, PADDLE_HEIGHT+PADDLE_Y, 'purple')
    
    paddle = canvas.create_rectangle(210, PADDLE_Y, 290, PADDLE_Y, 'purple')
    
    start_words = canvas.create_text (65, 200, 'Click Mouse to Start', color = 'grey', font = 'courier', font_size = 30)
    
    clicks = canvas.get_new_mouse_clicks()
    
    canvas.wait_for_click()
    
    canvas.delete(start_words)
    
    change_delay = .01
    
    while True:

        canvas.move(ball, change_x, change_y)     

        cur_x = canvas.get_left_x(ball)

        cur_y = canvas.get_top_y(ball)

        if cur_x > CANVAS_WIDTH - 10 or cur_x < 0:

            change_x =-change_x

            

        if cur_y > CANVAS_HEIGHT-10 or cur_y<0:

            change_y=-change_y
        
            

        mouse_x = canvas.get_mouse_x()
        
        canvas.moveto(paddle, mouse_x - 45, 500)
        canvas.moveto(paddle_thick, mouse_x - 45, 500)
        
    
        
        overlapping_objects = canvas.find_overlapping(cur_x, cur_y, cur_x + BALL_RADIUS, cur_y + BALL_RADIUS)
        
        
        for overlapping_object in overlapping_objects:
            if overlapping_object != ball and overlapping_object != paddle and overlapping_object != paddle_thick:
                canvas.delete(overlapping_object)
            
        for overlapping_object in overlapping_objects:   
            if overlapping_object == paddle:
                change_y = -change_y
        
        for overlapping_object in overlapping_objects:   
            if overlapping_object != ball and overlapping_object != paddle and overlapping_object != paddle_thick:
                change_y = -change_y
                
                blocks = blocks - 1     
                
                
        
        
        if cur_y >= CANVAS_HEIGHT-10:
            canvas.move(ball, 10, 10) 
            game_lost()
        
        if blocks == 0:
            canvas.move(ball, 10, 10) 
            game_won()
            
        
        if blocks == 80:
            change_delay = .001
            
        
        if blocks == 60:
            change_delay = .0001
            
            
            
        if blocks == 40:
            change_delay = .00001
            
        
        time.sleep(change_delay)
        

def game_won():
    canvas.create_rectangle(CANVAS_WIDTH/2 + 200, CANVAS_HEIGHT/2 + 200, CANVAS_WIDTH/2 - 200, CANVAS_HEIGHT/2 - 200)
    canvas.create_text (170, 200, 'Game Over', color = 'red', font = 'courier', font_size = 30)
    canvas.create_text (190, 260, 'You Win', color = 'green', font = 'courier', font_size = 30)
    


def game_lost():
    canvas.create_rectangle(CANVAS_WIDTH/2 + 200, CANVAS_HEIGHT/2 + 200, CANVAS_WIDTH/2 - 200, CANVAS_HEIGHT/2 - 200)
    canvas.create_text (170, 200, 'Game Over', color = 'red', font = 'courier', font_size = 30)
    canvas.create_text (180, 260, 'You Lost', color = 'red', font = 'courier', font_size = 30)
    
    
    
def create_bricks():

    canvas

    color=['red', 'orange', 'yellow', 'green', 'cyan']

    start_x = 0

    start_y = 40

    end_x = BRICK_WIDTH

    end_y = start_y+BRICK_HEIGHT

    color_index = 0

    for y in range(5):

        for x in range(2):    

            for i in range (10):

                Object_ID = canvas.create_rectangle(start_x, start_y, end_x, end_y, color[color_index])

                start_x = end_x + BRICK_GAP

                end_x = start_x+BRICK_WIDTH

            start_x = 0

            end_x = BRICK_WIDTH

            start_y = start_y + BRICK_HEIGHT + BRICK_GAP

            end_y = start_y + BRICK_HEIGHT

        color_index = color_index + 1

    

        
if __name__ == "__main__":
    main()