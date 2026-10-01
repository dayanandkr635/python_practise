units =float(input(" Enter electricity units consumed: "))

if units <=100:
    print("Low consumption")

elif units <=200:
    print("Moderate consumption")
    
elif units <=400:
    print("High consumption")
    
else:
    print("Very high consumption")