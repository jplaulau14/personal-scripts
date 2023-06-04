def find_long(array_string):
    return max([len(string) for string in array_string.split()])

print(find_long('Mathematics requires a small dose, not of genius, but of imaginative freedom which, in a larger dose, would be insanity'))

print((lambda x, y, z: x**y + z)(3, 2, 1))

basket = ['apples', 'oranges', 'mangoes']
basket[2] = 'grapes'

print(basket)

def find_num(arr):
    even = [n for n in arr if n % 2 == 0]
    odd = [n for n in arr if n % 2 != 0]
    return even[0] if len(even) == 1 else odd[0]

print(find_num([1, 3, 5, 7, 8]))

def mystery_function1 (word):
    vowels = ['a', 'e', 'i', 'o', 'u'] 
    while word[0] not in vowels: 
        word = word[1:] + word[0] 
    return word + 'ay'
def mystery_function2 (phrase):
    words = phrase.split()
    new_phrase = [mystery_function1 (word) for word in words]
    return ' '.join(new_phrase)
print(mystery_function2('strawberry cheesecake'))