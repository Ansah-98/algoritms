"""
writing all the bits provided by n using backtracking

"""

def append_beginning_fon(x,L):
    return [x + element for element in L]

def bit_strings(n):
    if n == 0:
        return
    if n ==1 :
        return [ "0", "1"]
    else:
        return (append_beginning_fon('0', bit_strings( n-1 )) + append_beginning_fon('1' , bit_strings (n-1) )) 


print(bit_strings(6))
