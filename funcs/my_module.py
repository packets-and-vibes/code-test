def cube_number(input_number: int) -> int:
    cubed = input_number ** 3
    return cubed

# my_start_number = 4
# my_cubed_number = (cube_number(my_start_number))
# print(f'The cube of {my_start_number} is {my_cubed_number}.')

def greet_person(name: str) -> str:
    return f'Hello, {name}.'

print(greet_person('Kenny'))