import turtle
def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)
        t.right(120)
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)
def draw_snowflake(level):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, 300, level)
        t.right(120)

    turtle.done()

if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії (0 або більше): "))
        if level < 0:
            raise ValueError
        draw_snowflake(level)
    except ValueError:
        print("Будь ласка, введіть ціле число, що більше або дорівнює нулю.")
