
 
# Hangman game
#

# -----------------------------------
# Helper code


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
'''
def isWordGuessed(secretWord, lettersGuessed):
    
    #secretWord: string, the word the user is guessing
    #lettersGuessed: list, what letters have been guessed so far
    #returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    #  False otherwise
    # FILL IN YOUR CODE HERE...
    l=[]
    for char in secretWord:
        temp=lettersGuessed.count(char)
        l.append(temp)
    
    if 0 in l:
        return False
    else:
        return True
'''
def isWordGuessed(secretWord, lettersGuessed):
    temp=''.join(lettersGuessed)
    return (temp[-1] in secretWord)
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    l=[]
    for char in secretWord:
        temp=lettersGuessed.count(char)
        l.append(temp)
    for i in range(len(l)):
        if l[i]==0:
           secretWord=secretWord.replace(secretWord[i],'_')
    return secretWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    b='abcdefghijklmnopqrstuvwxyz'
    b=list(b)
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in b:
             b.remove(lettersGuessed[i])
    return ''.join(b)
    
 
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print ('''Welcome to the game, Hangman!
I am thinking of a word that is %d letters long.
-----------''' %len(secretWord))
    num=8
    l=[]
    N=[]
    while num>0:
        print 'You have '+str(num)+' guesses left.'
        print 'Available letters:'+ getAvailableLetters(l)
        lg= raw_input('Please guess a letter:')
        lg=lg.lower()
        l.append(lg)
        NI=getGuessedWord(secretWord,l)
        N.append(NI)
        if(isWordGuessed(secretWord,l)and N.count(NI)==1):
            print 'Good guess:',getGuessedWord(secretWord,l)
            num+=1
        elif(l.count(lg))>1:
            print "Oops! You've already guessed that letter:",getGuessedWord(secretWord,l)
            num+=1
        else:
            print 'Oops! That letter is not in my word:',getGuessedWord(secretWord,l)
        print '-----------'
        if secretWord==NI:
            print 'Congratulations, you won!'
            break
        num-=1
    if secretWord!=NI:
        print 'Sorry, you ran out of guesses. The word was else.'
    print secretWord




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
