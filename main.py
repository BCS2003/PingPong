from src.gui import GUI
import player1 as p1
import player2 as p2


def main():
    gui = GUI(600, 400, title='Ping Pong', icon='assets/icon.png')
    gui.run_loop()


if __name__ == '__main__':
    main()
