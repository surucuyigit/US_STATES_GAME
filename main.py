import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

on_map = turtle.Turtle()
on_map.penup()
on_map.hideturtle()

data = pandas.read_csv("50_states.csv")
state_name = data.state.to_list()


correct_ones = []
score = 0
score_turtle = turtle.Turtle()
score_turtle.penup()
score_turtle.hideturtle()

while score < len(state_name):
    guess = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

    if guess == "Exit":
        missing_states = [state for state in state_name if state not in correct_ones]
        # missing_states = []
        # for state in state_name:
        #     if state not in correct_ones:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


    if guess in state_name and guess not in correct_ones:
        score += 1
        score_turtle.clear()
        score_turtle.goto(-100, 200)
        score_turtle.write(f"{score}/{len(state_name)}", font=("Arial", 25, "normal"))
        correct_ones.append(guess)
        # pos = state_name.index(guess)
        # x_pos = data.x[pos]
        # y_pos = data.y[pos]
        row_data = data[data.state == guess]
        on_map.goto(int(row_data.x), int(row_data.y))
        on_map.write(guess)
