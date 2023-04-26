# zip(iter, iter, ...)

list1 = ['a', 'b', 'c']
list2 = [10, 20, 30]
list3 = ['Wombat', 'Honey Badger', 'Prairie Dog']

combo = zip(list1, list2)

for item in combo:
    print(item)
print()

combo = zip(list1, list2)
print(f"combo: {combo}")

data = ['Fred', 'Ali', 'Hidago', 'Mary']
d_sort = sorted(data)
d_rev = reversed(data)

print(f"d_sort: {d_sort}")
print(f"d_rev: {d_rev}")

for letter, number in combo:
    print(letter * number)
print()

x = zip(list1, list2, list3)
print(f"x: {x}")
print(f"list(x): {list(x)}")
print(f"list(x): {list(x)}")

d1 = dict(zip(list1, list2))
print(f"d1: {d1}")




