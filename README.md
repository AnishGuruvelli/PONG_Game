# PONG_Game
Python Project


Steps:

*** Steps to be followed while making the pong game ***

1. create the screen
2. create and move the paddle
3. create another paddle
4. create the ball and make it move
5. detect collision with the wall and bounce back
6. detect collision with paddle
(this is the hardest part of the program cuz we can write a code that if its within 20px between the paddle and ball
then it collided but the problem arises when the ball doesnt hit exactly at the centre, but hits at one of its corners
then the dist is around 50px so code gets wrong)
7. detect when paddle misses
8. keep score

screen = [width=800, height=600]

paddle = [height = 100, width = 100, x_pos = 350, y_pos = 0]
each key press should move the paddle by 20px up and down

ball = [width = 20, height = 20, x_pos = 0, y_pos = 0]]
