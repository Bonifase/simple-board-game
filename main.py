from constants import NUM_ROWS, NUM_COLS
from helpers import player_turn, create_board, play_again


def main():
    lets_play_again = True
    max_score = NUM_ROWS * NUM_COLS // 2

    while lets_play_again:
        # initialise values
        board = create_board()
        player_turns = 0
        player_score = 0

        # main logic
        game_over = False
        while not game_over:
            success = player_turn(board, player_score, player_turns)
            if success:
                player_score += 1
            player_turns += 1
            if player_score >= max_score:
                game_over = True
        print()
        print('Congartulations!')
        print('You completed the game in', player_turns, 'turn')
        print('Your score is', player_score, '.', sep='')

        if not play_again():
            lets_play_again = False
    print('Goodbye!')


if __name__ == '__main__':
    main()
