input_text = '''






 Eatsee is an application that helps users find dishes that they’ll love by setting their preferences and swipe through user-tailored results, tap to find out more about the restaurant, then swipe right to save it to be favorites. Eatsee is currently available in Newcastle (New South Wales, Australia), Coffs Harbour (New South Wales, Australia), and San Francisco (California, United States). [31]

        Compared to our system, Eastsee only suggests random food based on their preference setting which doesn’t learn about users’ behavior. It focuses on food, not restaurants but our system prioritizes restaurants over food. It doesn’t support group suggestions and restaurants located in Thailand.


Whatever Mans (เที่ยงนี้กินไรดี)

Figure 2.5: Screenshot of Whatever Mans Application
[Source: https://play.google.com/store/apps/details?id=com.DEC.Eatwhat&hl=th]

        Whatever Mans Application is a Thai food random application that has an interaction with the user by creating an interactive animation called Pa-Man (ป้าแม้น) to talk with the user. Whatever Mans is available for download on Android only.

        Compared to our system, Whatever Mans Application supports only on an Android platform whereas our system supports both iOS and Android because of web application technology. Their suggestion isn't based on users’ profiles or preferences which means their suggestion is just randomization. Although it supports Thai food, it can suggest only food, not restaurants. It also doesn’t support group suggestions.

Tinder


Figure 2.6: Screenshot of Tinder Application
[Source: https://www.androidauthority.com/best-tinder-alternatives-android-1084559/]

Tinder is a geosocial networking and online dating application that allows users to anonymously swipe to like or dislike other profiles based on their photos, a small bio, and common interests. Once two users have "matched", they can exchange messages. [32]

Compared to our system, Tinder shares a similarity with our system which is a recommendation algorithm. It learns user preferences over time and suggests new people based on their preferences. However, their suggestion is based on individuals because it is a dating application.  The main contrast to our system is that Tinder focuses on suggesting new people whereas our system suggests restaurants.



On the design of Individual and Group Recommender Systems for Tourism Paper

Figure 2.7: GRSK Architecture from the Paper
[Source: https://www.semanticscholar.org/paper/On-the-design-of-individual-and-group-recommender-Garcia-Sebastia/b367686e60db2f68102cd14b1360e9fc26a1757b]

This paper presents a recommender system for tourism based on the tastes of the users, their demographic classification, and the places they have visited on former trips. The system is able to offer recommendations for a single user or a group of users. The group recommendation is elicited out of the individual personal recommendations through the application of mechanisms such as aggregation and intersection. The elicitation mechanism is implemented as an extension of e-Tourism, a user-adapted tourism and leisure application whose main component is the Generalist Recommender System Kernel (GRSK), a domain-independent taxonomy-driven recommender system. [33]

        Compared to our system, the algorithm designed in this paper can be adapted with our group recommendation system. However, their study focuses on tourism but our system focuses on restaurant recommendation.


Dynamic Music Recommender System Using Genetic Algorithm
This paper represents a music recommendation system that is able to recognize and provide items corresponding with user favorites. The system is able to identify the n-number of users' preferences and adaptively recommend music tracks according to user preferences by extracting unique features of each music track. Then applying BLX-a crossover to the extracted features of each music track. [https://www.ijeat.org/wp-content/uploads/papers/v3i4/D2957043414.pdf] The recommender is base on genetic algorithm along with content-based filtering technique for generate the initial population in genetic algorithm which can divided into 3 phase including feature extraction phase, evolution phase, and interactive Genetic algorithm phase. User favorite and user profiles are included. After that the successive page is constructed based on the user evaluation.

Compared to our system, the information of this paper that uses the genetic algorithm is similar to our system which are user favorite and user profiles. But the differences are our objective function and the system architecture in which we focus on the restaurant.






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