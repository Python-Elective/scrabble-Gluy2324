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

    # magic coding
    word_score = 0

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

    # checking post-condition
    assert word_score > 0, "score calculation failed"
    assert isinstance(word_score, int), "score must be integer"
    return word_score

# testcase
# legal
get_word_score("haPPy", 7)

#Ilegal
get_word_score(10000, 7)
get_word_score("", 7)
get_word_score("blabla", 0)
    