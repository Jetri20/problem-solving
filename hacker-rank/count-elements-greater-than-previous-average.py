def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) <= 1:
        return 0
    
    current = responseTimes[0]
    count = 0
    for i in range(1, len(responseTimes)):
        avg = current / i
        if responseTimes[i] > avg:
            count += 1
        current += responseTimes[i]
            
    return count