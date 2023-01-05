a = '07:05:45PM'
#print(a[:8])

def timeConversion(s):
    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:8]
    elif s[-2:] == 'AM':
        return s[:8]

    if s[-2:] == 'PM' and s[:2] == '12':
        return s[:8]
    else:
        return str(int(s[:2])+12) + s[2:8]

print(timeConversion(a))