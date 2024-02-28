from Main import *

def read_player_command():
    move = None
    while move not in {'g','d','h','b'} :
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move

def read_size_grid():
    size = 0
    while size <2 :
        size = int(input("Entrez la taille de la grille :"))
    return(size)

def read_theme_grid():
    theme = None
    while theme not in {'0', '1', '2'} :
        theme = input("Entrez le theme souhaité (0 (Default), 1 (Chemistry), 2 (Alphabet)) : ")
    return theme

if __name__ == '__main__':
    game_play()
    exit(1)


