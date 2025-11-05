def weight_converter():
    # Get weight input from user
    weight = int(input("Weight: "))

    # Get unit selection (L for pounds, K for kilograms)
    unit = input("(L)bs or (K)g: ")

    # Convert based on selected unit
    if unit.upper() == "L":
        # Convert pounds to kilograms
        converted = weight * 0.453
        print(f"You are {converted} kg")
    else:
        # Convert kilograms to pounds  
        converted = weight * 2.2
        print(f"Your weight in lbs is {converted} lbs")


if __name__ == "__main__":
    weight_converter()
