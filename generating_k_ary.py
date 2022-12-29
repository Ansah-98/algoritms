'''
generate all the strings  of length n drawn from  0...k - 1
'''

def range_to_list(k):
    result = []
    for i in range(k):
        result.append(str(i))
    return result

def base_k_strings(n,k):
    if n == 0:
        return []
    if n ==1 :
        return range_to_list(k)
    return (digit + bitstring for digit in base_k_strings(1,k) for bitstring in base_k_strings(n-1,k))

print(list(base_k_strings(3 , 5)))