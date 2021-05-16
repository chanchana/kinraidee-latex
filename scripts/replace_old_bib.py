input_text = '''



After the selection process, this process will use those chromosomes to generate the next generation by either crossover or mutation. Crossover is the most significant phase in a genetic algorithm. For each pair of parents to be mated, a crossover point is chosen at random from within the genes. [9] After that, offspring will be created and added to the population of next generation. For mutation, it occurs when new offspring are formed by flipped some bits. This process exists to maintain the diversity of population and prevent premature convergence.

 [8]

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