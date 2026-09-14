import math

def calculate_unit_price(diameter_cm, price_eur):
    # Convert diameter from cm to radius in meters
    radius_m = (diameter_cm / 100) / 2
    # Area = pi * r^2
    area_sq_m = math.pi * (radius_m ** 2)
    # Price per square meter
    return price_eur / area_sq_m

# Main program
d1 = float(input("Enter diameter of first pizza (cm): "))
p1 = float(input("Enter price of first pizza (€): "))

d2 = float(input("Enter diameter of second pizza (cm): "))
p2 = float(input("Enter price of second pizza (€): "))

unit_price1 = calculate_unit_price(d1, p1)
unit_price2 = calculate_unit_price(d2, p2)

print(f"\nPizza 1 unit price: {unit_price1:.2f} €/m²")
print(f"Pizza 2 unit price: {unit_price2:.2f} €/m²")

if unit_price1 < unit_price2:
    print("The first pizza gives better value for money.")
elif unit_price2 < unit_price1:
    print("The second pizza gives better value for money.")
else:
    print("Both pizzas offer the exact same value for money.")