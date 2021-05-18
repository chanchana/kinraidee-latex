file_name = 'appendixb'
figure_size = 'width=350pt'
prefix = 'A2'

figure_dict = {}

is_list_started = False

with open(f'data/{file_name}.txt') as f:
    for line in f:
        line = line.strip()
        if line:
            if line[:6] == 'Figure' and ':' in line:
                # print(line)
                figure_number = line.split(': ')[0].split(' ')[1]
                figure_caption = line.split(': ')[1]
                figure_name = line.split(': ')[1].replace(' ', '').replace('\'', '').replace('’', '')
                figure_ref_name = f'{prefix}{figure_name}'
                figure_dict[figure_number] = figure_ref_name

with open(f'data/{file_name}.txt') as f:
    with open(f'output/{file_name}.txt', 'w') as fw:
        for line in f:
            line = line.strip()
            if line:
                if line[:6] == 'Figure' and ':' in line:
                    # print(line)
                    figure_number = line.split(': ')[0].split(' ')[1]
                    figure_caption = line.split(': ')[1]
                    figure_name = line.split(': ')[1].replace(' ', '').replace('\'', '').replace('’', '')
                    figure_ref_name = f'{prefix}{figure_name}'
                    fw.write(f"\n\\begin{{figure}}[H]\centering\n")
                    fw.write(f"\\includegraphics[{figure_size}]{{./images/{figure_ref_name}.png}}\n")
                    fw.write(f"\\caption{{{figure_caption}}}\label{{fig:{figure_ref_name}}}\n")
                    fw.write(f"\\end{{figure}}\vspace{{-24pt}}\n")
                else:
                    paragraph = line
                    for key in figure_dict:
                        print(f'Figure {key}')
                        paragraph = paragraph.replace(f'Figure {key}', f"Figure~\\ref{{fig:{figure_dict[key]}}}")
                    fw.write('\n' + paragraph + '\n')
                    print(paragraph)

                # print(line)



print(figure_dict)

# \begin{figure}[!h]\centering
# \includegraphics[width=400pt]{./images/3seqdiagram_grouprec.png}
# \caption{Create Group Sequence Diagram}\label{fig:3seqdiagram_grouprec}
# \end{figure}