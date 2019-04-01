from controller.game import Game

if __name__ == "__main__":
    game = Game()    
    continue_game = game.main_menu()

    while continue_game:## reinicia o jogo
        del game
        game = Game()
        continue_game = game.main_menu()