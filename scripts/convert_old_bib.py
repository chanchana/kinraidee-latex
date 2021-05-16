old_bib_datafile = 'data/old_bib.txt'
new_bib = 'output/newbib.txt'

replace_bib_2 = '''
@article{ RecommendationSystemsPrinciples,
  author =	 {F.O. Isinkaye and Y.O. Folajimi and B.A. Ojokoh},
  title =	 {Recommendation systems: Principles, methods and evaluation},
  journal =	 {Egyptian Informatics Journal},
  volume =	 16,
  number =	 3,
  year =	 2015
}
'''

replace_bib_33 = '''
@article{ ExpertSystemsWithApplications,
  author =	 {Garcia, I. and Sebastia, L. and & Onaindia, E},
  title =	 {On the design of individual and group recommender systems for tourism},
  journal =	 {Expert Systems with Applications},
  volume =	 38,
  number =	 6,
  year =	 2011
}

'''

olb_bib_dict = {}

number = 1
with open (old_bib_datafile) as f:
    with open (new_bib, 'w') as fw:
        for line in f:
            line = line.strip()
            bib_result = ''
            name = ''
            if line:
                if number == 2:
                    name = 'RecommendationSystemsPrinciples'
                    bib_result = replace_bib_2
                elif number == 33:
                    name = 'ExpertSystemsWithApplications'
                    bib_result = replace_bib_33
                elif '[Online]' in line:
                    author = line.split('. (')[0]
                    title = line.split('“', 1)[1].split('”', 1)[0]
                    name = ''.join(e for e in title if e.isalnum())
                    howpublished = f"Available at \\url{{{line.split('Available: ', 1)[1].split('. [', 1)[0]}}}"
                    note = f"[Online; accessed {line.split('[Accessed ', 1)[1].split('].', 1)[0].replace(' ', '-')}]"
                    bib_result = f'''
@misc{{ {name},
  author = {{{author}}},
  title = {{{{{title}}}}},
  howpublished = \"{howpublished}\",
  note = \"{note}\"
}}
                    '''
                else:
                    print('error')
                print(bib_result)
                olb_bib_dict[number] = name
                fw.write(bib_result)
                number += 1


import pickle
with open('object/old_bib_dict', 'wb') as f:
    pickle.dump(olb_bib_dict, f)


# @misc{bworld,
#   author = {L. Bao},
#   title = {{BWorld Robot Control Software}},
#   howpublished = "Available at \url{http://aiweb.techfak.uni-bielefeld.de/content/bworld-robot-control-software/}",

#   note = "[Online; accessed 19-July-2008]"
# }

# @misc{bworld,
#   author = {L. Bao},
#   title = {{BWorld Robot Control Software}},
#   howpublished = "Available at \url{http://aiweb.techfak.uni-bielefeld.de/content/bworld-robot-control-software/}",

#   note = "[Online; accessed 19-July-2008]"
# }
