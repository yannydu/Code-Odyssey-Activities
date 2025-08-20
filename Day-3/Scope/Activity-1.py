# There's a problem with our code, we think the wrong variables are being called
# Fix the way the function is called on line 14.



def calculate_shield_strength(shield_modifier, ship_size):
    return shield_mods * ship_size


my_shield_mods = 5
my_ship_size = 10

## don't touch above this line


max_shield = calculate_shield_strength(shield_mods, ship_size)


# don't touch below this line

print(f"Maximum shield strength is: {max_shield}")

