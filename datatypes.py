favorite_cars = [
    {
        'make': 'Tesla',
        'model': 'Model S',
        'year': 2022, # Number (int)
        'price': 79999.99, # Float
        'features': ['Autopilot', 'Electric', 'All-Wheel Drive'], # List
        'is_electric': True, #Boolean
        'owner': None # None
    },
    {
        'make': 'Porsche',
        'model': '911 Carrera',
        'year': 2023, # Number (int)
        'price': 106500.00, #float
        'features': ['Sport Mode', 'Rear-Wheel Drive', 'Turbocharged'], # List
        'is_electric': False, #Boolean
        'owner': None # None
    }    
]

# if favorite_cars == []:
#     print("This list is empty")
#     print('Please add some items to the list\nThank you')
# elif favorite_cars[1]['make'] == 'Porsche':
#     print('The second iem is a Porsche')
#     print(favorite_cars[1]['make'] + ' ' + favorite_cars[1]['model'])
# else:
#     print('This list is not empty')
#     print(favorite_cars[1]['make'] + ' ' + favorite_cars[1]['model'])

# print(favorite_cars[0])
# print(favorite_cars[1]) # Each item requires a separate print statement

# for car in favorite_cars: # Basic for loop
#     print(car)
#     print("Next item:")

for car in favorite_cars:
    if car['make'] == 'Porsche':
        print("This car is a Porsche")
        print(car['make']+ ' ' + car['model'])
    else:
        print('This car is not a Porsche')
        print(car['make']+ ' ' + car['model'])

if any(car['make'] == 'Porsche' for car in favorite_cars): # Using any function
    print('Porsche found!')
else:
    print('There is no Porsche in this list')