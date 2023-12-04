import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S States Guess Game")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)



data=pandas.read_csv("50_states.csv")
state_list=data["state"].tolist()
guessed_states=[]
correct_states=0
while len(guessed_states)<52:
    answer_state = screen.textinput(title=f"{correct_states}/52 States Correct",
                                    prompt="What is the states name?")
    answer = answer_state.title()

    state_data=data[data.state==answer]
    if answer == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in state_list:
        guessed_states.append(answer)
        correct_states+=1
        state=turtle.Turtle()
        state.color("Black")
        state.penup()
        state.hideturtle()
        state.goto(int(state_data.x.iloc[0]),int(state_data.y.iloc[0]))
        state.write(answer,font=("Verdana",
                                        7, "normal"))


