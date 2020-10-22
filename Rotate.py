def shift_n_letters(letter, n):
    new_val = ord(letter) + n
    if ord(letter) in range (97,123):
        if new_val > 122:
            return chr(new_val - 26)
        if new_val < 97:
            return chr(new_val + 26)
        else:
            return chr(new_val)
    else:
        return letter
        
def rotate(s, n):
    result = ""
    for letter in s:
        result = result + shift_n_letters(letter, n)
    return result
