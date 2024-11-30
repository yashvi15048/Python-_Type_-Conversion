#1.Convert an integer to a floating-point number.
integer_number = 5
floating_point_number = float(integer_number)
print(floating_point_number)  # Output: 5.0

#2.Convert a float to an integer.
floating_point_number = 5.87
integer_number = int(floating_point_number)

print(integer_number)  # Output: 5

#3.Convert an integer to a string.
integer_number = 42
string_number = str(integer_number)

print(string_number)       # Output: '42'
print(type(string_number)) # Output: <class 'str'>

#4.Convert a list to a tuple.
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)       # Output: (1, 2, 3, 4)
print(type(my_tuple)) # Output: <class 'tuple'>

#5.Convert a tuple to a list.
my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)

print(my_list)       # Output: [1, 2, 3, 4]
print(type(my_list)) # Output: <class 'list'>

#6.Convert a decimal number to binary.
decimal_number = 42
binary_number = bin(decimal_number)

print(binary_number)       # Output: '0b101010'
print(binary_number[2:])   # Output: '101010' (without the '0b' prefix)

#7.Convert a non-zero number to boolean
number = 42
boolean_value = bool(number)

print(boolean_value)       # Output: True
print(type(boolean_value)) # Output: <class 'bool'>



