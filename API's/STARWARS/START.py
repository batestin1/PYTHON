# STARPEDIA

# Este é um projeto de requisição de api e armazenamento de dados em python, consumindo, para isso,
# a API do STARWARS
# link da api = https://swapi.dev/


import requests
import json
import time
import pandas as pd
from pymongo import MongoClient
import pymongo


#working connection
client = MongoClient('localhost', 27017)




#functions
def open():
    time.sleep(1)
    print('~' * 35)
    time.sleep(1)
    print('~' * 12 + 'STARPEDIA' + '~' * 16)
    time.sleep(1)
    print('~' * 35)
    time.sleep(1)
    print('~' + 'Developed by Maycon Cypriano' + '~~')
    print('~' * 35)
    print('')
    print('')
    time.sleep(1)
    print('This is your STARPEDIA!')
    time.sleep(1)
    print("""Here you can know all the information about Characters,
     Planets and Species of the STAR WARS universe""")
    time.sleep(1)
    choice()
    repet()


def choice():
    time.sleep(1)
    choice = input("""To get started, which item you want to explore:
    [A] - Characters 
    [B] - Planets
    [C] - Species
    Answer: """).upper()[0]

    if choice == 'A':
        characters()
    elif choice == 'B':
        planets()
    elif choice == 'C':
        species()
    else:
        print('Sorry, try again!')

def characters():
    time.sleep(1)
    pe = input('Enter the name of the character you want to refer to? ')
    people = requests.get(f'https://swapi.dev/api/people/?search={pe}')
    people_1 = json.loads(people.text)['results'][-1]
    name = people_1['name']
    height = people_1['height']
    mass = people_1['mass']
    hair = people_1['hair_color']
    skin = people_1['skin_color']
    eyes = people_1['eye_color']
    birth = people_1['birth_year']
    gender = people_1['gender']

    persona1 = {'Name': [name],
               'Mass': [mass],
               'Height':[height],
               'Hair':[hair],
               'Skin': [skin],
               'Eyes': [eyes],
               'Birth Year': [birth],
               'Gender': [gender]}
    persona1 = pd.DataFrame(persona1)
    db = client['StarWars']
    collections = db['persona']
    collections.insert_many(persona1.to_dict('Results'))
    persona1.to_excel('STARPEDIA-PERSONA.xlsx', index=False)

    time.sleep(1)
    print('We re processing your character')
    time.sleep(1)
    print('...')
    print('')
    time.sleep(1)
    print(f"""Here's the information we have about your character
    Full name: {name};
    Full weight: {mass} stone;
    Height: {height} inch;
    Hair Color: {hair};
    Eye Color: {eyes};
    Intergalatic Year of Birth: {birth};
    Gender: {gender}    
    """)
    time.sleep(1)
    print("""Your result was also saved in a STARPEDIA-PERSONA file, 
    thank you for the preference and may the force be with you.""")

def planets():
    time.sleep(1)
    pla = input('Which planet do you want to explore? ')
    planetis = requests.get(f'https://swapi.dev/api/planets/?search={pla}')
    planets_1 = json.loads(planetis.text)['results'][-1]
    name = planets_1['name']
    rotation = planets_1['rotation_period']
    orb = planets_1['orbital_period']
    dia = planets_1['diameter']
    clima = planets_1['climate']
    gravi = planets_1['gravity']
    population = planets_1['population']
    planetss = {'Name': [name],
               'Rotation': [rotation],
               'Orbital Period': [orb],
               'Diameter': [dia],
               'Climate': [clima],
               'Gravity': [gravi],
               'Population': [population]}
    planetss = pd.DataFrame(planetss)
    db = client['StarWars']
    collections = db['planets']
    collections.insert_many(planetss.to_dict('Results'))
    planetss.to_excel('STARPEDIA-PLANETS.xlsx', index=False)
    time.sleep(1)
    time.sleep(1)
    print('We re processing your planet')
    time.sleep(1)
    print('...')
    print('')
    time.sleep(1)
    print(f"""Here's the information we have about your planet
        Full name: {name};
        Rotation Period: {rotation}d;
        Diameter: {dia}km;
        Climate: {clima};
        Gravity: {gravi};
        Population: {population};  
        """)
    time.sleep(1)
    print("""Your result was also saved in a STARPEDIA-PLANETS file, 
        thank you for the preference and may the force be with you.""")

def species():
    time.sleep(1)
    es = input('Enter the species you want to get information? ')
    specie = requests.get(f'https://swapi.dev/api/species/?search={es}')
    specie_1 = json.loads(specie.text)['results'][-1]
    name = specie_1['name']
    clas = specie_1['classification']
    desig = specie_1['designation']
    skin = specie_1['skin_colors']
    life = specie_1['average_lifespan']
    lang = specie_1['language']
    speciess = {'Name': [name],
               'Classification': [clas],
               'Designation': [desig],
               'Skin Color': [skin],
               'Lifespan': [life],
               'Natural Language': [lang]}
    speciess = pd.DataFrame(speciess)
    db = client['StarWars']
    collections = db['Species']
    collections.insert_many(speciess.to_dict('Results'))
    speciess.to_excel('STARPEDIA-SPECIES.xlsx', index=False)
    time.sleep(1)
    time.sleep(1)
    print('We re processing your species')
    time.sleep(1)
    print('...')
    print('')
    time.sleep(1)
    print(f"""Here's the information we have about your species:
            Full name: {name};
            Classification: {clas};
            Designation: {desig};
            Skin Color: {skin};
            Lifespan: {life} years;
            Natural Language: {lang};  
            """)
    time.sleep(1)
    print("""Your result was also saved in a STARPEDIA-PLANETS file, 
            thank you for the preference and may the force be with you.""")

def repet():
    rs = input("Do you want to repeat the query?(y/n) ").upper()[0]
    if rs == 'Y':
        choice()
    else:
        print("Thank you and may the force be with you!")


if __name__== '__main__':
    open()