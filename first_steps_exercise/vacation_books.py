count_pages = int(input())
pages_hour = int(input())
days = int(input())

total_reading = count_pages // pages_hour

total = total_reading // days

print(total)
