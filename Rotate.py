# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

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
        

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
