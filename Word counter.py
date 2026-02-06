text = input("enter text:")
words = len(text.split())
chars = len(text)
vowels = sum(1 for c in text.lower() if c in "aeiou")

print("words:",words)
print("characters:",chars)
print("vowels:",vowels)