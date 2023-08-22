from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

DELAY = 0.09 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    ax = 0
    ay = 0
    
    #create player
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, "blue")
    
    #create the goal rectangle
    goal_x = 360
    goal_y = 360
    goal = canvas.create_rectangle(goal_x, goal_y, goal_x + SIZE, goal_y + SIZE,"red")
    
    direction = 'Right'
    count = 0
    
    while True:
        #handle key press
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            direction = 'Left'
        elif key == 'ArrowRight':
            direction = 'Right'
        elif key == 'ArrowUp':
            direction = 'Up'
        elif key == 'ArrowDown':
            direction = 'Down'
        
        #update the player's position
        if direction == 'Left':
            ax -= SIZE
        elif direction == 'Right':
            ax += SIZE
        elif direction == 'Up':
            ay-= SIZE
        else:  # direction == 'Down'
            ay += SIZE
        
        #change player possition
        canvas.moveto(player, ax, ay)
        
        #check for out of bounds
        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)
        if player_x < 0 or player_x >= CANVAS_WIDTH or player_y < 0 or player_y >= CANVAS_HEIGHT:
            break
        
        #detecting collisions
        goal_x = canvas.get_left_x(goal)
        goal_y = canvas.get_top_y(goal)
        goal_right = goal_x + SIZE
        goal_bottom = goal_y + SIZE
        
        if player_x < goal_right and player_x + SIZE > goal_x and player_y < goal_bottom and player_y + SIZE > goal_y:
            move_goal(canvas, goal)
            count += 1
        
        #print points
        text_obj = canvas.create_text(350, 387,text=f"{count} points")
        
        #sleep    
        time.sleep(DELAY)
        
        #delete old points text
        canvas.delete(text_obj)
        
    #show end points
    result = f"Your Score is : {str(count)}"
    canvas.create_text((CANVAS_WIDTH/2)-30, CANVAS_HEIGHT/2, 'Game Over', color='red')
    canvas.create_text((CANVAS_WIDTH/2)-40, (CANVAS_HEIGHT/2)+14, result, color='blue')
    
# Move the goal to a new location
def move_goal(canvas, goal):
    goal_x = random.randint(0, CANVAS_WIDTH // SIZE - 1) * SIZE
    goal_y = random.randint(0, CANVAS_HEIGHT // SIZE - 1) * SIZE
    canvas.moveto(goal, goal_x, goal_y)

if __name__ == '__main__':
    main()