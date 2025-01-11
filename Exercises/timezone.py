def timezeone(tz_from, tz_to, start, duration):
    return start < tz_from - tz_to - duration

print('Received yesterday?', timezeone(12, -4, 3, 1))
