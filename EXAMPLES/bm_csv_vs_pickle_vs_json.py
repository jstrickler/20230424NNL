
from timeit import Timer

REPEATS = 100

setup = '''
from csv import reader, writer
import pickle
'''

code_snippets = [
'''
with open('../DATA/city-of-chicago-salaries.csv') as junk_in:
   rdr = reader(junk_in)
   for row in rdr:
       pass
''',

'''
with open('../DATA/city-of-chicago-salaries.pic', "rb") as junk_in:
    data = pickle.load(junk_in, errors="replace")
''',
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup)
    print("{:60.60s} {}".format(code_snippet, t.timeit(REPEATS)))
    print('-' * 60)
