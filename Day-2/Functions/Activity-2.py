# ================================================================================================= #
# Hello Cadet, let's use what we learned about functions and pass in more values to the function.   #
# Let's create a function that calculates the number of nutriyum bars we need to bring on our trip. #
# ================================================================================================= #

def calculate_nutriyums(crew_size, mission_days):
    # Each crew member gets 3 nutriyum bars a day
    nutriyums_per_day = 3 

    nutriyums = 0
    return nutriyums


#======== DO NOT ACCESS CODE BELOW ==============#
crewA, missionA = 55, 27
nutriyumsA = calculate_nutriyums(crewA, missionA)

crewB, missionB = 103, 53
nutriyumsB = calculate_nutriyums(crewB, missionB)

print("\n========================")
print("Crew A size:", crewA)
print("Mission A days:", missionA)
print("Calculating number of nutriyums to bring for mission A:", nutriyumsA)
print("\n")
print("Crew B size:", crewB)
print("Mission B days:", missionB)
print("Calculating number of nutriyums to bring for mission B:", nutriyumsB)
print("========================\n")
