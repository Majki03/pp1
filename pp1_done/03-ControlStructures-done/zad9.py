how_many = int(input("Enter how many exercises are in the test: "))
count = 0

for ex in range(1, how_many + 1):
    exe = input("Was the task complited correctly? (Ture/False): ")
    if(exe == "True"):
        count += 1
    else:
        count = count

if(count >= 2):
    print("Test passed")