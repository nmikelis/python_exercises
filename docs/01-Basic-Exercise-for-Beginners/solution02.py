print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

for i in range(0,10):
    x_sum = previous_num + i
    print("Current number ",i,"Previous number ", previous_num, "Sum", x_sum)
    previous_num = i