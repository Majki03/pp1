def f(detector):
    count = 0
    max_count = 0
    
    for i in detector:
        if(i == "+"):
            count += 1
            max_count = max(max_count, count)
        elif(i == "-"):
            count -= 1
    
    return max_count >= 3
    
result1 = f("+-+++-+---")
result2 = f("+-+-+-+-")
result3 = f("+-++-+--")
result4 = f("+-++-++-+---")

print(result1)
print(result2)
print(result3)
print(result4)