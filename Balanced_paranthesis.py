'''Check if a list of paranthesis are balanced or not - works for both perfect/symmetric ('{([])}') and mixed '([{])}' sequence'''
'''Logic: balance the sequence with sum of bracket's complementary scores'''

def isbalanced(string):
    
    dict_brack = {'{':1, '(':2, '[':4, '}':-1, ')':-2,']':-4}
    sums = 0

    # An empty string is technically balanced
    if not string:
        return True
    
    for s in string:
        if s in dict_brack:
            sums += dict_brack[s]
            
    if not sums:
        return True
    
#     print(sums)
    return False

print(isbalanced('([{])}')) # True
print(isbalanced('{([])}')) # True
print(isbalanced('{([{])}')) # False 
