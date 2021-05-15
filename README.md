# Tickflow Syntax for [Sublime Text](https://www.sublimetext.com)
A collection of resources to add Tickflow syntax highlighting that is context aware (example: hex numbers that represent subroutines are colored differently than hex numbers used as values).  
Color scheme is based on Notepad++ and the original color scheme provided with [Tickompiler](https://github.com/rhmodding/Tickompiler).

![screenshots](https://github.com/optiMiskit/tickflow-syntax-highlighting-for-sublime/blob/main/Screenshots.png)

## Installation
1. Download the latest release: [![Downloads](https://img.shields.io/github/downloads/optiMiskit/tickflow-syntax-highlighting-for-sublime/total.svg)](https://github.com/optiMiskit/tickflow-syntax-highlighting-for-sublime/releases) or clone the repo.  
2. Place the `Tickflow_pkg` folder in the Sublime package folder (which you can find via `Preferences-> Browse Packages`).  
3. Close any .tickflow files you had open prior to installation and restart Sublime Text.  
4. If you would like to set a Tickompiler path (for compiling), edit `Tickflow.sublime-build` (by default, it will try to use Tickompiler in the same directory as your .tickflow file).

## Usage
Any .tickflow file you open will automatically use the .tickflow color scheme and syntax highlighting.  
Using `Tools->Build`, you can also compile into a .bin file.

    
## Purpose
Makes navigation easier; provides tickflow syntax support for a program that is natively supported by Windows, MacOS, and Linux.

## Work-in-progress
1. Snippet/template files
2. Improving build options.
