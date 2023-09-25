string = "Hello, Python!"


def alphabet_frequency(s):
    vowels = "aeiouAEIOU"
    frequency = {}

    for alphabet in s:
        if alphabet.isalpha():
            if alphabet in frequency:
                frequency[alphabet] += 1
            else:
                frequency[alphabet] = 1

    vowel_frequency = {vowel: frequency[vowel] for vowel in frequency if vowel in vowels}
    return vowel_frequency


print(alphabet_frequency(string))
