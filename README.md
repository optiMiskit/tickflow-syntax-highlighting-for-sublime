# Tickflow Syntax for [Sublime Text](https://www.sublimetext.com)
A collection of resources to add Tickflow syntax highlighting that is context aware (example: hex numbers that represent subroutines are colored differently than hex numbers used as values). Color scheme is based on Notepad++ and the original color scheme provided with [Tickompiler](https://github.com/rhmodding/Tickompiler).  

![screenshots](https://github.com/optiMiskit/tickflow-syntax-highlighting-for-sublime/blob/main/Screenshots.png)

## Installation
1. Clone the repo or download the latest release: [![Downloads](https://img.shields.io/github/downloads/optiMiskit/tickflow-syntax-highlighting-for-sublime/total.svg)](https://github.com/optiMiskit/tickflow-syntax-highlighting-for-sublime/releases). It is recommened to use this with Sublime Text 4.  
2. Place the `Tickflow_pkg` folder in the Sublime package folder (which you can find via `Preferences-> Browse Packages`).  
3. Close any .tickflow files you had open prior to installation and restart Sublime Text.  
4. To build through Sublime Text, place **both** `Tickomplier.jar` and `base.bin` in **one** of these directories:
```
.
├── Desktop/
│   └── RH_tools/
├── Documents/
│   └── RH_tools/
 ```
As a last resort, Sublime will attempt to use these files from the same folder as the currently opened .tickflow file.  
You can also modify `Build_Paths.py` (where specified) to add your own set locations for these files, if you'd prefer these files to be elsewhere.  
If for whatever reason your Citra installation doesn't have the [default user directory location](https://citra-emu.org/wiki/user-directory), you can also specify the location of /sdmc/rhmm/.  

## Usage - Syntax
* Any .tickflow file you open will automatically use the .tickflow color scheme and syntax highlighting.  
* If you type at the start of a new line, Sublime will have auto-complete suggestions. Typically, there will be some description and a list of arguments for each suggestion.
* If you hit 'Enter' on a suggestion, Sublime will highlight the first argument, so you can fill it in. If you hit 'Tab', you will move onto the next argument and so forth, until there are no more arguments.  
* For the list of currently known command names, you can type `` ` `` at the start of a new line. Please note that Sublime doesn't automatically delete the `` ` `` should you hit 'Enter' on one of the options in the list, so you will need to remove it.

## Usage - Builds

Builds: Using `Tools->Build With`, you have three build options:  

| Build Option  | About |
| ------------- | ------------- |
| Tickflow  | Compiles the currently open tickflow file  |
| Compile, Pack, & Move to Citra  | Same as previous + it packs the .bin file with all .tempo files in the directory into a C00.bin file   + it copies C00.bin into the /sdmc/rhmm/ folder in Citra  |
| [Multi] Compile, Pack, & Move to Citra  | Similar to previous, but instead it builds and packs all tickflow files in the same directory as the currently opened tickflow file  |
###### Output
Compilied files and tempo files are put into a "Compiled" folder. C00.bin is placed in the same folder as the tickflow file, but also copied to the Citra /sdmc/rhmm/ folder.

###### Useful Tip
Once you choose a Build option (via `Build With`), Sublime will set that option as the `Build` command (Ctrl+B / ⌘+B).
