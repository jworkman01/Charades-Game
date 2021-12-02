# Installing python:
First, check to see if you have python installed:
1. Open terminal
2. Run this command:
    
    python3 --version
3. If a current version number of python does not pop up, you don't have python installed
4. Install python, repeat step 2, and if a version number pops up, you can move on to the next steps

# Need to install the following (Instructions below):
1. pygame
2. time
3. requests

# How to install:
In order to install these, you will need pip installed on your machine. If you don't already have pip, to download and install it:
1. Open terminal and download pip by running this command:
    
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
2. Run this command:
    
    python3 get-pip.py

Now that you have pip installed, you can proceed with the remaining installs:  

3. Run this command:
    
    pip install requests
4. Run this command:
    
    pip install pygame
5. Run this command: 
    
    pip install time

You now have everything installed that is required to play our game. 
    
# To run the game after downloading it: 
1. Run this command:
    
    python3 main.py
    
# How to play:
1. 1 player from each team will need to have the game running on their machine
2. Once the game is started, the player acting out the words will have 5 minutes to get as many points as possible
3. If a team guesses correctly, click the score to add a point 
4. If the player wishes to skip the word, they can click "NEXT"
5. However, skipping a word does not count as a point, so don't click the score if you skipped the word
6. Continue to act out and guess words until the time runs out
7. At the end of the game, the team with the most points wins!
8. To quit the game, click "QUIT"
