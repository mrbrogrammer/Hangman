from hashlib import new
import sys
import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    new_word = []
    random_index = random.randint(0, len(word)-1)
    random_letter = word[random_index]
    # print the word with the unguessed letters censored
    for i in range(len(word)):
        if word[i] == random_letter:
            new_word.append(word[i])
        else:
            new_word.append("_")

    new_word = "".join(new_word)
    return new_word


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    if char in original_word and char not in answer_word:
        return True
    elif char in original_word:
        return False

# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    answer_word = enumerate(answer_word)
    new_word = ""
    # notify the player that the "letter" has multiple characters
    for index, character in answer_word:   
        if original_word[index] == char:
            new_word = new_word + char
        else:
             new_word = new_word + character
    return new_word

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def do_correct_answer(original_word, answer, guess):
    # notify the player that the letter is not in the word
    answer = fill_in_char(original_word, answer, guess)
    if guess == answer:
        answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    if number_guesses >= 0:
        print('Wrong! Number of guesses left: '+str(number_guesses))
        draw_figure(number_guesses)
    elif number_guesses == 0:
        draw_figure(number_guesses)

# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    figure = ["/----\n|\n|\n|\n|\n_______",
        "/----\n|   0\n|\n|\n|\n_______",
        "/----\n|   0\n|  /|\\\n|\n|\n_______",
        "/----\n|   0\n|  /|\\\n|   |\n|\n_______",
        "/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______",][::-1]
    print(figure[number_guesses])



# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    
    print("Guess the word: "+answer)
    guess = get_user_input()
    number_guesses = 5
    
    while number_guesses > 0:
        if guess == "quit" or guess =="exit":
            print("Bye!")
            break
        # if the function is_missing_char returns True return new more complete word
        elif is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
            if answer == word:
                break
            else:
                guess = get_user_input()
        else:
            if number_guesses > 1:
                # decrement attempt counter
                number_guesses -= 1
                do_wrong_answer(word, number_guesses)
                guess = get_user_input()
            else:
                number_guesses -= 1
                do_wrong_answer(word, number_guesses)
    # notify the player of defeat
    if number_guesses == 0:
        print("Sorry, you are out of guesses. The word was: "+word)

# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    # get file from the command line
    if len(sys.argv) == 2:
        words_file = sys.argv[1:]
        words_file = "".join(words_file)
    elif len(sys.argv) != 2:
        words_file = ask_file_name()

    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)