def find_vowel(s):
    l=['a','e','i','o','u']
    for i in s:
            if i in l:
                print('True')
            else:
                print('False')
s='Alex is Great'
find_vowel(s)
