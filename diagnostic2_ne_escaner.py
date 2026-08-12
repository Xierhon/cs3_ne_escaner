def calculate_fuel(cargo_weight):
    base_ship_weight = 50000 
    total_weight = base_ship_weight + cargo_weight
    needed_fuel = total_weight * 3
    return needed_fuel


while True:
    cargo = input("enter cargo(satellite, rover, supplies, or launch): ").lower()
    if cargo == "launch":
        break
    elif cargo == "satellite":
        total_cargo_weight = 1000
    elif cargo == "rover":
        total_cargo_weight = 2500
    elif cargo == "supplies":
        total_cargo_weight = 500
    else:
        print("Cargo is invalid.")

    if total_cargo_weight > 10000:
        print("MAX WEIGHT REACHED.")
        break


fuel_needed = calculate_fuel(total_cargo_weight)
print("total_cargo_weight:", total_cargo_weight, "kg")
print("fuel needed:", fuel_needed, "liters")