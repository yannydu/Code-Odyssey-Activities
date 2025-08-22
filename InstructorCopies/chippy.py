def main():
    print("Hello I am Chippie!")
    name = input("What is your name? ")
    print(f"Hello {name}! Nice to meet you")
    print("We will be blasting off today, but our ship isnt prepped.")
    print("First we need to figure out how many people are coming.")
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
    print("Now we need to know how long we are going for to decide fuel and food reserves.")
    days = int(input("How many days are you going? "))
    # Fuel needs 100L per day gone
    litres_needed = 100
    fuel = days * litres_needed
    # Crew needs 3 bars per person per day
    bars_needed = 3
    food = bars_needed * crew_size * days
    print(f"We need to bring {fuel}L of fuel and {food} nutriyum bars.")
main()