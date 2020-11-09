import random
import string

words = ['python', 'java', 'kotlin', 'javascript']
correct_answer = random.choice(words)
accepted_characters = string.ascii_lowercase
guess = list(len(correct_answer) * '-')
guessed_correct_char = set()
lives = 8
print('H A N G M A N')
while True:
    user_choice = input('Type "play" to play the game, "exit" to quit:')
    if user_choice not in {'play', 'exit'}:
        continue
    if user_choice == 'exit':
        break
    else:
        while lives > 0:
            if guess == list(correct_answer):
                print('You guessed the word!\nYou survived!')
                break
            else:
                print('\n' + ''.join(guess))
                char = input('Input a letter:')
                if len(char) != 1:
                    print('You should input a single letter')
                elif char not in accepted_characters:
                    print('It is not an ASCII lowercase letter')
                elif char in guessed_correct_char:
                    print('You already typed this letter')
                elif char not in correct_answer:
                    print('No such letter in the word')
                    lives -= 1
                    guessed_correct_char.add(char)
                else:
                    for j in range(len(correct_answer)):
                        if correct_answer[j] == char:
                            guess[j] = char
                            guessed_correct_char.add(char)
        else:
            print('You are hanged!\n')

