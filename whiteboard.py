# def palindrome(word):
   
#     w2= list(word)
#     x= list(word)
#     x.reverse()
#     if w2==x:
#        return True
#     else:
#         return False
        
        
# print(palindrome(coding))



# def find_palindrome(word):
#     if word == word [::-1]:
#         return True
#     else:
#         return False
    
    
    


def two_pointer(word):
    i = 0
    j = len(word) - 1
    
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
        
    return True

print(two_pointer('racecar'))