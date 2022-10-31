
# Main function
def seconds_to_dhms(time):
    seconds_to_minute =60
    seconds_to_hour   =60 * seconds_to_minute
    seconds_to_day    =24 * seconds_to_hour

# Conversion of days from seconds
    days = time // seconds_to_day
    time %= seconds_to_day

# Conversion of hours from seconds
    hours = time // seconds_to_hour
    time %= seconds_to_day

# Conversion of minutes from seconds
    minutes = time // seconds_to_minute
    time %= seconds_to_minute

# Decleration of seconds & time
    seconds = time

# Output statement
    print('%d days, %d hours, %d minutes, %d seconds' % (days, hours, minutes, seconds))

# User input
time = int(input("Enter the number of seconds: "))
seconds_to_dhms(time)
