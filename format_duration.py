def format_duration(seconds):
    """
    Calculate the Year, Day, Hour, Minute and Second values
    for given second parameter. Format the values in given format:
    '1 year, 1 day, 2 hours, 3 minutes and 1 second'
    
    Examples:
    >>>format_duration(1)
    1 second
    >>>format_duration(62)
    1 minute and 2 seconds
    >>>format_duration(3662)
    1 hour, 1 minute and 2 seconds
    """
    
    # Rules:
    # if seconds == 0 then return 'now'
    # 1 minute but 2 minute's'
    # year, day, hour, minute 'and' second
    
    # Calculations:
    # 1 year is 365 * 24 * 60 * 60 = 31536000 s
    # 1 day is 24 * 60 * 60 = 86400 s
    # 1 hour is 60 * 60 = 3600 s
    # 1 minute is 60 s
    # 1 second is 1 s
    
    if seconds == 0:
        return 'now'
    
    # Years, Days, Hours, Minutes and Seconds Calculations.
    rem = None
    years = seconds // (365 * 24 * 60 * 60)
    rem = seconds % (365 * 24 * 60 * 60)
    days = rem // (24 * 60 * 60)
    rem %= (24 * 60 * 60)
    hours = rem // (60 * 60)
    rem %= (60 * 60)
    minutes = rem // 60
    rem %= 60
    seconds = rem
    
    # According to their plural situations append result to the result list.
    result = []
    if years != 0:
        if years == 1:
            result.append('1 year')
        else:
            result.append(f'{years} years')
    if days != 0:
        if days == 1:
            result.append('1 day')
        else:
            result.append(f'{days} days')
    if hours != 0:
        if hours == 1:
            result.append('1 hour')
        else:
            result.append(f'{hours} hours')
    if minutes != 0:
        if minutes == 1:
            result.append('1 minute')
        else:
            result.append(f'{minutes} minutes')
    if seconds != 0:
        if seconds == 1:
            result.append('1 second')
        else:
            result.append(f'{seconds} seconds')
    
    # According to length of result list, return the result in correct format.
    if len(result) == 1:
        return result[0]
    elif len(result) == 2:
        return f'{result[0]} and {result[1]}'
    else:
        last_item = result.pop()
        return ', '.join(result) + f' and {last_item}'
