######################################################
# Project: <Project 2>
# UIN: <650266104>
# repl.it URL: <https://replit.com/@huangwo2017/project2starter#main.py> 
######################################################

#import turtle module
import turtle

#import random module
import random

def main():
  # Turtle object variables and settings
  s = turtle.Screen()
  # set screen background color
  s.bgcolor("#00B5E2")
  # update screen size as specified
  s.screensize(500, 500)
  s.setup(520, 520)  # slightly larger to avoid scrollbars

  # add shape for turtle
  s.addshape("tumblr_inline_mg16cuvZLO1roozkr540.gif")
  s.addshape("869350_50w_50h_zc.gif")
  
  s.bgpic("way2.gif")

  # disable screen updating; we control in animation loop
  s.tracer(0)

  # add first turtle
  t1 = turtle.Turtle()
  t1.penup()
  t1.shape("tumblr_inline_mg16cuvZLO1roozkr540.gif")
  t1.goto(-50,300)

  # add second turtle
  t2 = turtle.Turtle()
  t2.penup()
  t2.shape("869350_50w_50h_zc.gif")
  t2.goto(50,300)

  # add third turtle
  t3 = turtle.Turtle()
  t3.penup()
  t3.shape("869350_50w_50h_zc.gif")
  t3.goto(0,-225)

  # animation variables
  status = "Play"
  move_distance = .1

  # update variables for width and height 
  #       as expressions of screensize
  screen_width = 400
  screen_height = 500
  

  # teach how to play game
  t4 = turtle.Turtle()
  t4.penup()
  t4.goto(-255,100)
  t4.hideturtle()

  t4.write("Press left arrow button to move your car to go left, ", move=False, align='left', font=('Arial', 15, 'normal'))
  
  t4.goto(-255,50)
  t4.write("and press right arrow button to go right. Kill rabbit", move=False, align='left', font=('Arial', 15, 'normal'))
  
  t4.goto(-255,0)
  t4.write("can earn 10 score. Be careful the other car. Please", move=False, align='left', font=('Arial', 15, 'normal'))

  t4.goto(-255,-50)
  t4.write("press space button to start the game. Have fun!", move=False, align='left', font=('Arial', 15, 'normal'))

  # game function
  def func():

    t4.goto(-250,200)
    
    # set score, life, level
    score = 0
    life = 3
    level = 1
    
    # animation loop
    while (status == "Play"):
      # clear current drawings
      t1.clear()
      t2.clear()
      t4.clear()

      # update any values
      # calculate random x for first turtle
      random_x1 = random.randint(-250, 250)
      # calculate values for second turtle
      random_x2 = random.randint(-250, 250)
    
      t4.write("Score: "+ str(score) +' Lives: ' + str(life) + '  Level: ' + str(level), move=False, align='left', font=('Arial', 24, 'normal'))

      # handle edge condition
      current_y1 = t1.ycor()
      new_y1 = current_y1 - (int(level)*(move_distance))

      if (new_y1 <= -(screen_height/2) ):
        new_y1 = current_y1 + screen_height
        t1.setx(random_x1)
    
      if t3.distance(t1) <= 50:
        new_y1 = current_y1 + screen_height
        t1.setx(random_x1)
        t1.sety(new_y1)
        score += 10
        if score != 0:
          if score % 100 == 0:
            level += 1

      # handle edge for second turtle
      current_y2 = t2.ycor()
      new_y2 = current_y2 - (int(level)*(move_distance))
    
      if (new_y2 <= -(screen_height/2) ):
        new_y2 = current_y2 + screen_height
        t2.setx(random_x2)
    
      if t3.distance(t2) <= 50:
        new_y2 = current_y2 + screen_height
        t2.setx(random_x2)
        t2.sety(new_y2)
        life -= 1
    
      if life <= 0:
        break
    
      # move turtle
      t1.sety(new_y1)
    
      # handle second turtle
      t2.sety(new_y2)


     # set the key to move car
      def left():
        t3.setheading(180)
        t3.forward(20)

      def right():
        t3.setheading(0)
        t3.forward(20)
    
      s.onkey(left,'Left')
      s.onkey(right,'Right')
  
      s.listen()
  
      # render
      s.update()
  
    # game over
    t4.goto(-120,0)
    t4.write("GAME OVER", move=False, align='left', font=('Arial', 35, 'normal'))  

  s.onkeypress(func, 'space')
  s.listen()

main()