import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word: str, n: int):
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

    if len(word) > 0:
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


def display_hand(hand: dict):
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

def update_hand(hand: dict, word: str):
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
    assert isinstance(hand, dict), "hand must be a dictionary"
    assert isinstance(word, str), "word must be a string"


    hand_copy = hand.copy()
    for letter in word:
        if letter in hand_copy:
            hand_copy[letter] -= 1
            if hand_copy[letter] == 0:
                del hand_copy[letter]
    return hand_copy

#testcase
#print(update_hand({'k':1, 'e':2, 'y':3}, 'key'))



def is_valid_word(word: str, hand: dict , word_list: list) -> bool:
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    #checking pre condition
    assert isinstance(word, str), "word must be a string"
    #    "hello".count('l')     ans = 2

    """
    psuedocode!

    check if the word is in word_list or not
    make a hand_copy
    check for every letter in word
        if those letter is in hand coppy and those letter is still usable
            reduce those letter by 1
        else
            return false
    if all passed return true
    """


    hand_copy = hand.copy()

    for letter in word:
        if letter in hand_copy and hand_copy[letter] > 0:
            hand_copy[letter] -= 1
        else:
            return False
    if word not in word_list:
        return False
    return True

#testcase
print(is_valid_word("hello", {'h':1, 'e':1, 'o':1, 'l':2}, ['hello'])) #ans = TRUE
print(is_valid_word("hello", {'h':1, 'e':1, 'l':1, 'o':1}, ['hello'])) #ans = FALSE

def calculate_hand_len(hand : dict):
    """ 
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    len_hand = sum(hand.values())
    return len_hand

#print(calculate_hand_len({'h':1, 'e':1, 'l':2, 'o':1})) #ans = 5

def play_hand(hand : dict, word_list, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    # As long as there are still letters left in the hand:
    # Display the hand
    # Ask user for input
    # If the input is a single period:
    # End the game (break out of the loop)
    # Otherwise (the input is not a single period):
    # If the word is not valid:
    # Reject invalid word (print a message followed by a blank line)
    # Otherwise (the word is valid):
    # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
    # Update the hand
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score

    total_score = 0
    period = " "
    while True:
        hand = deal_hand(n)
        length_hand = calculate_hand_len(hand)

        if length_hand > 0:
            print("Current Hand:" + display_hand(hand))
        word = input('Enter word, or a "." to indicate that you are finished: ')
        word_score = get_word_score(word, n)

        print_total_score = str(total_score) + "points."
        print_word_score = str(word_score) + "points."

        if word == ".":
            print("Goodbye! Total score:" + print_total_score)
        else:
            if period in word:
                print("the input is not a single period")
                break
            else:
                if is_valid_word(word, hand, word_list) != True:
                    print("Invalid word, please try again." + "\n")
                else:
                    total_score += word_score
                    print('"' + word + '" earned' + print_word_score + print_total_score + "\n")




