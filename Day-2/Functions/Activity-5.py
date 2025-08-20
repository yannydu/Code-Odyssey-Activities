# Hello cadet,
# A lot our instruments require more precise time units than hours
# Let's create a function called hours_to_seconds(hours).
# Define the function below:






#==== DO NOT TOUCH BELOW THIS LINE ====#


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")

print("==== STARTING TESTS ====")
test(10)
test(1)
test(25)
test(100)
print("==== ENDING TESTS ====")
