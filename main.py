def main():
    pygame.init()

    game = controller.Controller(800,600)
    game.mainLoop()

if __name__ == "__main__":
    main()
