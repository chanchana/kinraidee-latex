with open('data/scenario.txt') as f:
    for line in f:
        line = line.strip()
        if line:
            # print(line)
            if '[H]' in line:
                name = line[3:]
                print('\subsubsection{' + name + '}')
            else:
                title = ''
                data = ''
                sep = ''
                if ':' in line:
                    title, data = line.split(':', 1)
                    sep = ':'
                elif '.' in line:
                    title, data = line.split('.', 1)
                    sep = '.'
                else:
                    title = line
                print('\\textbf{' + title + '}' + sep + ' ' + data.strip() + '\\\\')




# \subsubsection{Register}

# \textbf{Name}: Users Login\\
# \textbf{Actors}: Users\\