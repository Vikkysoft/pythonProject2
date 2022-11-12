# var_string = "radar"

# reversed_string = reversed(var_string)

# if list(reversed_string) == list(var_string):
# print("The string is a palindrome.")
# else:
# print("The string is not a palindrome.")


def is_palindrome(str):
    rev = ''.join(reversed(str))

    if str == rev:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")


str1 = "radar"
is_palindrome(str1)

str2 = "aibhopohbia"
is_palindrome(str2)

str3 = "testify"
is_palindrome(str3)

