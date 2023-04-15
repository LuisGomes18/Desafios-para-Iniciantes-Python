import curses

stdscr = curses.initscr()  # inicializa a biblioteca curses
curses.cbreak()  # desabilita o buffer de linha
stdscr.keypad(True)  # habilita a entrada de teclas especiais

n = 0

while n < 3:
    Jogada_Player_1 = str(input('Sua vez de jogar player 1: '))
    stdscr.clear()  # limpa a tela usando a função clear() da biblioteca curses
    Jogada_Player_2 = str(input('Sua vez de jogar player 2: '))
    stdscr.clear()  # limpa a tela usando a função clear() da biblioteca curses
    n += 1

stdscr.keypad(False)  # desabilita a entrada de teclas especiais
curses.echo()  # habilita o buffer de linha
curses.endwin()  # finaliza a biblioteca curses
