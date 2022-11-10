
var_string = "radar"

reversed_string = reversed(var_string)

if list(reversed_string) == list(var_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")