fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

target_letter = "x"
for fruit in fruits:
    if fruit.startswith(target_letter):
        print(fruit.title())
        break
else:
    print(f"{target_letter} not found")


