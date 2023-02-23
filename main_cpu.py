from random import choice, randint

from func_board import change_board as cb
from func_choosesimbol import choose_simbol as cs
from func_selection import selection as sl
from func_start import start
from func_winner import winner as wn

your_values, cpu_values, options, board, turn = start()
symbol, symbol_value = cs()

while True:

    # os.system('cls')

    if turn == 2:
        break

    elif options == []:
        print('It is a draw.')
        break

    else:

        if turn == 1:

            value = choice(options)
            options.remove(value)
            cpu_values += value

            symbol = 'O' if symbol_value == 0 else 'X'

            print(f'The CPU chose {value}.')

        else:
            print('It your turn.')
            print(f'The disponible options are: {options}')

            value = input('Choose a value.')

            value, options = sl(value, options)

            print(f'The chosen value was {value}.')

            your_values += value

            symbol = 'O' if symbol_value == 1 else 'X'

        board = cb(value, board, symbol)

        turn = wn(turn, your_values, cpu_values) if symbol_value == 0 else wn(
            turn, cpu_values, your_values)

        print(board)
        print()
