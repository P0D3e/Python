str_input = input("Insert a word that you want to check the vowels and the consonants in: ")

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vowelcount = 0
consonantcount = 0

str_input = str_input.lower()

for i in range(0, len(str_input)):
    if str_input[i] in ('a', 'e', 'i', 'o', 'u'):
        vowelcount += 1
    elif 'a' <= str_input[i] <= 'z':
        consonantcount += 1

print("Total number of consonants and vowels:")
print("Vowels:", vowelcount)
print("Consonants:", consonantcount)