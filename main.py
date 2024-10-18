import pandas
import turtle


tim = turtle.Turtle()
screen = turtle.Screen()
screen.title("Bharat States Game")
image = "map-of-india.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("list-of-states.csv")
all_states = data.States.to_list()
guessed_states = []

while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        states_not_guessed = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         states_not_guessed.append(state)
        new_data = pandas.DataFrame(states_not_guessed)
        new_data.to_csv("states_to_learn.csv")
        break
    # If answer is matched with the user input.
    if answer_state in all_states:
        guessed_states.append(answer_state)
        tim.hideturtle()
        tim.penup()
        state_data = data[data.States == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(state_data.States.item())


screen.exitonclick()
