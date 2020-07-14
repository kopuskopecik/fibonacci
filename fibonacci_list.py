# fibonacci list fromm 1 to 55
end_number = 55
counter = 1
fibonacci_list = [1]
index = 0

while counter <= end_number:
    fibonacci_list.append(counter)
    counter = counter + fibonacci_list[index]
    index = index + 1
    
print(fibonacci_list)