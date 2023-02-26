import re
# 1
strng = input("Enter a text:")
pattern = r"Rb{1,}r"
match = re.search(pattern,strng)
if match:
    print(match.group())
else:
    print(None)
print()

# 2
def check_number_card(number):
    pattern = r"\d{4}-\d{4}-\d{4}-\d{4}"
    match_2 = re.fullmatch(pattern,number)
    if match_2:
        return "Authorization done"
    else:
        raise ValueError("Not correct number of card")

# 3
def check_string(strng):
    pattern = r"^[a-zA-Z0-9]+[a-zA-Z]+[0-9_]+[a-zA-Z0-9_]*"
    match = re.fullmatch(pattern,strng)
    if match:
        return "Correct e-mail"
    else:
        raise ValueError("Not correct e-mail")

# 4
def check_login(strng):
    pattern = r"[a-zA-Z0-9]{2,10}"
    match = re.fullmatch(pattern, strng)
    if match:
        return "Correct login"
    else:
        raise ValueError("Not correct login")

