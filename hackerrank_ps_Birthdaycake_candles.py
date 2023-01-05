def birthdayCakeCandles(candles):
    # Write your code here
    highest_candles = 0
    max_v = max(candles)
    for i in range(len(candles)):
        if candles[i] == max_v:
            highest_candles += 1
    return highest_candles

a = '07:05:45PM'
print(a[-1:-3])