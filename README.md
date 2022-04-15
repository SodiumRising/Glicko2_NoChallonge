# Glicko2_NoChallonge
Glicko2 Python code without using the Challonge API


players.txt - Text file containing the players and their ratings, rds, and vol values. Each value is separated by a semi-colon (;). 
              New players are added to this file with the default values of Rating: 1500, RD: 350, Vol: 0.06
              The code will run the math and update these values accordingly.

tournament.txt - This file is the file you update to show who played who and who won. Each value is separated by a semi-colon (;).
                 The first entry is the player, followed by who they played, and lastly who won the match (0 = loss, 1 = win).
               
The math is ran by running the script "calculation.py", make sure to update the tournament.txt before running the script.            
