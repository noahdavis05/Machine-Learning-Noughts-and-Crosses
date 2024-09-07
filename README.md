# Machine Learning Noughts and Crosses
This is a Python implementation of Noughts and Crosses (Tic-Tac-Toe), inspired by the MENACE (Matchbox Educable Noughts and Crosses Engine) concept. It uses a machine learning approach to train the bot to play the game. The bot improves over time by playing multiple games and adjusting its strategy based on results.

## Table of Contents
- [Overview](#overview)
- [Files and Structure](#files-and-structure)
- [Usage](#usage)

## Overview
This project was inspired by a video on the MENACE engine I watched on youtube https://www.youtube.com/watch?v=R9c-_neaxeU.
This initally started out as a command line game, but I added a very basic user interface usign pygame.
### Bot's Learning
The bot uses a simple reinforcement learning algorithm: after each game, it reinforces successful strategies (winning moves) and penalizes the moves that lead to losses. Over time, the bot's decision-making process becomes more refined, making it a fairly competent opponent. <br><br> However, the bot is not perfect at this stage. Occasionally, it makes seemingly careless mistakes, which I believe stem from a lack of sufficient training. This becomes especially apparent when the game reaches unusual states that the bot rarely encounters during training. For example, if the player makes an unconventional move (like missing a winning opportunity), the bot may fail to recognize the optimal response. These rare game states are undertrained, and the bot struggles with less common scenarios.
### The Results
I’ve also included a pre-trained dataset in the repository, so the bot already performs well right from the start. Although it hasn’t been trained for too long, the results are impressive—the bot makes smart plays and is quite difficult to beat. Even in its current state, the bot is adept at creating winning opportunities and often forcing draws when a win isn’t possible.

## Files and Structure
- bot.py contains the bot class which is used in training and in the game.
- main.py is the file where the bots are trained.
- noughtsAndCrosses.py is the class for the noughts and crosses grid.
- game.py is the file where the user can play against the bot.
- setUpDB.py is the file to initialise and create the table in the database for training.
- training.db is the database with the weightings for each move.

## Usage
To use this code yourself: Clone this repo. install pygame 
```
pip install pygame
```
Optional - Initialize the database and train the bots.
```
python setUpDB.py
python main.py
```
Play against the bot.
```
python game.py
```
This will launch the graphical interface where you can play against the bot.

