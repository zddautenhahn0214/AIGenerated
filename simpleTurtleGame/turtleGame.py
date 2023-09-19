#this one didnt really work for a few reasons, but its a good start

# Import the turtle module
import turtle

def main():
  # Set up the screen
  wn = turtle.Screen()
  wn.bgcolor("lightgreen")
  wn.title("Turtle Game")

  # Create a turtle
  tess = turtle.Turtle()
  tess.shape("turtle")
  tess.color("blue")
  tess.penup()

  # Define a function for moving the turtle
  def move_turtle(key):
    if key == "Up":
      tess.forward(50)
    elif key == "Down":
      tess.backward(50)
    elif key == "Left":
      tess.left(45)
    elif key == "Right":
      tess.right(45)

  # Set up the main game loop
  #failed to initilize score variable
  score = 0
  while True:
    # Check for user input
    wn.onkeypress(move_turtle)

    # Check for obstacles
    if tess.xcor() > 300 or tess.xcor() < -300:
      tess.right(180)
    if tess.ycor() > 300 or tess.ycor() < -300:
      tess.right(180)

    # Increase the score
    score = score + 1
    tess.write("Score: " + str(score), False, align="left")

    # # End the game if the turtle hits an obstacle
    # if tess.distance(obstacle1) < 20 or tess.distance(obstacle2) < 20:
      # break

  # Display the final score
  print("Your final score was: " + str(score))

  # Close the screen
  wn.exitonclick()

# Call the main function
if __name__ == "__main__":
  main()
