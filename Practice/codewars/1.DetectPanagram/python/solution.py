import string


def format(s):
    res = ""
    for ch in s.lower().replace(" ", ""):
        if ch not in res:
            res = res + ch
    return res


def is_pangram(s):
    alphabet = list(string.ascii_lowercase)
    counter = 0

    for l in format(s):
        if l in alphabet:
            counter += 1

    if counter >= len(alphabet):
        return True
    else:
        return False

# pangram = "Aacdefghijklmnopqrstuvwxyz is not a pangram."
# Tricky Case: Repeated Chars, Whitespaces, Uppercase, More than alphabet
# test.assert_equals(is_pangram(pangram), False)
