# Hey cadet, let's fix how the ship's shields get calculated by declaring a global variable
# Set the variable ship_size to 4




# DO NOT TOUCH BELOW THIS LINE

def calculate_shields(mods):
    return ship_size * mods

def calculate_speed(engine_bonus, mods):
    return engine_bonus * mods - ship_size

print(f"Ship has {calculate_shields(4)} max shields.")
print(f"Ship has {calculate_speed(3, 4)} max speed.")
