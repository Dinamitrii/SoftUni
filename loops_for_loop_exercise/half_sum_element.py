import sys

n = int(input())

total_sum = 0

max_num = - sys.maxsize

for i in range(1, n + 1):
    currentNum = int(input())

    total_sum = total_sum + currentNum

    if currentNum > max_num:
        max_num = currentNum

sum = total_sum - max_num
if sum == max_num:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    diff = abs(sum - max_num)
    print(f"Diff = {diff}")
