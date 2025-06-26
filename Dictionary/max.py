dictionary = {'a': 3, 'b': 2, 'c': 1}
dictionary_keys = dictionary.keys()
dictionary_values = dictionary.values()

print(max(dictionary, key=dictionary.get))