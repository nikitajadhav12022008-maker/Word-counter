#Python based Word counter
#input text
text = input("enter text:")
#define words using split
words = len(text.split())
#defining char as length of text
chars = len(text)
#define logic for vowels
vowels = sum(1 for c in text.lower() if c in "aeiou")
#final step of printing everything
print("words:",words)
print("characters:",chars)
print("vowels:",vowels)

