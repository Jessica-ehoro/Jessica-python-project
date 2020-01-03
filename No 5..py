print('''Please pick one:
            rock

            paper

            scissors''')



while True:

    game_index = {'rock': 1, 'paper': 2, 'scissors': 3}

    player_a = str(input("Player A: "))

    player_b = str(input("Player B: "))

    a = game_index.get(player_a)

    b = game_index.get(player_b)

    g = a - b



    if g in [-1, 3]:

        print('player A is the winner!')

        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':

            continue

        else:

            print('Game Over! ')

            break

    elif g in [-3, 1]:
 
        print('player B is the winner! ')

        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':

            continue

        else:

            print('Game Over!')

            break

    else:

        print('Draw.Please continue.')

        print('')
