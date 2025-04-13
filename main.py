# Import the necessary class from procyclingstats
from procyclingstats import Rider
import json

# Create an instance for a specific rider
rider = Rider("rider/tadej-pogacar")

# Get and print the rider's birthdate
print("Rider Birthdate:", rider.birthdate())

# Alternatively, you can parse all available data
rider_data = rider.parse()
print(json.dumps(rider_data, indent=4))

# print("Rider Data:", rider_data)
