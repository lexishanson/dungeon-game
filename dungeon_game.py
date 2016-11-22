import random

# think of a way to hold on to a map. Should be a list. We'll put tuples in there as record of each location

CELLS = [(0,0), (0,1), (0,2),
         (1,0), (1,1), (1,2),
         (2,0), (2,1), (2,2)]


def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)

    if monster == door or monster == start or door == start:
        return get_locations

    return monster, door, start

    # monster = random location
    # door = random " "
    # start(player) = random " "
    # if monster, door, start are the same, do it again
    # return monster, door, start


def move_player(player, move):
    # player = (x,y)
    x, y = player #because we can't modify tuple that is player, so we'll modify these two values

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1
    return x, y

    # get the player's current location
    # if move is LEFT, y - 1
    # if move is RIGHT, y + 1
    # if move is UP, x - 1
    # if move is DOWN, x + 1

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    # player = (x, y)
    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2:
        moves.remove('RIGHT')
    if player [0] == 0:
        moves.remove('UP')
    if player[0] == 2:
        moves.remove('DOWN')
    # if player's y is 0, remove DOWWN
    # if player's x is 0, remove UP
    # if player's x is 2, remove LEFT
    # if players y is 2, remove RIGHT
    return moves

def draw_map(player):
    # - - - 
    # _/_/_/
    print(' _ _ _')
    tile = '|{}'

    for idx, cell, in enumerate(CELLS): #look at CELLS as indexes
        if idx in [0, 1, 3, 4, 6, 7]:
            if cell == player:
                print(tile.format('X'), end = '')
            else:
                print(tile.format('_'), end = '')
        else:
            if  cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))


monster, door, player = get_locations()
print("Welcome to the dungeon!")


while True:
    moves = get_moves(player)

    print("You're currently in room{}".format(player)) # fill in position
    draw_map(player) 
    print("You can move{}".format(moves))  #fill in with avail moves
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break
    if move in moves:
        player = move_player(player, move)
    else:
        print("**Walls are hard, stop walkinginto them!**")
        continue #because we want to immediately refresh if they give us a bad one
    
    if player == door:
        print("You escaped!")
        break
    elif player == monster:
        print("You were eaten by the montser!")
        break

    # if it's a good move, change player's position
    # if it's a bad move, dont do anything
    # if the new player position is the door, they win
    # if the new player position is the monster, they lose
    # otherwise, continue
