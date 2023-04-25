import typing as T

def spam(color: str, country: T.Any) -> None:
    print("color: {}".format(color))
    print("country: {}".format(country))
    # return None

spam("blue", "Italy")
spam(10, 20)

def double(thing):
    return thing * 2

print("double('trouble'): {}".format(double('trouble')))

values = ['red', 'Paraguay']
spam(values[0], values[1])
spam(*values)  # expand values iterable to individual arguments


def find_lines(search_term, *file_paths, ignore_case=True):
    if ignore_case:
        search_term = search_term.lower()
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                if ignore_case:
                    search_line = raw_line.lower()
                else:
                    search_line = raw_line
                if search_term in search_line:
                    line = raw_line.rstrip()
                    print(file_path, line)

find_lines('Rabbit', "DATA/alice.txt", "DATA/words.txt", ignore_case=False)

find_lines("wombat")

def hello(whom="world"):
    print(f"Hello, {whom}")

hello("Fred")
hello("North Carolina")
hello()

spam(country="Burkina Faso", color="purple")

#       pos      pos     pos  kw      kw
#       only     req     opt  req     opt
def wacky(p1, /, p2, p3, *p4, p5, p6, **p7):
    pass

# wacky(10, 15, 20, 1, 2, 3, p4="wombat", p5="badger")

def toast(spread, /):
    print(spread)

toast('jam')
toast('marmite')
toast('honey')
# toast(spread="peanut butter")

animal = "woodchuck"

def ham():
    fruit = "mango"  # local variable
    print("animal: {}".format(animal))

ham()
print("fruit: {}".format(fruit))






