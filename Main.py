import random, numpy as np, time
from textual_2048 import *
THEMES = {
    "0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256",
          512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"},
    "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O",
          512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"},
    "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H",
          512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}
}

def create_grid(taille_grid):
    assert type((taille_grid)) == int
    game_grid = []
    for i in range(0,taille_grid):
        game_grid.append([0 for i in range(taille_grid)])
    return game_grid

def get_value_new_tile():
    p = random.randint(0,100)
    if p > 90 :
        return(4)
    return(2)

def get_all_tiles(grid):
    tiles = []
    for i in range(len(grid)) :
        for j in range(len(grid[i])):
            if grid[i][j] in {' ' , 0, ""}:
                tiles.append(0)
            else :
                tiles.append(grid[i][j])
    return tiles

def get_empty_tiles_positions(grid):
    positions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in {' ' , 0, ""}:
                positions.append((i,j))
    return(positions)

def grid_get_value(grid, x, y):
    if grid[x][y] == ' ' or grid[x][y] == '':
        return(0)
    return(grid[x][y])

def get_new_position(grid):
    empty_positions = get_empty_tiles_positions(grid)
    random_position = empty_positions[random.randint( 0 , len(empty_positions) - 1 )]
    return random_position

def grid_add_new_tile(grid):
    x , y = get_new_position(grid)
    value = get_value_new_tile()
    grid[x][y] = value
    return(grid)

def init_game(taille_grid):
    grid = create_grid(taille_grid)
    grid_add_new_tile(grid)
    grid_add_new_tile(grid)
    return(grid)

def grid_to_string(grid, taille):
    a = """"""
    for i in range(taille):
        a = a + ' ===' * taille
        a = a + '\n'
        a = a + '|   ' * taille + '|\n'
    a = a + ' ===' * taille
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ' ' :
                position = ((4*taille)+1)*(i+1) + ((4*taille)+2)*i + (j*4) + 2
                a = a[ : position] + str(grid[i][j]) + a[position+1: ]
    return (a + '\n')

def long_value(grid):
    values = get_all_tiles(grid)
    longest = max(values)
    return len(str(longest))

def grid_to_string_with_size(grid,taille_grille,longueur_valeur):
    a = """"""
    for i in range(taille_grille):
        a = a + (' ' + ('=' * (2+longueur_valeur)))* taille_grille + '\n'
        a = a + ('|' + ' ' * (2+longueur_valeur)) * taille_grille + '|\n'
    a = a + (' ' + '=' * (2+longueur_valeur))* taille_grille
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ' ':
                position = ((((2+longueur_valeur)+1) * taille_grille) + 1) * (i + 1) + ((((2+longueur_valeur)+1) * taille_grille) + 2) * i + (j * ((2+longueur_valeur)+1)) + 2
                a = a[: position] + str(grid[i][j]) + (' ' * (longueur_valeur-len(str(grid[i][j])))) + a[position + longueur_valeur:]
    return a

def long_value_with_theme(grid,theme):
    tiles = get_all_tiles(grid)
    tiles = set(tiles)
    keys = theme.keys()
    values = theme.values()
    length = 0
    for tile in tiles :
        if tile in keys :
            if length < len(theme[tile]) :
                length = len(theme[tile])
    return length

def grid_to_string_with_size_and_theme(grid,theme,taille_grille,longueur_valeur):
    a = """"""
    for i in range(taille_grille):
        a = a + (' ' + ('=' * (2+longueur_valeur)))* taille_grille + '\n'
        a = a + ('|' + ' ' * (2+longueur_valeur)) * taille_grille + '|\n'
    a = a + (' ' + '=' * (2+longueur_valeur))* taille_grille
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] not in {0,'',' '}:
                position = ((((2+longueur_valeur)+1) * taille_grille) + 1) * (i + 1) + ((((2+longueur_valeur)+1) * taille_grille) + 2) * i + (j * ((2+longueur_valeur)+1)) + 2
                a = a[: position] + theme[grid[i][j]] + (' ' * (longueur_valeur-len(theme[grid[i][j]]))) + a[position + longueur_valeur:]
    return(a + '\n')

def move_row_left(row1):
    row = np.copy(row1)
    row = list(row)
    j = -1
    nb_zeroes = 0
    while j<len(row):
        try :
            j += 1
            if row[j] == 0 :
                row.pop(j)
                nb_zeroes += 1
                j -= 1
        except:
            break
    for i in range(nb_zeroes):
        row.append(0)
    for k in range(len(row)-1):
        if row[k] !=0 and row[k] == row[k+1]:
            row[k] = row[k]*2
            row.pop(k+1)
            row.append(0)
    return(row)

def move_row_right(row1):
    row = np.copy(row1)
    row = list(row)
    j = -1
    nb_zeroes = 0
    while j<len(row):
        try :
            j += 1
            if row[j] == 0 :
                row.pop(j)
                nb_zeroes += 1
                j -= 1
        except:
            break
    for i in range(nb_zeroes):
        row.insert(0,0)
    for k in range(len(row)-1,0,-1):
        if row[k] !=0 and row[k] == row[k-1]:
            row[k] = row[k]*2
            row.pop(k-1)
            row.insert(0,0)
    return(row)

def move_grid(grid,direction):
    if direction in {"d","right"} :
        new_grid = []
        for i in range(len(grid)):
            new_grid.append(move_row_right(grid[i]))
    elif direction in {"g","left"} :
        new_grid = []
        for i in range(len(grid)):
            new_grid.append(move_row_left(grid[i]))
    elif direction in {"b","down"} :
        new_grid = np.copy(grid)
        new_grid = np.array(new_grid)
        new_grid = new_grid.transpose()
        new_grid = list(new_grid)
        for i in range(len(new_grid)):
            new_grid[i]= list(new_grid[i])
        new_grid = move_grid(new_grid,"d")
        new_grid = np.array(new_grid)
        new_grid = new_grid.transpose()
        new_grid = list(new_grid)
        for j in range(len(new_grid)):
            new_grid[j]= list(new_grid[j])
    elif direction in {"h","up"} :
        new_grid = np.copy(grid)
        new_grid = np.array(new_grid)
        new_grid = new_grid.transpose()
        new_grid = list(new_grid)
        for i in range(len(new_grid)):
            new_grid[i]= list(new_grid[i])
        new_grid = move_grid(new_grid,"g")
        new_grid = np.array(new_grid)
        new_grid = new_grid.transpose()
        new_grid = list(new_grid)
        for j in range(len(new_grid)):
            new_grid[j]= list(new_grid[j])
    return new_grid

def is_grid_full(grid):
    if len(get_empty_tiles_positions(grid)) == 0 :
        return(True)
    return(False)

def move_possible(grid):
    #ordres des mouvements de la liste à renvoyer : g, d, u, b
    moves = [True,True,True,True]

    if move_grid(grid,"g") == grid :
        moves[0] = False

    if move_grid(grid,"d") == grid :
        moves[1] = False

    if move_grid(grid,"h") == grid :
        moves[2] = False

    if move_grid(grid,"b") == grid :
        moves[3] = False

    return moves

def is_game_over(grid):
    if move_possible(grid) == [False,False,False,False] :
        return True
    return False

def get_grid_tile_max(grid):
    maxim =[]
    for i in range(len(grid)):
        maxim.append(max(grid[i]))
    return(max(maxim))

def is_winner(grid):
    if get_grid_tile_max(grid) >= 2048 :
        return True
    return False

def random_play():
    grid = init_game(4)
    print(grid_to_string_with_size_and_theme(grid, THEMES["0"], 4, long_value_with_theme(grid,THEMES["0"])))
    while is_game_over(grid) == False :
        try :
            move = random.choice(("d","g","h","b"))
            grid = move_grid(grid, move)
            grid = grid_add_new_tile(grid)
            print(grid_to_string_with_size_and_theme(grid, THEMES["0"], 4, long_value_with_theme(grid,THEMES["0"])))
            time.sleep(1)
        except :
            continue
    if is_winner(grid)==True :
        print(" CONGRATULATIONS !!! ")
    else :
        print(" Try again loser ")
    return None

def game_play() :
    grid_size = read_size_grid()
    theme_number = read_theme_grid()
    grid = init_game(grid_size)
    print(grid_to_string_with_size_and_theme(grid, THEMES[theme_number], grid_size, long_value_with_theme(grid,THEMES[theme_number])))
    while is_game_over(grid) == False :
        try :
            move = read_player_command()
            grid = move_grid(grid, move)
            grid = grid_add_new_tile(grid)
            print(grid_to_string_with_size_and_theme(grid, THEMES[theme_number], grid_size, long_value_with_theme(grid,THEMES[theme_number])))
        except :
            continue
    if is_winner(grid)==True :
        print(" CONGRATULATIONS !!! ")
    else :
        print(" Try again loser ")
    return None

if __name__ == "__main__" :
    game_play()