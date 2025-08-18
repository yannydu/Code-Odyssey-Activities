# ========================================================================================================= #
# Greetings cadet, good job making it to the 2nd day of training.                                           #
# We have a function to calculate how many energy crystals to bring on a trip                               #
# Let's fix the bug on line __ by calling the calculate energy crystals function for the trip to Gamma 9    #
# ========================================================================================================= #

def calculate_crystals(distance):
  crystals_per_light_year = 100
  
  total_crystals = crystals_per_light_year * distance
  return total_crystals

distance_to_alpha_centauri = 12
distance_to_gamma_9 = 15

# 

crystals_for_alpha = calculate_crystals(distance_to_alpha_centauri)
crystals_for_gamma = 0

#
print("\n=============================")
print("Alpha Centauri is", distance_to_alpha_centauri, "light years away.")
print("Gamma 9 is", distance_to_gamma_9, "light years away.")

print("Energy crystals needed for Alpha Centauri:", crystals_for_alpha)
print("Energy crystals needed for Gamme 9:", crystals_for_gamma)
print("=============================")
