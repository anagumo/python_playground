import common_functions

"""
to_romans(int)
ej. 1939 -> MCMXXXIX

Instructions:
1. Convert the number into a list where each element is a digit 
of the number: number_to_list(int)
2. Convert the number list into a new one where each element is raised 
to base 10 according to its position: to_base_10(list[int])
3. Compress the number list into a string where each element is a Roman numeral
"""

romans = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC',
    100: 'C',
    200: 'CC',
    300: 'CCC',
    4000: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM',
    1000: 'M'
}

def to_number_list(number:int) -> list[int]:
    """
    A pure converter function that takes a number as input and returns a 
    new list where each element is a digit of the number.
    Corner cases:
    - If the input is an empty string, the function should return an empty list
    - If the input is a string number, the function should valid it as int first
    - If the input is an invalid string, the function should return an empty list
    """
    descomposition = []

    if common_functions.is_integer(number):
        for digit in str(number):
            descomposition.append(int(digit))

    return descomposition

def to_base_10(numbers: list[int]) -> list[int]:
    """
    A pure converter function that takes a list as input and returns a new
    list where each number is converted to base 10 according to its position.
    Corner cases:
    - If the input is an empty list, the function should return an empty list
    """
    list_to_base_10 = []
    index = 0
    index_base_10 = len(numbers) - 1

    while index < len(numbers):
        list_to_base_10.append(numbers[index] * 10**index_base_10)
        index = index + 1
        index_base_10 = index_base_10 - 1

    return list_to_base_10

def to_roman(numbers_base_10: list[int]) -> str:
    """
    A pure compressor function that takes a list of numbers and returs 
    a string. Each element in the list is converted to a roman numeral 
    and its concatenated into the string.
    Corner cases:
    - If the input is an empty list, the function should return an empty list
    """
    roman_string = ""

    for number in numbers_base_10:
        roman_string = roman_string + romans[number]

    return roman_string

print(to_roman(to_base_10(to_number_list(1939))))