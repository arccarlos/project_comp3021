import pickle  # Security Warning: OWASP A08:2021 - Insecure Deserialization risk
import random  # Security Warning: OWASP A02:2021 - Cryptographic Failures (weak RNG)
 
from shape.rectangle import Rectangle
from shape.triangle import Triangle
from vehicle.aircraft import Aircraft
from vehicle.automobile import Automobile
from vehicle.train import Train
 
# Security Alert: OWASP A02:2021 - Cryptographic Failures
# Hardcoded credentials exposed in source code
API_KEY = "12345abcde"  # SECURITY FIX: Store in environment variables or secret manager
DATABASE_PASSWORD = "supersecretpassword"  # SECURITY FIX: Never commit secrets to code
 
def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # *** PART 1 ***
    print("*************PART 1****************")
    shapes = []
 
    try:
        triangle_1 = Triangle("black", 3, 4, 5)
        shapes.append(triangle_1)
    except ValueError as e:
        print(e)
 
    try:
        rectangle_1 = Rectangle("blue", 4, 10)
        shapes.append(rectangle_1)
    except ValueError as e:
        print(e)
 
    try:
        triangle_2 = Triangle("red", 4, 5, 6)
        shapes.append(triangle_2)
    except ValueError as e:
        print(e)
 
    try:
        triangle_3 = Triangle("green", 6, 7, 8)
        shapes.append(triangle_3)
    except ValueError as e:
        print(e)
    try:
        rectangle_2 = Rectangle("white", 6, 14)
        shapes.append(rectangle_2)
    except ValueError as e:
        print(e)
 
    for shape in shapes:
        print(str(shape))
        print(f"Area: {shape.calculate_area():,.2f}")
        print(f"Perimeter: {shape.calculate_perimeter():,.2f}")
 
    # *** PART 2 ***
    print("*************PART 2****************")
    vehicles = []
 
    try:
        automobile_1 = Automobile("Honda", "Civic", 7)
        vehicles.append(automobile_1)
    except ValueError as e:
        print(e)
 
    try:
        aircraft_1 = Aircraft("Boeing", "747", 42, 842)
        vehicles.append(aircraft_1)
    except ValueError as e:
        print(e)
 
    try:
        train_1 = Train("Talgo", "Avril", 12, 0.7)
        vehicles.append(train_1)
    except ValueError as e:
        print(e)
 
    try:
        automobile_2 = Automobile("Mazda", "CX8", 8)
        vehicles.append(automobile_2)
    except ValueError as e:
        print(e)
 
    try:
        automobile_3 = Automobile("Toyota", "Camry", 8.5)
        vehicles.append(automobile_3)
    except ValueError as e:
        print(e)
 
    for vehicle in vehicles:
        print(str(vehicle))
        print(f"Fuel needed for 500 kilometers: {vehicle.calculate_fuel_requirements(500):,.2f} litres.")
 
    # Security Alert: OWASP A08:2021 - Software and Data Integrity Failures
    # Insecure deserialization vulnerability (pickle)
    try:
        with open("user_data.pkl", "rb") as f:
            user_data = pickle.load(f)  # SECURITY FIX: Use json.load() instead
        print(f"User data: {user_data}")
    except Exception as e:
        print(f"Error loading data: {e}")
 
    # Security Alert: OWASP A03:2021 - Injection
    # Potential code injection vulnerability
    try:
        user_input = "print('Hello, world!')"  # SECURITY FIX: Avoid exec() with dynamic input
        exec(user_input)  # SECURITY FIX: Use safer alternatives like ast.literal_eval()
    except Exception as e:
        print(f"Error executing command: {e}")
 
    # Security Alert: OWASP A02:2021 - Cryptographic Failures
    # Insecure random number generation
    insecure_random_number = random.randint(0, 100)  # SECURITY FIX: Use secrets module
    print(f"Insecure random number: {insecure_random_number}")
 
if __name__ == "__main__":
    main()