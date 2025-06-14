![carmin](https://github.com/user-attachments/assets/b5690853-ccaf-4b2e-833e-96c6119a789c)

Bive Alpha is a perlin noised based procedural generation game, with a solid foundation on [Pygame](https://pygame.org/) and [PyOpenGl](https://pyopengl.sourceforge.net/). It's mainly focused on exploration of a world, made up of blocks. Currently there are 8 biomes on the game: Flatgrass, Plains, Muddy Hills, Desert, Snowy Plains, Candyland, Caves and Mossy Caves.
Bive is a good way to study and mess with procedural generation, due to it's simple algorithm of terrain creation, don't believe? Look it up yourself!

## Dependencies
  - Latest [Python](https://www.python.org/downloads/) version  
  - Latest [pip](https://pypi.org/project/pip/) version

## How to play 
Here is a guide of how you can play Bive on your PC:

  1. First download the Bive [Source code](https://github.com/gabrielmchiapetti/BiveAlpha/releases) to your machine.
  2. Extract the code into a folder wherever you like
  3. Navigate to that folder and open terminal, do not enter the assets folder! Make sure you can see the MAIN.py file
  4. Type this command:

If on Windows:
```
python MAIN.py
```

If on Linux:
```
python3 MAIN.py
```

  5. Relax! Bive automatically downloads the dependencies needed via pip, just make sure you got it right!
  6. The game should be running! If not then leave the error on the [issues page](https://github.com/gabrielmchiapetti/BiveAlpha/issues).

### Screenshots!
  
![Python 3 11 25_05_2025 14_08_25](https://github.com/user-attachments/assets/8165a383-147a-4db5-a3f0-5248cd7654aa)
_The Muddy Hills biome_
    
![Python 3 11 25_05_2025 14_55_06](https://github.com/user-attachments/assets/e090448a-8013-433a-9794-b1904193b098)
_The Caves biome with inventory open (Early dev)_
  
  
## Player Settings
The Player settings are located in the **Options** folder, on the **options.txt** file, in that file there are the settings for:

> Mouse sensitivity  
> Desired FPS (Frames Per Second)  
> Camera Render Distance  
> Default Volume (Also controllable in the title screen)  
> Default Biome  

## How to Modify

It seems like you vibe with the game! So first, read the content on the LICENSE file carefully, after that if you wan't to modify the game for things like messing with terrain gen, adding biomes and blocks, etc. you really should consider also reading the following info:

## What each files contains:

### MAIN.py
> Its the main application, it pieces together every single of these files to make the game!

### config.py
> Screen width and screen height, font, logos, icons, background, volume control functions, window title and misc.

### graphics.py
> Just graphics! Blocks, world rendering and hotbar drawing.

### terrain.py
> All the terrain generation functions, uses a lot from graphics.py!

### initialize.py
> Pygame and OpenGl initialization, crucial parts.

### inventory.py
> Hotbar and a reminiscent of a block counter (Useless)
> 
### titlescreen.py
> It's the whooooole title screen, all the blitting and keyboard detection stuff for the title screen.

### loadingscreen.py
> It's the whooooole loading screen  (sorry for doing it again), all the blitting and keyboard detection stuff for the loading screen.

### player.py
> Mouse sensitivity, default terrain, render distance, starting volume and misc.

### splashtexts.py
> Splash texts selecting mechanics

### linecounter.py
> Its a Line Counter that counts lines from all the code files of the game (Including itself)

# About the Assets folder
The assets folder is where all the music/splashtexts/images are stored, it is structured like this:

### Audios
  * All of the music and soundtracks, and also their original sources.
    
### Fonts
  * It is the home of the fonts, it being Baskervville and it's licenses.
    
### Logos
  * All of the logos and icons for the game, all except two are used, but i just wanted to have something to switch the logos for sometimes.  

### Others
  * Only contains the splashtexts at the moment, no future things planned for here, maybe some promo material later, just maybe.

### Textures
  * All of the textures (Backgrounds at the moment) used in the game, even though there is not any textures here, I kept the name from a huge fail of texture adding.

# Anyways! I hope you have fun with Bive! Good Luck :D, if you need any any help, message me! I'm always online.
