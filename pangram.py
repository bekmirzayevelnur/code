def check_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    for char in alphabet:
        if char not in sentence:
            return "pangram emas"
    return "pangram"

sentence = input()
result = check_pangram(sentence)
print(result)
