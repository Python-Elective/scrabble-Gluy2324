import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """

    # checking pre-cont=dition
    assert isinstance(word, str), "word must be a string"
    word = word.lower()
    assert word.islower()
    assert len(word)
    assert isinstance(n, int), "n must be an int"
    assert n > 0, "hand length n must not be 0"


    #Psuedocode

    """
    For each letter in word
        get letter score from dict SCRABBLE_LETTER_VALUES
        add up all the letter scores

    multiply by length of words
    followed by bonus calculation
    example, if n=7 and you make the word 'waybel' on the first try
    it would be worth 115 points
    """
    word_score = 0
    for letter in word:
        word_score += SCRABBLE_LETTER_VALUES[letter]
    word_score *= len(word)
    if len(word) == n:
        word_score += 50

    # checking post-condition
    assert word_score >= 0, "score calculation failed - score is negative"
    assert isinstance(word_score, int), "score must be integer"


    return word_score

# testcase
#print(get_word_score("happy", 7))


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")       # print all on the same line
    print()     
    
#display_hand({'a': 2})

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n // 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

#print(deal_hand(7))

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    """
    make a hand.copy()
    for every letter in word
        use the letter has a key to look up in the hand dict
        and subtract 1 from the dict values letter counts

    return handcopy
    """
    hand_copy = hand.copy()
    for letter in word:
        if letter in hand_copy:
            hand_copy[letter] -= 1
        if hand_copy[letter] == 0:
            del hand_copy[letter]
    
    return hand_copy


print(update_hand({'k':1, 'e':2, 'y':3}, 'key'))