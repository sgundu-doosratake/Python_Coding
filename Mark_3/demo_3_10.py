# Print not divisible by 5 and 3
i = 1

for i in range(100):
    if (i%5==0 or i%3==0):
        continue

    print(i)

    i+=1

print("Loop Completed")
