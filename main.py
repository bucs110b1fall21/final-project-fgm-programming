from src import Controller
from src import ControllerWithSubloops

def main():
    #pygame.init()
    #team = {"lead": "Joseph", "backend": "Matthew", "frontend": "Fayeem"}
    #print("software lead is:" , team["lead"])
    #print("backend is:" , team["backend"])
    #print("frontend is" , team["frontend"])
    game = ControllerWithSubloops.Controller()
    game.mainloop()


    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
main()
