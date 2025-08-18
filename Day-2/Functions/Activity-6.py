# Hey there cadet, we have some modules that are currently running using Farenheit, yuck.
# Let's convert them into the superiour unit, celsius. 
# Create a function called to_celsius(f) to convert farenheit to celsius.
# 
# Here is the formula to convert from farenheit to celsius:
# c = 5/9 * (f-32)








# Write your code above this line

def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees farenheit is", c, "degree celsius")

print("\n============= STARTING TESTS =============")
test(100)
test(88)
test(104)
print("============= ENDING TESTS =============\n")
