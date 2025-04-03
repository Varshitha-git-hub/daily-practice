def convert_to_seconds(minutes):
    seconds=minutes*60
    return seconds
minutes=int(input("enter minutes:"))
result=convert_to_seconds(minutes)
print(minutes,"minutes is equal to", result,"seconds")
