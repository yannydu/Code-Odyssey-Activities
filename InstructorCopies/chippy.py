def main():
    print("Hello I am Chippie!")
    name = input("What is your name? ")
    print(f"Hello {name}! Nice to meet you")
    print("We will be blasting off today, but our ship isnt prepped.")
    print("First we need to figure out how many people are coming.")

    # Crew 
    crew_size = int(input("How many people do you want on the ship? "))
    print("Please list names of the crew:")
    crew = [name]
    for i in range(crew_size):   
        name = input("Name: ")
        crew.append(name)
    print("Your crew: ", end=" ")
    for c_name in crew: 
        if c_name == crew[-1]: 
            print(f"{c_name}")
        else:
            print(f"{c_name}, ", end=" ")

    
    # Propulsion
    print("Now that we have the fuel, we need to know the distance for the trip")
    print("Please list all the planets you want to travel to and the distances")
    planet_amounts = int(input("How many planets are we visiting? "))
    old_planet = "Earth"
    planets = ["Earth"]
    distances = []
    for i in range(planet_amounts):
        planet = input("Planet Name: ")
        distance = int(input(f"Distance (in kilometers) to travel from {old_planet} to {planet}: "))
        old_planet = planet
        planets.append(planet)
        distances.append(distance)
    print(f"We will be travelling to ", end=" ")
    for p in planets:
        if p == planets[-1]: 
            print(f"{p}")
        else:
            print(f"{p}, ", end=" ")
    total_distance = 0
    for dis_size in distances:
        total_distance += dis_size
    print(f"We will be travelling {total_distance}km.")
    
    # Food
    print("Now we need to know how long we are going to get our food reserves.")
    days = int(input("How many days are you going? "))
    # Crew needs 3 bars per person per day
    bars_needed = 3
    food = bars_needed * crew_size * days
    print(f"We need to bring {food} nutriyum bars.")


main()