import curses

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)

n = 0

while n < 3:
    Jogada_Player_1 = str(input('Sua vez de jogar player 1: '))
    stdscr.clear()
    Jogada_Player_2 = str(input('Sua vez de jogar player 2: '))
    stdscr.clear()
    n += 1

stdscr.keypad(False)
curses.echo()
curses.endwin()
