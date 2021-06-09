import random
animal = {'lion': ['mane', 'teeth', 'pride', 'Africa', 'predator'],
          'tiger': ['stripes', 'fur', 'endangered', 'cat', 'claws'],
          'bear': ['hibernates', 'North America', 'Brown', 'Fur', 'Strong'],
          'owl': ['hoot', 'nocturnal', 'flies', 'big eyes', 'eats mice'],
          'frog': ['pond', 'green', 'tongue', 'amphibian', 'eats flies'],
          'toucan': ['rainbow', 'long beak', 'South America', 'tropical', 'wings'],
          'monkey': ['eats bananas', 'trees', 'tail', 'swing', 'primate'],
          'shark': ['ocean', 'dangeous', 'cartilege', 'sharp teeth', 'fins'],
          'zebra': ['stripes', 'black and white', 'africa', 'safari', 'hoofs'],
          'wolverine': ['vicious', 'skunk bear', 'brown', 'small', 'fast']}

randomanimal = random.choice(dict(enumerate(animal)))
guess = ""
attributes = animal[randomanimal]
print ("Let's play a game!")
print ("Guess the animal I'm thinking of.")

while guess != randomanimal:
    if guess in attributes:
        print ("yes")
    elif guess in animal.keys():
        print ("Try Again")
    elif guess != "":
        print ("no")

    guess = raw_input('What animal am I thinking of?')

print ("You Win")