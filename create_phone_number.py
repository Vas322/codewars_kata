"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def create_phone_number(n):
    slice1, slice2, slice3 = n[:3], n[3:6], n[6:]
    str1 = ''.join(str(i) for i in slice1)
    str2 = ''.join(str(i) for i in slice2)
    str3 = ''.join(str(i) for i in slice3)
    return f'({str1}) {str2}-{str3}'


print(create_phone_number(list))
