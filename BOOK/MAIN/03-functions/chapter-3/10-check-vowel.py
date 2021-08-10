#A function that takes character and returns True in case of vowel else False
#Check 'u','k','m','i'.

def checkVowel(character):
    if character in ('a','e','i','o','u'):
        return True
    else:
        return False

print(checkVowel('u'))
print(checkVowel('k'))
print(checkVowel('m'))
print(checkVowel('i'))
