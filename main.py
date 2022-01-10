from random import randint
import numpy as np
import keyboard
import time
import tkinter as tk
from random import randint
from tkinter import BOTH


keys = ["left", "right", "up", "down"]


# Méthode permettant l'initialisation de la matrice 4x4
# avec deux composantes à '2' au lieu de '0'
def init():
    # TODO ajouter règles du jeu à l'init

    m = np.zeros((4,4))
    for i in range(2):
        init_random_case(m)
    return m


def init_random_case(m):
    case_occupe = True
    while case_occupe:
        x = randint(0, 3)
        y = randint(0, 3)
        if m[x, y] == 0:
            case_occupe = False
            m[x, y] = 2
    return m


def jouer(m):
    print("A vous de jouer !\n")
    key_pressed = detect_key_pressed()
    print(key_pressed)
    match key_pressed:
        case 'left':
            left(m)
        case 'right':
            right(m)
        case 'up':
            up(m)
        case 'down':
            down(m)
    return m


def detect_key_pressed():
    print("detect_key_pressed()")
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('left'):  #
                print('Left')
                return 'left'
            if keyboard.is_pressed('right'):  #
                print('Right')
                return 'right'
            if keyboard.is_pressed('up'):  #
                print('Up')
                return 'up'
            if keyboard.is_pressed('down'):  #
                print('Down')
                return 'down'
        except:
            print('Mauvaise touche')
            break  # if user pressed a key other than the given key the loop will break


def test_fin_partie(m):
    # TODO Améliorer test fin de partie
    #   Toutes les cases peuvent être remplies et la partie non terminée [2, 2, 2, 2]
    test = 'Partie perdue'
    for ligne in m:
        if 2048 in ligne:
            test = 'Partie gagnée'
            break
        elif 0 in ligne:
            test = 'Partie en cours'
            break
    return test


def left(m):
    ligne = 0
    while ligne < 4:
        colonne = 1
        while colonne < 4:
            # Si la case n'est pas vide
            if m[ligne, colonne] != 0:
                while colonne != 0 and m[ligne, colonne - 1] == 0:
                    m[ligne, colonne - 1] = m[ligne, colonne]
                    m[ligne, colonne] = 0
                    colonne -= 1
                if colonne != 0 and m[ligne, colonne - 1] == m[ligne, colonne]:
                    m[ligne, colonne - 1] *= 2
                    m[ligne, colonne] = 0
                    colonne -= 2
            colonne += 1
        ligne +=1
    m = init_random_case(m)
    return m


def right(m):
    ligne = 0
    while ligne < 4:
        colonne = 2
        while colonne >= 0:
            # Si la case n'est pas vide
            if m[ligne, colonne] != 0:
                while colonne != 3 and m[ligne, colonne + 1] == 0:
                    m[ligne, colonne + 1] = m[ligne, colonne]
                    m[ligne, colonne] = 0
                    colonne += 1
                if colonne != 3 and m[ligne, colonne + 1] == m[ligne, colonne]:
                    m[ligne, colonne + 1] *= 2
                    m[ligne, colonne] = 0
                    colonne += 2
            colonne -=1
        ligne +=1
    m = init_random_case(m)
    return m


def up(m):
    colonne = 0
    while colonne < 4:
        ligne = 1
        while ligne < 4:
            # Si la case n'est pas vide
            if m[ligne, colonne] != 0:
                while ligne != 0 and m[ligne - 1, colonne] == 0:
                    m[ligne -1, colonne] = m[ligne, colonne]
                    m[ligne, colonne] = 0
                    ligne -= 1
                if ligne != 0 and m[ligne - 1, colonne] == m[ligne, colonne]:
                    m[ligne - 1, colonne] *= 2
                    m[ligne, colonne] = 0
                    ligne -= 2
            ligne += 1
        colonne += 1
    m = init_random_case(m)
    return m


def down(m):
    colonne = 0
    while colonne < 4:
        ligne = 2
        while ligne >= 0:
            # Si la case n'est pas vide
            if m[ligne, colonne] != 0:
                while ligne != 3 and m[ligne + 1, colonne] == 0:
                    m[ligne + 1, colonne] = m[ligne, colonne]
                    m[ligne, colonne] = 0
                    ligne += 1
                if ligne != 3 and m[ligne + 1, colonne] == m[ligne, colonne]:
                    m[ligne + 1, colonne] *= 2
                    m[ligne, colonne] = 0
                    ligne += 2
            ligne -= 1
        colonne += 1
    m = init_random_case(m)
    return m


# GUI
def couleur(valeur):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    if valeur == 0:
        rgb = (240, 240, 240)
        return "#%02x%02x%02x" % rgb
    else:
        g = 255 * (2048 - valeur) / 2048
        b = 230 * (2048 - valeur) / 2048
        rgb = (255, int(g), int(b))
        return "#%02x%02x%02x" % rgb


# Début du programme
print('2048 sur Python \n')

# Initialisation du jeu
partie_en_cours = 'Partie en cours'
matrice = init()

# Initilisation du GUI
window = tk.Tk(className='2048 en Python')
window.geometry("480x480")
window.resizable(False, False)

for i in range(4):
    for j in range(4):
        frame = tk.Frame(
            master=window,
            borderwidth=0,
            height=100,
            width=100
        )
        frame.grid(row=i, column=j, padx=10, pady=10)
        frame.pack_propagate(False)
        valeur = randint(0,2048)
        label = tk.Label(master=frame, text=f"{matrice[i,j]}", bg=couleur(matrice[i,j]))
        label.grid(row=i, column=j)
        label.pack(fill=BOTH, expand=1)

window.update()

# Jeu
while partie_en_cours == 'Partie en cours':
    print(matrice)
    time.sleep(0.5)
    matrice = jouer(matrice)

    for i in range(4):
        for j in range(4):
            frame = tk.Frame(
                master=window,
                borderwidth=0,
                height=100,
                width=100
            )
            frame.grid(row=i, column=j, padx=10, pady=10)
            frame.pack_propagate(False)
            valeur = randint(0,2048)
            label = tk.Label(master=frame, text=f"{matrice[i,j]}", bg=couleur(matrice[i,j]))
            label.grid(row=i, column=j)
            label.pack(fill=BOTH, expand=1)

    window.update()

    partie_en_cours = test_fin_partie(matrice)

# Sortie du jeu
if partie_en_cours == 'Partie gagnée':
    print('Vous avez gagné !')
elif partie_en_cours == 'Partie perdue':
    print('Vous avez perdu !')
else:
    print('Mauvaise sortie de jeu')
