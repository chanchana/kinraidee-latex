figure_dict = {}

is_list_started = False

with open('data/ui3.txt') as f:
    for line in f:
        line = line.strip()
        if line:
            if line[:6] == 'Figure' and ':' in line:
                # print(line)
                figure_number = line.split(': ')[0].split(' ')[1]
                figure_caption = line.split(': ')[1]
                figure_name = line.split(': ')[1].replace(' ', '')
                figure_ref_name = f'3ui_{figure_name}'
                figure_dict[figure_number] = figure_ref_name

with open('data/ui3.txt') as f:
    with open('output/ui_design.txt', 'w') as fw:
        for line in f:
            line = line.strip()
            if line:
                if '[H]' in line:
                    fw.write(f"\\newpage\n\\subsection{{{line.replace('[H]', '')}}}\n")
                elif line[:6] == 'Figure' and ':' in line:
                    # print(line)
                    figure_number = line.split(': ')[0].split(' ')[1]
                    figure_caption = line.split(': ')[1]
                    figure_name = line.split(': ')[1].replace(' ', '')
                    figure_ref_name = f'3ui_{figure_name}'
                    fw.write(f"\\begin{{figure}}[!h]\centering\n")
                    fw.write(f"\\includegraphics[height=300pt]{{./images/{figure_ref_name}.png}}\n")
                    fw.write(f"\\caption{{{figure_caption}}}\label{{fig:{figure_ref_name}}}\n")
                    fw.write(f"\\end{{figure}}\n")
                elif line[0].isnumeric():
                    if not is_list_started:
                        fw.write('\\begin{enumerate}\n')
                        is_list_started = True
                    fw.write(f"\\item {line.split('.', 1)[1].strip()}\n")
                else:
                    if is_list_started:
                        fw.write('\\end{enumerate}\n')
                        is_list_started = False
                    paragraph = line
                    for key in figure_dict:
                        print(f'Figure {key}')
                        paragraph = paragraph.replace(f' Figure {key}', f"~\\ref{{fig:{figure_dict[key]}}}")
                    fw.write(paragraph + '\n')
                    print(paragraph)

                # print(line)



print(figure_dict)

# \begin{figure}[!h]\centering
# \includegraphics[width=400pt]{./images/3seqdiagram_grouprec.png}
# \caption{Create Group Sequence Diagram}\label{fig:3seqdiagram_grouprec}
# \end{figure}