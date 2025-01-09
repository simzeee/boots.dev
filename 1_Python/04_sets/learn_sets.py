def remove_duplicates(spells):
    spells = set(spells)
    return list(spells)


fruits = {"apple", "banana", "grape"}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}

fruits.add("pear")
print(fruits)

fruits = set()
fruits.add("pear")
print(fruits)
# Prints: {'pear'}

fruits = {"apple", "banana", "grape"}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple
