import pygame
from src import Controller


# from src import ControllerWithSubloops

def main():
    # pygame.init()pip
    # team = {"lead": "Joseph", "backend": "Matthew", "frontend": "Fayeem"}
    # print("software lead is:" , team["lead"])
    # print("backend is:" , team["backend"])
    # print("frontend is" , team["frontend"])
    game = Controller.Controller()
    game.mainloop()


# WithSubloops
###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
main()
