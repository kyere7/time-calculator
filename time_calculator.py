def add_time(start, duration, day =None):
    days_of_week_index = {
        "monday": 0,
        "tuesday":1,
        "wednesday":2,
        "thursday":3,
        "friday":4,
        "saturday":5,
        "sunday":6
    }
    days = ["Monday","Tuesday","Wednesday","Thursday", "Friday","Saturday","Sunday"]
    #fetching hours and mins from duration
    broken_duration = duration.partition(':')
    d_hours = int(broken_duration[0])
    d_minutes = int(broken_duration[2])
    #fetching hours and mins from start
    broken_start = start.partition(':')
    start_hrs = int(broken_start[0])
    get_start_min = broken_start[2].split(' ')
    start_mins = int(get_start_min[0])
    am_or_pm = get_start_min[1]
    am_pm_change = {"AM":"PM", "PM":"AM"}
    amt_of_days = int((d_hours/24))

    #getting the calculations
    calc_time_mins = d_minutes + start_mins
    if (calc_time_mins >= 60):
        start_hrs += 1
        calc_time_mins= calc_time_mins % 60
    amt_am_pm_change = int((start_hrs+d_hours)/12)
    calc_time_hrs = (start_hrs + d_hours) % 12

    calc_time_mins = calc_time_mins if calc_time_mins > 9 else "0" + str(calc_time_mins)
    calc_time_hrs = calc_time_hrs = 12 if calc_time_hrs ==0 else calc_time_hrs
    if (am_or_pm == "PM" and start_hrs + (d_hours % 12) >= 12):
        amt_of_days += 1
    am_or_pm = am_pm_change[am_or_pm] if amt_am_pm_change % 2 ==1 else am_or_pm
    time_returned = str(calc_time_hrs) + ':'+ str(calc_time_mins)+ " " + am_or_pm
    if (day):
        day = day.lower()
        index = int((days_of_week_index[day]) + amt_of_days) % 7
        current_day = days[index]
        if amt_of_days > 1:
            time_returned = time_returned+ ", " + current_day + " (" + str(amt_of_days) + " days later)"
        elif amt_of_days ==1:
            time_returned = time_returned + ", " + current_day + " " +"(next day)" 
        elif amt_of_days ==0:
            time_returned = time_returned + ", " + current_day
        # time_returned = time_returned+ ", " + current_day + " (" + str(amt_of_days) + " days later)" if amt_of_days > 1 else time_returned + ", " + current_day + " " +"(next day)" 
        # if amt_of_days == 0:
        #    return time_returned + ", " + current_day 

        return time_returned
    if not day:
        if amt_of_days== 1:
            return time_returned + " " +"(next day)"
        elif amt_of_days >1:
            return time_returned + " (" + str(amt_of_days) + " days later)"

        return time_returned

# print(add_time("11:06 PM", "2:02", "Friday"))
# print(add_time("11:06 PM", "300:22"))
# print(add_time("11:06 PM", "2000:12", "Tuesday"))

