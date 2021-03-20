theBoard = {'TL': ' ','TM': ' ','TR': ' ',
            'ML': ' ','MM': ' ','MR': ' ',
            'LL': ' ','LM': ' ','LR': ' ',}

def printBoard(board):
    print('\nCurrent state')
    print('-------')
    print('|' + board['TL'] + '|' + board['TM'] + '|' + board['TR'] + '|')
    print('|-+-+-|')
    print('|' + board['ML'] + '|' + board['MM'] + '|' + board['MR'] + '|')
    print('|-+-+-|')
    print('|' + board['LL'] + '|' + board['LM'] + '|' + board['LR'] + '|')
    print('-------')

def printGuide():
    print('\nOptions')
    print('TL | TM | TR\nML | MM | MR\nLL | LM | LR')
    print('\n(Press D for draw...)\n')

print('\n\n' + "=" * 100)
print('\nWelcome to our super simple TicTacToe game!...')
print('Playing this game is easy, once you pick the player names, just pick your options from the list below')

player1 = input('\nEnter who will Play with X: ')
print('Ok!, ' + player1 + ' will play with X. ')

player2 = input('\nEnter who will Play with O: ')
print('Ok!, ' + player2 + ' will play with O. ')

currentPlayer = player1
turn = "X"
while True:

    printBoard(theBoard)
    printGuide()

    move = input('\n' + currentPlayer + '(' + turn + '), Enter your move: ').upper()
        
    if move.lower() == 'd':
        print('\nYou choose to draw, exiting!\n')
        break

    if theBoard.get(move,'--') == '--':
        print('\nInvalid Entry, try again')
        continue

    if theBoard.get(move) != ' ':
        print('\n' + move + ' already taken, try again')
        continue

    theBoard[move] = turn

    if ((theBoard['TL'] == theBoard['TM'] == theBoard['TR']) and theBoard['TL'] != ' ') or \
       ((theBoard['ML'] == theBoard['MM'] == theBoard['MR']) and theBoard['ML'] != ' ') or \
       ((theBoard['LL'] == theBoard['LM'] == theBoard['LR']) and theBoard['LL'] != ' ') or \
       ((theBoard['TL'] == theBoard['ML'] == theBoard['LL']) and theBoard['TL'] != ' ') or \
       ((theBoard['TM'] == theBoard['MM'] == theBoard['LM']) and theBoard['TM'] != ' ') or \
       ((theBoard['TR'] == theBoard['MR'] == theBoard['LR']) and theBoard['TR'] != ' ') or \
       ((theBoard['TL'] == theBoard['MM'] == theBoard['LR']) and theBoard['TL'] != ' ') or \
       ((theBoard['LL'] == theBoard['MM'] == theBoard['TR']) and theBoard['LL'] != ' '):
        print('\n' + currentPlayer + '(' + turn + '), You won!')
        printBoard(theBoard)
        break

    isDraw = True
    for i in theBoard:
        if theBoard.get(i) == ' ':
            isDraw = False
            break
    
    if isDraw:
        printBoard(theBoard)
        print('\nNo more moves, its a Draw!\n')
        break

    if turn == "X":
        turn = "O"
        currentPlayer = player2
    else:
        turn = "X"
        currentPlayer = player1