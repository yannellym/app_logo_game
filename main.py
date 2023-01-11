import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess That Logo Game")
image = "logo_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("placements.csv")
all_names = data.name.to_list()
#print(all_names)


guessed_logos = []

while len(guessed_logos) <18:
    answer_name = screen.textinput(title=f"{len(guessed_logos)}/17 guessed correctly", prompt="Type a logo name:").title()
    if answer_name == "Exit":
        missing_names = []
        for name in all_names:
            if name not in guessed_logos:
                missing_names.append(name)
        print(f"You missed the following the following logos{missing_names}")
    if answer_name in all_names:
        guessed_logos.append(answer_name)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        logo_data = data[data.name == answer_name] 
        t.goto(float(logo_data.x), float(logo_data.y))
        t.write(logo_data.name.item(), font=('Arial', 16, "normal"))
    




screen.exitonclick()
