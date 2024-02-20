from collections import deque 

def check_polindrome(word):
    word = word.replace(' ', '')
    
    symbols = deque(word)
    
    while len(symbols) > 1:
        if symbols.popleft() != symbols.pop():
            return False
    return True


a = 'oko'

b = 'paap'

c = 'Am I sas s ma'


c_p = check_polindrome(c)
a_p = check_polindrome(a)
b_p = check_polindrome(b)
print(a_p)
print(b_p)
print(c_p)