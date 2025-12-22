def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) <= 1:
        return 0
    
    avg = responseTimes[0]
    count = 0
    for i in range(1, len(responseTimes)):
        if responseTimes[i] > avg:
            count += 1
            avg += responseTimes[i] / i
            
    return count