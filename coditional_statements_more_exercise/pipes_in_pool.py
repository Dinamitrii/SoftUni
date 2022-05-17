volume = int(input())
first_pipe = int(input())
second_pipe = int(input())
hours_off = float(input())

liters_full = abs((first_pipe + second_pipe) * hours_off)

first_pipe_percentage = (first_pipe / (first_pipe + second_pipe)) * 100
second_pipe_percentage = (second_pipe / (first_pipe + second_pipe)) * 100
total_volume_percentage = liters_full / volume * 100

if liters_full <= volume:
    print(f'The pool is {total_volume_percentage:.2f}% full. Pipe 1: {first_pipe_percentage:.2f}%. Pipe 2: {second_pipe_percentage:.2f}%.')
else:
    print(f'For {hours_off:.2f} hours the pool overflows with {abs(volume - liters_full):.2f} liters.')
