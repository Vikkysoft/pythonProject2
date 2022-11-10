# var_string = "radar"

# reversed_string = reversed(var_string)

# if list(reversed_string) == list(var_string):
# print("The string is a palindrome.")
# else:
# print("The string is not a palindrome.")


def is_palindrome(str1):
    rev = ''.join(reversed(str1))

    if str1 == rev:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")


str1 = "radar"
is_palindrome(str1)

