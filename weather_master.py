temp = []
cold = []
total_temp = 0
day = 0
out = -100  # user can change this constant

print('Weather Master 4.0!')
intemp = int(input('Next Temperature (or -100 to quit): '))

if intemp == out:
    print('No temperatures were entered.')
    quit()
else:
    while intemp != out:
        temp.append(intemp)
        total_temp += intemp
        day += 1
        intemp = int(input('Next Temperature (or -100 to quit): '))

    for i in temp:
        if i < 16:
            cold.append(i)

    avg = total_temp / day
    high = max(temp)
    low = min(temp)
    print('Highest temperature: %d' % high)
    print('Lowest temperature: %d' % low)
    print('Average temperatue: %f' % avg)
    print('%d cold day(s)' % len(cold))
