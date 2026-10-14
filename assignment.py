def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: It will be 3 and 4, the for loop always goes to the first check and it said if the number is greater than 1 then only print it adding +1 to it so it checked in our list of 1, 2, 3 where the number is greater than 1 which is 2 and it added 1 to 2 and gave 3 as first output and then same for 3 +1, 4
# so only number greater than 1 passed on to add_one 

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: It will return 3, because return sends a value back to whoever called the function. add_one returns value + 1, and the loop then passes that returned value to print, which is what makes it appear in the output. And then if we run add_one(2) on its own line without print, the function would still compute 3, but nothing would be displayed.
