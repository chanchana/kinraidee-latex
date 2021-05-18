input_text = '''






[34]





'''

old_bib_dict = {}
import pickle
with open('object/old_bib_dict', 'rb') as f:
    old_bib_dict = pickle.load(f)

# print(old_bib_dict)

print()
print()
print('----------------------------------')
print()

for line in input_text.split('\n'):
    line = line.strip()
    if line:
        for key in old_bib_dict:
            if f'[{key}]' in line:
                line = line.replace(f'[{key}]', f'\\cite{{{old_bib_dict[key]}}}')
        print('\n' + line)

print()
print('----------------------------------')
print()