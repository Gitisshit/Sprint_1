task_string = '1h 45m,360s,25m,30m 120s,2h 60s'
task_list = task_string.replace(' ', ',').split(',')
minutes_sum = 0
for elem in task_list:
    if 'h' in elem:
        minutes_sum += int(elem[:-1]) * 60
    elif 's' in elem:
        minutes_sum += int(elem[:-1]) / 60
    else:
        minutes_sum += int(elem[:-1])
print(int(minutes_sum))
