# Minecraft-Stronghold-Finder
This is a small program used to quickly find the closest stronghold relative to the player's position in a Minecraft world using only two Eyes of Ender and some information displayed pressing F3 on the keyboard.

## How to use
First of all we choose a random point from which we throw the first Eye of Ender. Once we throw it, we need to turn towards the direction of the Eye of Ender (without moving our character, X and Z coords must remain the same). Now we press F3 and take note of these three numbers:

* X coordinate
* Z coordinate
* Direction we're facing

![Minecraft image 1](/images/Minecraft1d.png "First throw of Eye of Ender")

Then we move about 150 blocks away from the first point, possibly perpendicularly to the direction of the stronghold, and we throw another Eye of Ender, and we take note of the X, Z coordinates and the direction, just like before.

![Minecraft image 2](/images/Minecraft2d.png "Second throw of Eye of Ender")

Now we're ready to use the program by double-clicking on the .exe file (note that it might take some second for the program to open). We just need to insert the data in the correct text fields and press "Calculate". The approximate coordinates of the stronghold should appear at the bottom. 


