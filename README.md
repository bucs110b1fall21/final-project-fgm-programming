:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Space Invaders
## CS 110 Final Project
### Fall 2021
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

[https://github.com/bucs110b1fall21/final-project-fgm-programming](#)

<< [link to demo presentation slides](#) >>

### Team: FGM Programming
#### George Reisner, Fayeem Mooktadeer, Matthew Davidson

***

## Project Description *(Software Lead)*
Our project is a take on the classic "Space Invaders" game. The player takes control of a ship that has to make sure the enemy ships don't go past. The player does this by launching projectiles at the enemy ships to destroy them. If an enemy ship goes past the player without being destroyed, the player will lose a life until they reach zero. The enemies approach in waves each one harder than the last. 

***    

## User Interface Design *(Front End Specialist)*
* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
* << You should also have a screenshot of each screen for your final GUI >>
![starterGUI](https://raw.githubusercontent.com/ingmarlehmann/qml-invaders/master/docs/screenshots/menu.png)
![GAME](https://www.nodebox.net/node/documentation/concepts/subnetworks-space-invaders.png)
![GAMEOVER](https://thumbs.dreamstime.com/b/space-invaders-game-over-9507779.jpg)


***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * Pygame, random, sys
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). >>
        * ![class diagram](assets/class_diagram.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * controller -  , ControllerWithSubloops - , Enemy - The object that must be destroyed by the player, moves down from the top of the screen, Player - The character that is controllled by the player and can fire projectiles at enemies, as well as move left and right, Projectile - This will be the object fired by the player at the enemy, when it hits the enemy they are destroyed 

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* bin
    * <all of your python files should go here>
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - George Reisner

Worked as integration specialist by making sure all of the code worked as a whole and fixing bugs and issues when they came up. As well as writing the ATP and the proposals. Worked on classes: Controller, Projectile, Enemy

### Front End Specialist - Fayeem Mooktadeer

Front-end lead conducted significant research on how to make the GUI and controller work, as well as properly implemented them to work with the other parts of the project. Worked on Controller class.

### Back End Specialist - Matthew Davidson

The back end specialist ceated the classes for each part. As well as outlined how the classes interact with each other while the game was underway. Also added the diagrams for how everything will work initially. Worked on class: Player

## Testing *(Software Lead)*
* We would troubleshoot issues as they happened by doing small sections of the project at once before adding them to the big project. This allowed for easy fixing before bad code messed up larger parts and be harder to spot.
    * Originally, a problem we ran into was the classes not showing up on the screen and only showing a blank page. That was fixed by changing the controller. Another issue was the key down command was recording two responses instead of one.


* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run Counter Program  | GUI window appears with count = 0  |          |
|  2  | click count button  | display changes to count = 1 |                 |
etc...
