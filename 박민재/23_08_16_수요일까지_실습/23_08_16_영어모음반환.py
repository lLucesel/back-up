string = "Hello, Python!"
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for alphabet in s:
        if alphabet in vowels:
            count +=1
            return count

print(count_vowels(string))