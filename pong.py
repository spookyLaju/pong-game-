# first import turtle module 
import turtle
# creating the window ofthe pong game 
win =  turtle.Screen()
win.title('pong by spookylaju')
win.bgcolor('black')
win.setup(width=600, height=600)
#this win.tracers stops the window from updating itself
win.tracer(0)

#score
score_a = 0
score_b = 0 

#paddle A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('blue')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-250, 0)

#paddle B 
paddle_b = turtle.Turtle ()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('red')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(250, 0)

#Ball
ball =  turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = -0.2
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("player A :0  player B :0", align='center', font=("courier", 24, 'normal'))



#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_dowm():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)    
 

def paddle_b_up():
    x= paddle_b.ycor()
    x += 20
    paddle_b.sety(x)

# the x does not denote the coordinates 
def paddle_b_dowm():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)    

# keyboard binding 
win.listen()
win.onkeypress(paddle_a_up, 'w')    
win.onkeypress(paddle_a_dowm, 's')    
win.onkeypress(paddle_b_up, 'Up')    
win.onkeypress(paddle_b_dowm,'Down')  

#main game loop 
# win update , ensures everytime the loops run it update the screen 
while True:
    win.update()

    #movement for the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #border checking 
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy *= -1  

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *= -1  

    if ball.xcor()> 290:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("player A :{}  player B :{}".format(score_a, score_b), align='center', font=("courier", 24, 'normal'))

    if ball.xcor()< -290:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1 
        pen.clear()
        pen.write("player A :{}  player B :{}".format(score_a, score_b), align='center', font=("courier", 24, 'normal'))
   # paddle and ball colisions 
   # the logic here is ........(is there a more simple way to structure this logic)
    if (ball.xcor() > 240 and ball.xcor() <250) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(240)
        ball.dx *= -1 

    if (ball.xcor() < -240 and ball.xcor() >-250) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-240)
        ball.dx *= -1     
