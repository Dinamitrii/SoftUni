from math import floor

width = float(input())
long = float(input())
height = float(input())
astronaut_height = float(input())

needed_space = 2 * 2 * (astronaut_height + 0.40)
actual_space = width * long * height

astronaut_count = actual_space / needed_space

if 3 <= astronaut_count <= 10:
    print(f"The spacecraft holds {floor(astronaut_count)} astronauts.")
elif astronaut_count < 3:
    print("The spacecraft is too small.")
elif astronaut_count > 10:
    print("The spacecraft is too big.")
