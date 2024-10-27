def forecast(temp):
    avg = sum(temp)/len(temp)
    m = min(temp)
    mx = max(temp)
    print(f"Average temp : {avg}, Min temp: {m}, Max temp: {mx}")



temperature_readings = [25, 28, 21, 24, 27]
forecast(temperature_readings)