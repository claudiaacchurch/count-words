# One
# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

# name the function
def reading_time(input):
    if type(input) == str:
        stringlist = input.split()
        num = len(stringlist)
    else:
        num = input
    
    seconds = round(num/200*60)
    minutes = round(seconds/60)
    hours = round(seconds/3600)
    print (hours)
    print (seconds)
    seconds_formatted = seconds%60
    minutes_formatted = minutes%60
    if num == 0:
        return 0
    elif num >= 0:
        if minutes > 59:
            return f'{hours} hours, {minutes_formatted} minutes, {seconds_formatted} seconds'
        elif seconds > 60:
            return f'{minutes} minutes, {seconds_formatted} seconds'
        else:
            return f'{seconds} seconds'
# parameters:
#  number of words .. 200
#  text


# returns:
# time (float? date time? x number of hours, minutes, seconds, datetime)


# side effects:
# none

    pass
