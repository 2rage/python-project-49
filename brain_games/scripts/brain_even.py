import random
from brain_games.constants import MAX_ATTEMPTS
from brain_games.game_logic import get_user_answer_string, print_question, print_correct_answer, print_wrong_answer, print_user_lose, print_user_win
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def handle_game_round(name) -> bool:
        
        random_number = random.randrange(1, 99)
        print_question(random_number)

        correct_answer = is_even(random_number)
        user_answer = get_user_answer_string()

        if user_answer != 'yes' and user_answer != 'no':
            print('Error. Please enter answer "yes" or "no"')
            return False

        if correct_answer == user_answer:
            print_correct_answer()
            return True
        else:
            print_wrong_answer(user_answer, correct_answer)
            print_user_lose(name)
            return False

def brain_even_number(name) -> int:
    print('Answer "yes" if the number is even, otherwise answer "no"')
    rounds_played = 0

    while rounds_played < MAX_ATTEMPTS:
        if handle_game_round(name):
            rounds_played += 1
        else:
            break

    if rounds_played == MAX_ATTEMPTS:
        print_user_win(name)


def main():
    greet()
    name = welcome_user()
    brain_even_number(name)


if __name__ == '__main__':
    main()
