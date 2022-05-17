days_rest = int(input())

maximum_playtime_minutes_per_year = 30000

work_days = 365 - days_rest

playtime_when_work_minutes = 63
playtime_when_rest_minutes = 127

total_playtime_minutes = (work_days * playtime_when_work_minutes) + (days_rest * playtime_when_rest_minutes)

difference_minutes = abs(maximum_playtime_minutes_per_year - total_playtime_minutes)

difference_total_hours = difference_minutes // 60
difference_total_minutes = difference_minutes % 60

if total_playtime_minutes <= maximum_playtime_minutes_per_year:
    print('Tom sleeps well')
    print(f'{difference_total_hours} hours and {difference_total_minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{difference_total_hours} hours and {difference_total_minutes} minutes more for play')
