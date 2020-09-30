from words import fruits
from words import animals
from words import places
from words import randoms
import random

def getFruit():
    word=random.choice(fruits)
    return word

def getAnimal():
    word=random.choice(animals)
    return word

def getPlace():
    word=random.choice(places)
    return word

def getRandom():
    word=random.choice(randoms)
    return word

def play(word):
    word_complete="-" *len(word)
    guessed= False
    guessed_letters=[]
    guessed_words=[]
    tries=6
    #print("Lets play Hungman!")
    print(display(tries))
    print(word_complete)
    print("\n")
    while not guessed and tries >0:
        guess=input("Please guess a letter:")
        if len(guess)==1 and guess.isalpha:
            if guess in guessed_letters:
                print("You already guessed the alphabet")
            elif guess not in word:
                print(guess,"is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,",guess," is in the word")
                guessed_letters.append(guess)
                word_as_List=list(word_complete)
                indices= [i for i,letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_as_List[index]=guess
                word_complete="".join(word_as_List)
                if "-" not in word_complete:
                    guessed = True
        elif len(guess)== len(word):
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess," is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed= True
                word_complete=word
        else:
            print("Not a valid guess.")
        print(display(tries))
        print(word_complete)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word")
    else:
        print("Sorry, you ran out of tries. the word was",word)

def display(tries):
    stages=[#0
        """

        --------
        |    |
        |    o
        |   \|/
        |    |
        |   / \\
        -

        """,
        #1
        """

        --------
        |    |
        |    o
        |   \|/
        |    |
        |   /    
        -

        """,
        #2
        """

        --------
        |    |
        |    o
        |   \|/
        |    |
        |   
        -

        """,
         #3
        """

        --------
        |    |
        |    o
        |   \|
        |    |
        |   
        -

        """,
        #4
        """

        --------
        |    |
        |    o
        |    |
        |    |
        |   
        -

        """,
        #5
        """

        --------
        |    |
        |    o
        |  
        |    
        |   
        -

        """,
        #6
        """

        --------
        |    |
        |    
        |  
        |    
        |   
        -

        """


    ]
    return stages[tries]

def main():
    ask='y'
    while ask=='y':
        print("Lets play Hungman!")
        print("""Please Select a Category
        1.Friuts
        2.Animals
        3.Places
        4.Random
        """)
        number=int(input("Enter a number for the Category selected:"))
        if number==1:
            wordgiven=getFruit()
            play(wordgiven)
        elif number==2:
            wordgiven=getAnimal()
            play(wordgiven)
        elif number==3:
            wordgiven=getPlace()
            play(wordgiven)
        elif number==4:
            wordgiven=getRandom()
            play(wordgiven)
        else:
            print("Invalid choice.")
        ask=input("Play again (y/n)")

if __name__ == "__main__":
    main()