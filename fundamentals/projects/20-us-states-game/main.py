from turtle import Screen, Turtle
import pandas as pd

# create a Screen object
screen = Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)

# create a turtle instance
turtle = Turtle()
turtle.shape(img)

# extract a DataFrame
data = pd.read_csv("50_states.csv")

# extract a list of states from the state Series(column) in the data DataFrame
us_states = data.state.to_list()

# setup an accumulator
total_num_of_states = us_states_total = len(us_states)
total_num_guessed_states = 0
guessed_states = []

while total_num_of_states >= 1:
    # prompt for user input
    answer_state = screen.textinput(title=f"({total_num_guessed_states}/{us_states_total}) State(s) Correct", prompt="Enter name of a state?").title()

    # break from the while if user types exit
    if answer_state == "Exit":
        break

    # check if the answer_state is in data
    # if true:
    # create a turtle to write name of a state at the x and y coordinates...

    if answer_state in us_states:
        # append answer_state to guessed_states
        guessed_states.append(answer_state)

        # extract row containing the answer_state
        state_row = data[data.state == answer_state]

        # extract the x and y coordinates from state row
        xcor = int(state_row["x"])
        ycor = int(state_row["y"])

        # creat a turtle...
        state_turtle = Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(xcor, ycor)
        state_turtle.pendown()
        state_turtle.write(f"{answer_state}")

        # increment the total number of guessed states
        total_num_guessed_states += 1

    # decrement total number of states
    total_num_of_states -= 1

# generate a csv file containing states that have not been guessed
states_to_learn = {
    "US State(s) To Learn": []
}
for state in us_states:
    if state not in guessed_states:
        states_to_learn["US State(s) To Learn"].append(state)

# generate csv file
states_data_frame = pd.DataFrame(states_to_learn)
states_data_frame.to_csv("states_to_learn.csv", index=False, header=True)

# keep screen open
screen.mainloop()
