"""
mastermind.py

De implementatie van het spel Mastermind zelf. Kan verschillende algoritmes gebruiken.

@author Lina Blijleven
@date   24/02/2022
"""
import itertools

# Importeer de functies om een mens te laten raden
import human

# Importeer de algoritmes
import simple
import bogo
import worst_case
import eig


# Importeer de hulpfuncties uit de utils file
from utils import feedback, generate_code

class Mastermind():

    # Spelopties
    kleuren = []
    lengte = 0
    duplicates = True
    max_guesses = 10
    method = ""

    # De huidige code
    code = ('R', 'R', 'R', 'R')

    # Constructor
    def __init__(self, kleuren=['R', 'O', 'Y', 'G', 'C', 'B'], lengte=4, duplicates=True, max_guesses=10, method='human'):

        self.kleuren = kleuren
        self.lengte = lengte
        self.duplicates = duplicates
        self.max_guesses = max_guesses
        self.method = method

        # Reset de code, guesses, etc.
        self.reset()

        # Print informatie voor de speler
        print("De mogelijke kleuren zijn: " + str(self.kleuren))
        print("De code heeft lengte: " + str(self.lengte))
        if (duplicates):
            print("De code kan meerdere keren dezelfde kleur bevatten.")
        else:
            print("Elke kleur komt maar een keer voor in de code.")
        print("Aantal pogingen beschikbaar: " + str(self.max_guesses))

        # Start het spel
        self.play(method)

    # Start een nieuw spel
    def reset(self):

            # Maak een code
        self.code = generate_code(self.kleuren, self.lengte, self.duplicates)
        print("De supergeheime code is: " + str(self.code))

        # Verwijder de oude geraden antwoorden
        self.guesses = []

    def permutaties(self):

        # Mogen we dubbele kleuren gebruiken?
        if (self.duplicates):
            perms = itertools.product(self.kleuren, repeat=self.lengte)
        else:
            perms = itertools.permutations(self.kleuren, self.lengte)
        # Zet de permutaties om naar een lijst i.p.v. itertools object
        return [p for p in perms]

    # Speel het spel
    def play(self, method):

        # Heeft de speler al gewonnen?
        gewonnen = False

        # Houd het aantal pogingen bij
        no_guesses = 0

        # Het spel gaat door tot de speler of de code goed heeft
        # of geen pogingen meer over heeft.
        while (not gewonnen and no_guesses < self.max_guesses):

            # Laat de speler raden
            print("Aantal overgebleven pogingen: " + str(self.max_guesses - no_guesses))

            # Bepaal de volgende gok met de gewenste methode
            if (method == 'bogo'):
                # Vraag een guess aan gebaseerd op bogosort
                guess = bogo.guess(self.kleuren, self.lengte, self.duplicates)
            elif(method == 'simple'):
                # Vraag een gok op gebaseerd op het simpele algoritme
                guess = simple.guess(self.permutaties, self.code)
            #elif(method == 'worst_case'):
                # Vraag een gok op gebaseerd op het worst case algoritme
                # guess = worst_case.guess()
            elif(method == 'eig'):
                # Vraag een gok op gebaseerd op het eigen algoritme
                guess = eig.eig(self.kleuren, self.code, self.permutaties)
            else:
                # Laat een mens gokken
                guess = human.guess(self.lengte, self.kleuren)

            # Is het goed? Dan laten we de speler weten dat hij heeft gewonnen
            if (''.join(self.code) == guess):
                gewonnen = True
            else:
                prev_guess = guess
                prev_feedback = feedback(self.code, guess)
                print("Kleuren op de juiste positie: " + str(prev_feedback[0]))
                print("Kleuren op de verkeerde positie: " + str(prev_feedback[1]))

            # Een poging gedaan
            no_guesses += 1

            # if (self.method == "simple"):
            #     simple.update(prev_guess, prev_feedback)

        if (gewonnen):
            print("Yay! je hebt gewonnen.")
        else:
            print("Helaas, je hebt geen pogingen meer.")
            print("De code was: " + str(self.code))

# Zet een spelletje mastermind klaar met de gekozen opties.
# Wil je het spel op een andere manier spelen? Bijvoorbeeld met meer kleuren of langere codes?
# Dan kun je dat hier aanpassen.
#
# Voor de methode heb je de keuze uit 'simpel', 'human' en 'bogo'
# Met duplicates kun je ervoor kiezen om wel of geen dubbele kleuren te gebruiken.

ai = input("Op welke manier wil je dat mastermind opgelost word?, human, worstcase, simple, bogo of eig? ")

if ai == "human":
    default = input("Wil je met de default settings spelen, "
                    "ja of nee? ")

    if default == "ja":
        game = Mastermind()

    if default == "nee":
        guess = int(input("Hoeveel guesses wil je? "))
        lengte_code = int(input("Hoelang wil je dat de code is? "))
        dups = input("Wil je dupes? ")
        if dups == "ja":
            game = Mastermind(lengte=lengte_code, duplicates=True, max_guesses=guess)
        else:
            game = Mastermind(lengte=lengte_code, duplicates=False, max_guesses=guess)

elif ai == "worstcase":
    Mastermind(method="worst_case")
elif ai == "simple":
    Mastermind(method="simple")
elif ai == "eig":
    Mastermind(method="eig")
elif ai == "bogo":
    Mastermind(method="bogo")



# Start een nieuwe ronde
#game.reset()
