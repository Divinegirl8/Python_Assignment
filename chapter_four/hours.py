def seconds_since_midnight(hour, minutes, seconds):
    hour_in_seconds = (hour * 60) * 60
    minute_in_seconds = (minutes * 60) + seconds
    return hour_in_seconds + minute_in_seconds


