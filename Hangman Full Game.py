#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created on: Fri May  7 15:52:31 2021
@author: Chris Thompson
@pythonVersion: 3.8
    
@description: This is a script to create a game of hangman
"""
#####################################
#IMPORT MODULES
#####################################
import random
import requests
import tkinter as tk
import os
from threading import *

#####################################
#GLOBAL VARIABLES
#####################################
# initiate dictionary
data = {}

# Get the response from the API endpoint.
response = requests.get("https://bryandulaney.github.io/wordList.json")

# Return the JSON formatted infomration to our data dictionary
data = response.json()


#Lists that store our hangman figure
hangmanEasy = [ " ___________\n"
            "     |       | \n"
            "     |        \n"
           "     |         \n"
            "   |      \n"  
            "  |      \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n" ,
                " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |         \n"
            "   |      \n"  
            "  |      \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n" , 
          
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "    |       |\n"
            "   |      \n"  
            "  |      \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n" ,
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "    |      /|\n"
            "   |      \n"  
            "  |      \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n" ,
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\  \n"
            "   |      \n"  
            "  |      \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\  \n"
            "    |       |  \n"  
            "  |      \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       |  \n"  
            "    |        \ \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n" ,

            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
            " |       \n"
            "  |      \n"
     "_______| ________ \n",
     
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "     |    _/ \ \n" 
            " |       \n"
            "  |      \n"
     "_______| ________ \n",
     
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "      |   _/ \_ \n" 
            " |       \n"
            "  |      \n"
     "_______| ________ \n",
     
            " ___________\n"
            "  |         | \n"
            "   |        O \n"
           "   |       /|\/ \n"
            "  |         | \n"  
            "    |     _/ \_ \n" 
            "     |     GAME  \n"
            "    |      OVER! \n"
     "_______| ____________ \n"]

hangmanHard = [ " ___________\n"
            "     |       | \n"
            "     |        \n"
           "     |         \n"
            "   |      \n"  
            "  |      \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n" ,
                " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |         \n"
            "   |      \n"  
            "  |      \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n" , 
          
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "    |       |\n"
            "   |      \n"  
            "  |      \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n" ,
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "    |      /|\n"
            "   |      \n"  
            "  |      \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n" ,
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\  \n"
            "   |      \n"  
            "  |      \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\  \n"
            "    |       |  \n"  
            "  |      \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       |  \n"  
            "    |        \ \n "    
            " |      \n"
            "  |      \n"
     "_______| ________ \n" ,

            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
               "     |  GAME  \n"
            "    |      OVER! \n"
     "_______| ____________ \n"]

hangmanExtreme = [ " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "     |   ---------- \n"
            "    |       20 \n"
     "________| _________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "     | ---------- \n"
            "    |       19 \n"
     "_______| ____________ \n",
     " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ---------- \n"
            "    |       18 \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------\n"
            "    |       17 \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ---------- \n"
            "    |       16 \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------\n"
            "    |       15 \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------- \n"
            "    |       14 \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------\n"
            "    |       13 \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------\n"
            "    |       12 \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------- \n"
            "    |       11 \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------\n"
            "    |       10 \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------\n"
            "    |       9  \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ---------- \n"
            "    |       8  \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------\n"
            "    |       7  \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ---------- \n"
            "    |       6  \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------\n"
            "    |       5  \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------\n"
            "    |       4  \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------\n"
            "    |       3  \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------\n"
            "    |       2  \n"
     "_______| ____________ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
                "      | ----------   \n"
            "    |      LAST \n"
     "_______| ______MOVE_ \n",
            " ___________\n"
            "     |      | \n"
            "     |      O \n"
           "     |     /|\ \n"
            "    |       | \n"  
            "    |      / \ \n" 
               "     |  GAME  \n"
            "    |     OVER! \n"
     "_______| ____________ \n"]
      
#List of options when spinning the wheel
wheel = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, "L", "L", "B"]
#A list storing the different in-game display options
fortune = ["Each letter is worth:\n"
           "\n"
           "           /|         \n"
           "          / |         \n"
           "            |         \n"
           "            |         \n"
           "            |         \n"
           "            |         \n"
           "            |         \n"
           "            __|__ point\n",
           "Each letter is worth:\n"
           "\n"
           "           ___        \n"
           "         /     |      \n"
           "               |      \n"
           "              /       \n"
           "             /        \n"
           "            /         \n"
           "           |          \n"
           "              |___ points\n",
           "Each letter is worth:\n"
           "\n"
           "           ___        \n"
           "         /    |       \n"
           "              |       \n"
           "          ___/        \n"
           "             \        \n"
           "             |        \n"
           "             |        \n"
           "         \___/ points \n",
           "Each letter is worth:\n"
           "\n"
           "                     \n"
           "       |       |     \n"
           "       |       |     \n"
           "        | ___ |      \n"
           "              |      \n"
           "              |      \n"
           "              |      \n"
           "               | points\n",
           "Each letter is worth:\n"
           "\n"
           "          ____      \n"
           "         |          \n"
           "         |          \n"
           "          |___      \n"
           "              \     \n"
           "              |     \n"
           "              |     \n"
           "           ___/ points \n",
           "Each letter is worth:\n"
           "\n"
           "          ____      \n"
           "        |      |    \n"
           "        |           \n"
           "        | ___       \n"
           "        |     \     \n"
           "        |     |     \n"
           "        |     |     \n"
           "        \ ___ / points \n",
           "Each letter is worth:\n"
           "\n"
           "   _____           \n"
           "         |          \n"
           "         |          \n"
           "         |          \n"
           "         |          \n"
           "         |          \n"
           "         |          \n"
           "          |   points\n",
           "Each letter is worth:\n"
           "\n"
           "          ___       \n"
           "       |       \     \n"
           "       |       |     \n"
           "        \ ___ /     \n"
           "        /     \     \n"
           "        |     |     \n"
           "        |     |     \n"
           "           \___/ points\n",
           "Each letter is worth:\n"
           "\n"
           "          ___       \n"
           "      |        \   \n"
           "      |        |   \n"
           "       \  ___  /    \n"
           "               \    \n"
           "               |    \n"
           "               |    \n"
           "                | points\n",
           "Each letter is worth:\n"
           "\n"
           "        ___     \n"
           "   /| /     \  \n"
           "  / |  |   |    \n"
           "    |  |   |    \n"
           "    |  |   |    \n"
           "    |  |   |    \n"
           "    |  |   |    \n"
           "      __|__\__/  points\n",
           "     OH NO!   \n"
           "\n"
           "  You lost a turn!\n"
           "              \n"
           "    |   |     \n"
           "     ___       \n"
           "   /    \     \n"
           "             \n"
           "            \n"
           "            \n",
           "     OH NO!   \n"
           "\n"
           "  You went bankrupt!\n"
           "              \n"
           "    |   |     \n"
           "     ___       \n"
           "    /   \      \n"
           "               \n"
           "  You lose a turn and \n"
           "  all of your points. \n"]
#####################################
#USER-DEFINED FUNCTIONS
#####################################
#Check if the file exists
def fileExists(filePath):
    exists = os.path.exists(filePath)
    return exists
#Write the file to the file path
def writeFile(filePath, textToWrite):
    fileHandle = open(filePath, 'w')
    fileHandle.write(textToWrite)
    fileHandle.close()
#Read the file if it exists
def readFile(filePath):
    if not fileExists(filePath):
        print('The file, ' + filePath + ' does not exist - cannot read it.')
        return ''

    fileHandle = open(filePath, 'r')
    data = fileHandle.read()
    fileHandle.close()
    return data
#Creates the single player game window
def threadingSingle():
    tSingle = Thread(target = singleMenu)
    tSingle.start()
#Creates the multiplayer menu to choose a game mode    
def multiMenu():
    head.destroy()
    single.destroy()
    multi.destroy()
    
    multiMain = Label(root, text = 'Choose a multiplayer mode:' , font='arial 20 bold', bg = 'PaleTurquoise1').pack()
#Creates the multiplayer game window
def threadingMulti():
    tMulti = Thread(target = multiMenu)
    tMulti.start()

#####################################
#CLASSES
#####################################
#The main menu to choose what game mode to play
class MainMenu(tk.Tk):
    #Sets up the frame and label and buttons for the main menu
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.foo = None
        self.label1 = tk.Label(self.frame, text = 'Choose a game mode:' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label1.pack()
        self.button1 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Single Player'  ,padx =5,bg ='LightCyan3' ,command = self.singlePlayerMenu)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Multiplayer'  ,padx =5,bg ='LightCyan3' ,command = self.multiplayerMenu)
        self.button2.pack()
        self.button3 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Exit'  ,padx =5,bg ='LightCyan3' ,command = self.exit)
        self.button3.pack()
        self.frame.pack()
    #Label and buttons for choosing difficulty for single player mode
    def singlePlayerMenu(self):
        self.label1.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.label2 = tk.Label(self.frame, text = 'Choose a difficulty:' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label2.pack()
        self.button4 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Easy'  ,padx =5,bg ='LightCyan3' ,command = self.easySingle)
        self.button4.pack()
        self.button5 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Hard'  ,padx =5,bg ='LightCyan3' ,command = self.hardSingle)
        self.button5.pack()
        self.button6 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Extreme'  ,padx =5,bg ='LightCyan3' ,command = self.extremeSingle)
        self.button6.pack()
        self.button7 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Back'  ,padx =5,bg ='LightCyan3' ,command = self.mainMenu)
        self.button7.pack()
        self.button8 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Exit'  ,padx =5,bg ='LightCyan3' ,command = self.exit)
        self.button8.pack()
    #Label and buttons for choosing multiplayer mode    
    def multiplayerMenu(self):
        self.label1.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.label2 = tk.Label(self.frame, text = 'Choose a multiplayer mode:' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label2.pack()
        self.button4 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Traditional Hangman'  ,padx =5,bg ='LightCyan3' ,command = self.multiplayer)
        self.button4.pack()
        self.button5 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Wheel of Fortune'  ,padx =5,bg ='LightCyan3' ,command = self.wheelOfFortune)
        self.button5.pack()
        self.button6 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Back'  ,padx =5,bg ='LightCyan3' ,command = self.mainMenu)
        self.button6.pack()
        self.button7 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Exit'  ,padx =5,bg ='LightCyan3' ,command = self.exit)
        self.button7.pack()
    #A repeat of the __init__() function to be activated by back button    
    def mainMenu(self):
        self.label2.destroy()
        self.button4.destroy()
        self.button5.destroy()
        self.button6.destroy()
        self.button7.destroy()
        try:
            self.button8.destroy()
        except:
            None
        
        self.label1 = tk.Label(self.frame, text = 'Choose a game mode:' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label1.pack()
        self.button1 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Single Player'  ,padx =5,bg ='LightCyan3' ,command = self.singlePlayerMenu)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Multiplayer'  ,padx =5,bg ='LightCyan3' ,command = self.multiplayerMenu)
        self.button2.pack()
        self.button3 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Exit'  ,padx =5,bg ='LightCyan3' ,command = self.exit)
        self.button3.pack()
    #Creates the window for easy mode for single player
    def easySingle(self):
        self.easySingle = tk.Toplevel(self.master)
        self.easySingle.geometry('1000x700')
        self.easySingle.resizable(0,0)
        self.easySingle.title("Thompson-Hangman")
        self.easySingle.config(bg ='LightCyan2')
        
        self.app = EasyMode(self.easySingle)
    #Creates the window for hard mode for single player
    def hardSingle(self):
        self.hardSingle = tk.Toplevel(self.master)
        self.hardSingle.geometry('1000x700')
        self.hardSingle.resizable(0,0)
        self.hardSingle.title("Thompson-Hangman")
        self.hardSingle.config(bg ='LightCyan2')
        
        self.app = HardMode(self.hardSingle)
    #Creates the window for hard mode for single player
    def extremeSingle(self):
        self.extremeSingle = tk.Toplevel(self.master)
        self.extremeSingle.geometry('1000x700')
        self.extremeSingle.resizable(0,0)
        self.extremeSingle.title("Thompson-Hangman")
        self.extremeSingle.config(bg ='LightCyan2')
        
        self.app = ExtremeMode(self.extremeSingle)
    #Creates the window for two player mode
    def multiplayer(self):
        self.multiplayer = tk.Toplevel(self.master)
        self.multiplayer.geometry('1000x700')
        self.multiplayer.resizable(0,0)
        self.multiplayer.title("Thompson-Hangman")
        self.multiplayer.config(bg ='LightCyan2')
        
        self.app = TwoPlay(self.multiplayer)
    #Creates the window for wheel of fortune mode
    def wheelOfFortune(self):
        self.wheelOfFortune = tk.Toplevel(self.master)
        self.wheelOfFortune.geometry('1000x700')
        self.wheelOfFortune.resizable(0,0)
        self.wheelOfFortune.title("Thompson-Hangman")
        self.wheelOfFortune.config(bg ='LightCyan2')
        
        self.app = Wheel(self.wheelOfFortune)
    #Exit the system
    def exit(self):
        self.master.destroy()
#Creates the game for single player easy mode        
class EasyMode(tk.Frame):
    #Set up the frame and game buttons
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg ='LightCyan2', width = 1000, height = 700)
        self.label1 = tk.Label(self.frame, text = 'Hangman' , font='arial 20 bold')
        self.label1.place(x=500, y=15)
        self.label2 = tk.Label(self.frame, text = "Score:", font='arial 15 bold')
        self.label2.place(x = 400,y=50)
        self.points = tk.StringVar()
        self.label3 = tk.Label(self.frame, textvariable = self.points, font='arial 15 bold')
        self.label3.place(x = 475,y=50)
        self.label4 = tk.Label(self.frame, text = "High Score:", font='arial 15 bold', bg = 'seashell2')
        self.label4.place(x = 400,y=85)
        self.highScore = tk.StringVar()
        self.label5 = tk.Label(self.frame, textvariable = self.highScore, font='arial 15 bold', bg = 'seashell2')
        self.label5.place(x = 525,y=85)
        self.name = tk.StringVar()
        self.label6 = tk.Label(self.frame, font = 'arial 15 bold', textvariable = self.name, bg ='antiquewhite2')
        self.label6.place(x=25, y = 40)
        
        self.directions = tk.StringVar()
        self.entry1 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.directions, bg ='antiquewhite2',width = 50,)
        self.entry1.place(x=25, y = 70)
        self.directions.set("Press NEW GAME to begin.")
        self.entry = tk.StringVar()
        self.entry2 = tk.Entry(self.frame, font = 'arial 15', textvariable = self.entry , bg = 'antiquewhite2')
        self.entry2.place(x=25, y = 90)
        self.text = tk.StringVar()
        self.entry3 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.text, bg ='antiquewhite2',width = 60)
        self.entry3.place(x=25, y = 275)
        self.label7 = tk.Label(self.frame, text = "Current category:", font='arial 12 bold', bg = 'seashell2')
        self.label7.place(x = 25,y=300)
        self.currentCategory = tk.StringVar()
        self.label8 = tk.Label(self.frame, textvariable = self.currentCategory, font='arial 12 bold', bg = 'seashell2')
        self.label8.place(x = 210,y=300)
        self.label9 = tk.Label(self.frame, text = "Letters guessed:", font='arial 12 bold', bg = 'seashell2')
        self.label9.place(x = 25,y=325)
        self.letterBank = tk.StringVar()
        self.label10 = tk.Label(self.frame, textvariable = self.letterBank, font='arial 12 bold', bg = 'seashell2')
        self.label10.place(x = 210,y=325)
        self.label11 = tk.Label(self.frame, text = "Guesses left:", font='arial 12 bold', bg = 'seashell2')
        self.label11.place(x = 25,y=350)
        self.guesses = tk.StringVar()
        self.label12 = tk.Label(self.frame, textvariable = self.guesses, font='arial 12 bold', bg = 'seashell2')
        self.label12.place(x = 210,y=350)
        self.person = tk.StringVar()
        self.label13 = tk.Label(self.frame, font = 'arial 10 bold', textvariable = self.person, bg ='antiquewhite2',width = 60)
        self.label13.place(x=25, y = 380, height = 200)
        self.current = tk.StringVar()
        self.entry4 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.current, bg ='antiquewhite2',width = 60)
        self.entry4.place(x=25, y = 590)
        self.label14 = tk.Label(self.frame, text = "Answer:", font='arial 15 bold', bg = 'seashell2')
        self.label14.place(x = 25,y=615)
        self.answer = tk.StringVar()
        self.label15 = tk.Label(self.frame, textvariable = self.answer, font='arial 15 bold', bg = 'seashell2')
        self.label15.place(x = 120,y=615)
        self.categoryList = tk.Text(self.frame, height = 100, width = 50)
        self.button10 = tk.Button(self.frame, font = 'arial 13 bold', text = 'NEW GAME'  ,padx =5,bg ='LightCyan3' ,command = self.threading1)
        self.button10.place(x=25,y=150)
        self.button11 = tk.Button(self.frame, font = 'arial 13 bold', text = 'ENTER NAME'  ,padx =5,bg ='LightCyan3' ,command = self.threading2)
        self.button11.place(x=25,y=190)
        self.button12 = tk.Button(self.frame, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='LightCyan3' ,command = self.threading3)
        self.button12.place(x=25,y=230)
        self.button13 = tk.Button(self.frame, font = 'arial 13 bold', text = 'GUESS'  ,padx =5,bg ='LightCyan3' ,command = self.guess)
        self.button13.place(x=225,y=150)
        self.button14 = tk.Button(self.frame, font = 'arial 13 bold', text = 'LETTER'  ,padx =5,bg ='LightCyan3' ,command = self.threading5)
        self.button14.place(x=225,y=190)
        self.button15 = tk.Button(self.frame, font = 'arial 13 bold', text = 'WORD'  ,padx =5,bg ='LightCyan3' ,command = self.threading6)
        self.button15.place(x=225,y=230)
        self.button16 = tk.Button(self.frame, font = 'arial 13 bold', text = 'MAIN MENU'  ,padx =5,bg ='LightCyan2' ,command = self.mainMenu)
        self.button16.place(x=25,y=650)
        self.button17 = tk.Button(self.frame, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='LightCyan2' ,command = self.exit)
        self.button17.place(x=900,y=650)
        
        #Separate Entry texts for each category in order to display them one above the other
        self.label16 = tk.Label(self.frame, font = 'arial 10 bold', text = "List of categories:", bg ='LightCyan2')
        self.label16.place(x=700, y = 30)
        self.countries = tk.StringVar()
        self.entry5 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.countries, bg ='LightCyan2',width = 40,)
        self.entry5.place(x=700, y = 50)
        self.fruit = tk.StringVar()
        self.entry6 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.fruit, bg ='LightCyan2',width = 40,)
        self.entry6.place(x=700, y = 70)
        self.elements = tk.StringVar()
        self.entry7 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.elements, bg ='LightCyan2',width = 40,)
        self.entry7.place(x=700, y = 90)
        self.mammals = tk.StringVar()
        self.entry8 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.mammals, bg ='LightCyan2',width = 40,)
        self.entry8.place(x=700, y = 110)
        self.dinosaurs = tk.StringVar()
        self.entry9 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.dinosaurs, bg ='LightCyan2',width = 40,)
        self.entry9.place(x=700, y = 130)
        self.insects = tk.StringVar()
        self.entry10 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.insects, bg ='LightCyan2',width = 40,)
        self.entry10.place(x=700, y = 150)
        self.herbs = tk.StringVar()
        self.entry11 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.herbs, bg ='LightCyan2',width = 40,)
        self.entry11.place(x=700, y = 170)
        self.science = tk.StringVar()
        self.entry12 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.science, bg ='LightCyan2',width = 40,)
        self.entry12.place(x=700, y = 190)
        self.chemicals = tk.StringVar()
        self.entry13 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.chemicals, bg ='LightCyan2',width = 40,)
        self.entry13.place(x=700, y = 210)
        self.states = tk.StringVar()
        self.entry14 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.states, bg ='LightCyan2',width = 40,)
        self.entry14.place(x=700, y = 230)
        self.cities = tk.StringVar()
        self.entry15 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.cities, bg ='LightCyan2',width = 40,)
        self.entry15.place(x=700, y = 250)
        self.figures = tk.StringVar()
        self.entry16 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.figures, bg ='LightCyan2',width = 40,)
        self.entry16.place(x=700, y = 250)
        
        #These are the labels to show the list of categories
        self.label17 = tk.Label(self.frame, font = 'arial 10 bold', text = "List of categories:", bg ='LightCyan2',width = 40,)
        self.label17.place(x=700, y = 30)
        self.countries = tk.StringVar()
        self.entry17 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.countries, bg ='LightCyan2',width = 40,)
        self.entry17.place(x=700, y = 50)
        self.fruit = tk.StringVar()
        self.entry18 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.fruit, bg ='LightCyan2',width = 40,)
        self.entry18.place(x=700, y = 70)
        self.elements = tk.StringVar()
        self.entry19 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.elements, bg ='LightCyan2',width = 40,)
        self.entry19.place(x=700, y = 90)
        self.mammals = tk.StringVar()
        self.entry20 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.mammals, bg ='LightCyan2',width = 40,)
        self.entry20.place(x=700, y = 110)
        self.dinosaurs = tk.StringVar()
        self.entry21 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.dinosaurs, bg ='LightCyan2',width = 40,)
        self.entry21.place(x=700, y = 130)
        self.insects = tk.StringVar()
        self.entry22 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.insects, bg ='LightCyan2',width = 40,)
        self.entry22.place(x=700, y = 150)
        self.herbs = tk.StringVar()
        self.entry23 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.herbs, bg ='LightCyan2',width = 40,)
        self.entry23.place(x=700, y = 170)
        self.science = tk.StringVar()
        self.entry24 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.science, bg ='LightCyan2',width = 40,)
        self.entry24.place(x=700, y = 190)
        self.chemicals = tk.StringVar()
        self.entry25 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.chemicals, bg ='LightCyan2',width = 40,)
        self.entry25.place(x=700, y = 210)
        self.states = tk.StringVar()
        self.entry26 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.states, bg ='LightCyan2',width = 40,)
        self.entry26.place(x=700, y = 230)
        self.cities = tk.StringVar()
        self.entry27 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.cities, bg ='LightCyan2',width = 40,)
        self.entry27.place(x=700, y = 250)
        self.figures = tk.StringVar()
        self.entry28 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.figures, bg ='LightCyan2',width = 40,)
        self.entry28.place(x=700, y = 270)
        self.countries.set("'c' - countries")
        self.fruit.set("'f' - fruits & vegetables")
        self.elements.set("'e' - periodic elements")
        self.mammals.set("'m' - mammals")
        self.dinosaurs.set("'d' - dinosaurs")
        self.insects.set("'i' - insects")
        self.herbs.set("'h' - herbs & spices")
        self.science.set("'s' - science")
        self.chemicals.set("'a' - chemicals")
        self.states.set("'u' - U.S. states")
        self.cities.set("'w' - world cities")
        self.figures.set("'p' - historical figures")
        
        #Directions for how to use the buttons
        self.label18 = tk.Label(self.frame, font = 'arial 14 bold', text = "How to play:", bg ='LightCyan2',width = 40,)
        self.label18.place(x=500, y = 350)
        self.label19 = tk.Label(self.frame, font = 'arial 10 bold', text = "NEW GAME: Press this to begin a new game with a new user.", bg ='LightCyan2',width = 50,)
        self.label19.place(x=550, y = 380)
        self.label20 = tk.Label(self.frame, font = 'arial 10 bold', text = "ENTER NAME: Press this after you have typed a username.", bg ='LightCyan2',width = 50,)
        self.label20.place(x=550, y = 410)
        self.label21 = tk.Label(self.frame, font = 'arial 10 bold', text = "PLAY: Press this to begin a game or play again.", bg ='LightCyan2',width = 50,)
        self.label21.place(x=550, y = 440)
        self.label22 = tk.Label(self.frame, font = 'arial 10 bold', text = "GUESS: Press this after pressing PLAY to begin guessing.", bg ='LightCyan2',width = 50,)
        self.label22.place(x=550, y = 470)
        self.label23 = tk.Label(self.frame, font = 'arial 10 bold', text = "LETTER: After typing a letter, press this button to make a guess.", bg ='LightCyan2',width = 50,)
        self.label23.place(x=550, y = 500)
        self.label24 = tk.Label(self.frame, font = 'arial 10 bold', text = "WORD: After typing a word, press this button to make a guess.", bg ='LightCyan2',width = 50,)
        self.label24.place(x=550, y = 530)
        self.frame.pack()
        
    #This begins the game    
    def newGame(self):
        #Reset all text boxes
        self.entry.set("")
        self.directions.set("")
        self.text.set("")
        self.name.set("")
        #Set in tkinter
        self.directions.set("Please enter a username and press ENTER NAME:")
    #Thread to prevent the GUI from crashing
    def threading1(self):
        t1 = Thread(target = self.newGame)
        t1.start()
    #Creates username and checks if a file for it exists
    def user(self):
        #Set score and comboBonus variables here so they won't reset with a new game
        self.score = 0
        self.points.set(self.score)
        self.comboBonus = 0
        #Display username in tkinter
        self.userName = self.entry.get()
        self.userName = self.name.set(self.userName)
        
        #Save the user's file based on their username
        self.DATA_FILE_PATH = f"{self.name.get()}Easy.txt"
        #Check if the file already exists
        if not fileExists(self.DATA_FILE_PATH):
            self.hiScore = 0
            self.highScore.set(self.hiScore)
            self.text.set("Welcome to easy mode! Press the PLAY button to begin.")
        else:
            self.savedDataString = readFile(self.DATA_FILE_PATH)
            self.savedDataList = self.savedDataString.split(',')
            self.userName = self.savedDataList[0]
            self.hiScore = self.savedDataList[1]
            self.hiScore = int(self.hiScore)
            self.highScore.set(self.hiScore)
            self.text.set("Welcome back! Press the PLAY button to begin.")
    #Thread to prevent the GUI from crashing  
    def threading2(self):
        t2 = Thread(target = self.user)
        t2.start()
    #Sets up the game with key lists/variables and has the player choose a category    
    def play(self):
        #Reset all text boxes
        self.entry.set("")
        self.directions.set("")
        self.text.set("")
        self.answer.set("")
        #List of all possible player choices
        self.choices = []
        self.choices.append("a")
        self.choices.append("b")
        self.choices.append("c")
        self.choices.append("d")
        self.choices.append("e")
        self.choices.append("f")
        self.choices.append("g")
        self.choices.append("h")
        self.choices.append("i")
        self.choices.append("j")
        self.choices.append("k")
        self.choices.append("l")
        self.choices.append("m")
        self.choices.append("n")
        self.choices.append("o")
        self.choices.append("p")
        self.choices.append("q")
        self.choices.append("r")
        self.choices.append("s")
        self.choices.append("t")
        self.choices.append("u")
        self.choices.append("v")
        self.choices.append("w")
        self.choices.append("x")
        self.choices.append("y")
        self.choices.append("z")
        #Number of guesses the user has
        self.guessCounter = 10
        self.guesses.set(self.guessCounter)
        # Prompt user to select category
        while True:
            # Return random word based on category selection    
            # assign variables for random dictionary value
            self.countries = random.choice(data['countries']).lower()
            self.fruitVeg = random.choice(data['fruitVeg']).lower()
            self.elements = random.choice(data['elements']).lower()
            self.mammals = random.choice(data['mammals']).lower()
            self.dinosaurs = random.choice(data['dinosaurs']).lower()
            self.insects = random.choice(data['insects']).lower()
            self.herbSpice = random.choice(data['herbSpice']).lower()
            self.science = random.choice(data['science']).lower()
            self.chemicals = random.choice(data['chemicals']).lower()
            self.usStates = random.choice(data['usStates']).lower()
            self.worldCities = random.choice(data['worldCities']).lower()
            self.people = random.choice(data['people']).lower()
            self.directions.set("Choose a category using the options to the right: ")
            
            self.category = self.entry.get()
            if self.category == 'c':
                self.randomWord = self.countries.lower()
                self.currentCategory.set("Countries")
                break
            elif self.category == 'f':
                self.randomWord = self.fruitVeg.lower()
                self.currentCategory.set("Fruits and Veggies")
                break
            elif self.category == 'e':
                self.randomWord = self.elements.lower()
                self.currentCategory.set("Periodic Elements")
                break
            elif self.category == 'm':
                self.randomWord = self.mammals.lower()
                self.currentCategory.set("Mammals")
                break
            elif self.category == 'd':
                self.randomWord = self.dinosaurs.lower()
                self.currentCategory.set("Dinosaurs")
                break
            elif self.category == 'i':
                self.randomWord = self.insects.lower()
                self.currentCategory.set("Insects")
                break
            elif self.category == 'h':
                self.randomWord = self.herbSpice.lower()
                self.currentCategory.set("Herbs and Spices")
                break
            elif self.category == 's':
                self.randomWord = self.science.lower()
                self.currentCategory.set("Science")
                break
            elif self.category == 'a':
                self.randomWord = self.chemicals.lower()
                self.currentCategory.set("Chemicals")
                break
            elif self.category == 'u':
                self.randomWord = self.usStates.lower()
                self.currentCategory.set("U.S. States")
                break
            elif self.category == 'w':
                self.randomWord = self.worldCities.lower()
                self.currentCategory.set("World Cities")
                break
            elif self.category == 'p':
                self.randomWord = self.people.lower()
                self.currentCategory.set("Historical Figures")
                break
                        
        self.directions.set("Word selected. Press the GUESS button to begin guessing.")
        #Clear the entry text
        self.entry.set("")
        self.word = self.randomWord
        #Empty list to store letters in the word.
        self.letters = []
        #Empty list to store letters that the player guesses
        self.lettersGuessed = []
        #Changes all letters in the word into an underscore symbol.
        for self.character in list(self.word):
            self.letters.append("_")
        #Change any spaces from an underscore back into a space
        for i in range(len(self.word)):
            self.character = self.word[i]
            if self.character == " ":
                self.letters[i] = self.word[i]    
        #Print out the underscores for the word joined by a space before each guess
        self.current.set("The current word is: " + " ".join(self.letters))
    #Thread to prevent the GUI from crashing
    def threading3(self):
        t3 = Thread(target = self.play)
        t3.start()
    #Player begins guessing by choosing what to guess
    def guess(self):
        self.entry.set("")
        self.text.set("")
        self.directions.set("Enter your guess then press LETTER or WORD.")
        if self.guessCounter == 10:
            self.person.set(hangmanEasy[0])
    #Player guesses a letter
    def letter(self):
        #Player guess input
        self.guess = self.entry.get()
        while True:
            #Break if user guesses a letter in the list of choices
            if self.guess in self.choices:
                break
            #Repeat input message if user guesses something not in the choices list
            else:
                self.text.set("You either guessed that letter, or you typed something else.")
                self.entry.set("")
                #self.directions.set("Press GUESS to guess again.")
        #For correct guess
        if self.guess.lower() in list(self.word):
             self.text.set("You are correct!")
             self.entry.set("")
             #self.directions.set("Press GUESS.")
             
             #Iterate through the word to change all instances of a correct
             #guess from underscores to the letter
             for i in range(len(self.word)):
                 self.character = self.word[i]
                 if self.character == self.guess:
                     self.letters[i] = self.word[i]
             #This adds to the user's score based on the number of times
             #the correct guess appears in the word
             self.addScore = self.letters.count(self.guess) * 2
             self.score = self.score + self.addScore
             self.points.set(self.score)
             self.userName = self.name.get()
             #Check for high score and save data
             if self.score > self.hiScore:
                 self.hiScore = self.score
                 self.highScore.set(self.hiScore)
                 self.text.set("You have a new high score!")
             else:
                 self.hiScore = self.hiScore
             self.dataList = [self.userName, str(self.hiScore)]
             self.outputText = ','.join(self.dataList)
             writeFile(self.DATA_FILE_PATH, self.outputText)
             self.current.set("The current word is: " + " ".join(self.letters))
        #Wrong guess
        else:
            self.text.set("Sorry, that letter is not in the word.")
            self.entry.set("")
            #self.directions.set("Press GUESS.")
            #Remove one from guessCounter and let user know number of guesses
            #remaining
            self.guessCounter -= 1
            self.guesses.set(self.guessCounter)
            #Print the hangman figure when player makes wrong guess
            if self.guessCounter == 10:
                self.person.set(hangmanEasy[0])
            elif self.guessCounter == 9:
                self.person.set(hangmanEasy[1])
            elif self.guessCounter == 8:
                self.person.set(hangmanEasy[2])
            elif self.guessCounter == 7:
                self.person.set(hangmanEasy[3])
            elif self.guessCounter == 6:
                self.person.set(hangmanEasy[4])
            elif self.guessCounter == 5:
                self.person.set(hangmanEasy[5])
            elif self.guessCounter == 4:
                self.person.set(hangmanEasy[6])
            elif self.guessCounter == 3:
                self.person.set(hangmanEasy[7])
            elif self.guessCounter == 2:
                self.person.set(hangmanEasy[8])
            elif self.guessCounter == 1:
                self.person.set(hangmanEasy[9])
            elif self.guessCounter == 0:
                self.person.set(hangmanEasy[10])
            #Check to see if game ends due to no more guesses left
            if self.guessCounter == 0:
                self.text.set("\nSorry, you did not guess the word in time.")
                self.answer.set(self.word)
                self.userName = self.name.get()
                if self.score > self.hiScore:
                    self.hiScore = self.score
                    self.highScore.set(self.hiScore)
                    self.text.set("You have a new high score!")
                else:
                    self.hiScore = self.hiScore
                self.dataList = [self.userName, str(self.hiScore)]
                self.outputText = ','.join(self.dataList)
                writeFile(self.DATA_FILE_PATH, self.outputText)
                self.score = 0
        #Remove the player's guess from the choices list so that it is no
        #longer an option
        self.choices.remove(self.guess)
        self.lettersGuessed.append(self.guess) 
        self.letterBank.set(sorted(self.lettersGuessed))
        #Check if game ends because player guessed all letters in the word
        if "_" not in self.letters:
            self.directions.set("You guessed the word! To play again press PLAY.")
            self.answer.set(self.word)
            #If player guesses 3 words in a row, get bonus points
            self.comboBonus = self.comboBonus + 1
            if self.comboBonus == 3:
                self.text.set("Nice job! You correctly guessed 3 words in a row.")
                self.score += 3
                #Reset the combo tracker back to 0
                self.comboBonus = 0
    #Thread to prevent the GUI from crashing
    def threading5(self):
        t5 = Thread(target = self.letter)
        t5.start()
    #Player guesses the word
    def wordguess(self):
        self.guess = self.entry.get()
        #If correct, add to player score and break loop
        if self.guess.lower() == self.word:
            self.directions.set("Correct! To play again press PLAY.")
            self.answer.set(self.word)
            self.score = self.score + 10
            self.points.set(self.score)
            self.userName = self.name.get()
            #Check for high score and save data
            if self.score > self.hiScore:
                self.hiScore = self.score
                self.highScore.set(self.hiScore)
                self.text.set("You have a new high score!")
            else:
                self.hiScore = self.hiScore
            self.dataList = [self.userName, str(self.hiScore)]
            self.outputText = ','.join(self.dataList)
            writeFile(self.DATA_FILE_PATH, self.outputText)
            #If player guesses 3 words in a row, get bonus points
            self.comboBonus = self.comboBonus + 1
            if self.comboBonus == 3:
                self.text.set("Nice job! You correctly guessed 3 words in a row.")
                self.score += 3
                self.points.set(self.score)
                self.score =self.score + self.addScore
                self.points.set(self.score)
                self.userName = self.name.get()
                #Check for high score and save data
                if self.score > self.hiScore:
                    self.hiScore = self.score
                    self.highScore.set(self.hiScore)
                    self.text.set("You have a new high score!")
                else:
                    self.hiScore = self.hiScore
                self.dataList = [self.userName, str(self.hiScore)]
                self.outputText = ','.join(self.dataList)
                writeFile(self.DATA_FILE_PATH, self.outputText)
                #Reset the combo tracker back to 0
                self.comboBonus = 0
            #If player guess incorrect
        else:
            self.text.set("Sorry, that's not the correct word or spelling.")
            self.guessCounter -= 1
            self.guesses.set(self.guessCounter)
            #Print the hangman figure when player makes wrong guess
            if self.guessCounter == 10:
                self.person.set(hangmanEasy[0])
            elif self.guessCounter == 9:
                self.person.set(hangmanEasy[1])
            elif self.guessCounter == 8:
                self.person.set(hangmanEasy[2])
            elif self.guessCounter == 7:
                self.person.set(hangmanEasy[3])
            elif self.guessCounter == 6:
                self.person.set(hangmanEasy[4])
            elif self.guessCounter == 5:
                self.person.set(hangmanEasy[5])
            elif self.guessCounter == 4:
                self.person.set(hangmanEasy[6])
            elif self.guessCounter == 3:
                self.person.set(hangmanEasy[7])
            elif self.guessCounter == 2:
                self.person.set(hangmanEasy[8])
            elif self.guessCounter == 1:
                self.person.set(hangmanEasy[9])
            elif self.guessCounter == 0:
                self.person.set(hangmanEasy[10])
            #Check if player has run out of guesses
            if self.guessCounter == 0:
                self.text.set("Sorry, you did not guess the word in time.")
                self.answer.set(self.word)
                self.userName = self.name.get()
                if self.score > self.hiScore:
                    self.hiScore = self.score
                    self.highScore.set(self.hiScore)
                    self.text.set("You have a new high score!")
                else:
                    self.hiScore = self.hiScore
                self.dataList = [self.userName, str(self.hiScore)]
                self.outputText = ','.join(self.dataList)
                writeFile(self.DATA_FILE_PATH, self.outputText)
                self.score = 0
    #Thread to prevent the GUI from crashing
    def threading6(self):
        t6 = Thread(target = self.wordguess)
        t6.start()
        
    #Take user back to main menu
    def mainMenu(self):
        self.master.destroy()
    #Exit the system
    def exit(self):
        root.destroy()

#Creates hard mode
class HardMode(EasyMode):
    #Creates username and checks if a file for it exists
    def user(self):
        #Set score and comboBonus variables here so they won't reset with a new game
        self.score = 0
        self.points.set(self.score)
        self.comboBonus = 0
        #Display username in tkinter
        self.userName = self.entry.get()
        self.userName = self.name.set(self.userName)
        
        #Save the user's file based on their username
        self.DATA_FILE_PATH = f"{self.name.get()}Hard.txt"
        #Check if the file already exists
        if not fileExists(self.DATA_FILE_PATH):
            self.hiScore = 0
            self.highScore.set(self.hiScore)
            self.text.set("Welcome to hard mode! Press the PLAY button to begin.")
        else:
            self.savedDataString = readFile(self.DATA_FILE_PATH)
            self.savedDataList = self.savedDataString.split(',')
            self.userName = self.savedDataList[0]
            self.hiScore = self.savedDataList[1]
            self.hiScore = int(self.hiScore)
            self.highScore.set(self.hiScore)
            self.text.set("Welcome back! Press the PLAY button to begin.")
    #Thread to prevent the GUI from crashing  
    def threading2(self):
        t2 = Thread(target = self.user)
        t2.start()
    #Sets up the game with key lists/variables and has the player choose a category    
    def play(self):
        #Reset all text boxes
        self.entry.set("")
        self.directions.set("")
        self.text.set("")
        self.answer.set("")
        #List of all possible player choices
        self.choices = []
        self.choices.append("a")
        self.choices.append("b")
        self.choices.append("c")
        self.choices.append("d")
        self.choices.append("e")
        self.choices.append("f")
        self.choices.append("g")
        self.choices.append("h")
        self.choices.append("i")
        self.choices.append("j")
        self.choices.append("k")
        self.choices.append("l")
        self.choices.append("m")
        self.choices.append("n")
        self.choices.append("o")
        self.choices.append("p")
        self.choices.append("q")
        self.choices.append("r")
        self.choices.append("s")
        self.choices.append("t")
        self.choices.append("u")
        self.choices.append("v")
        self.choices.append("w")
        self.choices.append("x")
        self.choices.append("y")
        self.choices.append("z")
        #Number of guesses the user has
        self.guessCounter = 7
        self.guesses.set(self.guessCounter)
        # Prompt user to select category
        while True:
            # Return random word based on category selection    
            # assign variables for random dictionary value
            self.countries = random.choice(data['countries']).lower()
            self.fruitVeg = random.choice(data['fruitVeg']).lower()
            self.elements = random.choice(data['elements']).lower()
            self.mammals = random.choice(data['mammals']).lower()
            self.dinosaurs = random.choice(data['dinosaurs']).lower()
            self.insects = random.choice(data['insects']).lower()
            self.herbSpice = random.choice(data['herbSpice']).lower()
            self.science = random.choice(data['science']).lower()
            self.chemicals = random.choice(data['chemicals']).lower()
            self.usStates = random.choice(data['usStates']).lower()
            self.worldCities = random.choice(data['worldCities']).lower()
            self.people = random.choice(data['people']).lower()
            self.directions.set("Choose a category using the options to the right: ")
            
            self.category = self.entry.get()
            if self.category == 'c':
                self.randomWord = self.countries.lower()
                self.currentCategory.set("Countries")
                break
            elif self.category == 'f':
                self.randomWord = self.fruitVeg.lower()
                self.currentCategory.set("Fruits and Veggies")
                break
            elif self.category == 'e':
                self.randomWord = self.elements.lower()
                self.currentCategory.set("Periodic Elements")
                break
            elif self.category == 'm':
                self.randomWord = self.mammals.lower()
                self.currentCategory.set("Mammals")
                break
            elif self.category == 'd':
                self.randomWord = self.dinosaurs.lower()
                self.currentCategory.set("Dinosaurs")
                break
            elif self.category == 'i':
                self.randomWord = self.insects.lower()
                self.currentCategory.set("Insects")
                break
            elif self.category == 'h':
                self.randomWord = self.herbSpice.lower()
                self.currentCategory.set("Herbs and Spices")
                break
            elif self.category == 's':
                self.randomWord = self.science.lower()
                self.currentCategory.set("Science")
                break
            elif self.category == 'a':
                self.randomWord = self.chemicals.lower()
                self.currentCategory.set("Chemicals")
                break
            elif self.category == 'u':
                self.randomWord = self.usStates.lower()
                self.currentCategory.set("U.S. States")
                break
            elif self.category == 'w':
                self.randomWord = self.worldCities.lower()
                self.currentCategory.set("World Cities")
                break
            elif self.category == 'p':
                self.randomWord = self.people.lower()
                self.currentCategory.set("Historical Figures")
                break
            #else:
             #   text.set("That was not a category option. Press PLAY again.")
        
        self.directions.set("Word selected. Press the GUESS button to begin guessing.")
        #Clear the entry text
        self.entry.set("")
        self.word = self.randomWord
        #Empty list to store letters in the word.
        self.letters = []
        #Empty list to store letters that the player guesses
        self.lettersGuessed = []
        #Changes all letters in the word into an underscore symbol.
        for self.character in list(self.word):
            self.letters.append("_")
        #Change any spaces from an underscore back into a space
        for i in range(len(self.word)):
            self.character = self.word[i]
            if self.character == " ":
                self.letters[i] = self.word[i]    
        #Print out the underscores for the word joined by a space before each guess
        self.current.set("The current word is: " + " ".join(self.letters))
    #Thread to prevent the GUI from crashing
    def threading3(self):
        t3 = Thread(target = self.play)
        t3.start()
    #Player begins guessing by choosing what to guess
    def guess(self):
        self.entry.set("")
        self.text.set("")
        self.directions.set("Enter your guess then press LETTER or WORD.")
        if self.guessCounter == 7:
            self.person.set(hangmanHard[0])
    #Player guesses a letter
    def letter(self):
        #Player guess input
        self.guess = self.entry.get()
        while True:
            #Break if user guesses a letter in the list of choices
            if self.guess in self.choices:
                break
            #Repeat input message if user guesses something not in the choices list
            else:
                self.text.set("You either guessed that letter, or you typed something else.")
                self.entry.set("")
                #self.directions.set("Press GUESS to guess again.")
        #For correct guess
        if self.guess.lower() in list(self.word):
             self.text.set("You are correct!")
             self.entry.set("")
             #self.directions.set("Press GUESS.")
             
             #Iterate through the word to change all instances of a correct
             #guess from underscores to the letter
             for i in range(len(self.word)):
                 self.character = self.word[i]
                 if self.character == self.guess:
                     self.letters[i] = self.word[i]
             #This adds to the user's score based on the number of times
             #the correct guess appears in the word
             self.addScore = self.letters.count(self.guess) * 2
             self.score = self.score + self.addScore
             self.points.set(self.score)
             self.userName = self.name.get()
             #Check for high score and save data
             if self.score > self.hiScore:
                 self.hiScore = self.score
                 self.highScore.set(self.hiScore)
                 self.text.set("You have a new high score!")
             else:
                 self.hiScore = self.hiScore
             self.dataList = [self.userName, str(self.hiScore)]
             self.outputText = ','.join(self.dataList)
             writeFile(self.DATA_FILE_PATH, self.outputText)
             self.current.set("The current word is: " + " ".join(self.letters))
        #Wrong guess
        else:
            self.text.set("Sorry, that letter is not in the word.")
            self.entry.set("")
            #Lose points for wrong guess
            self.score = self.score - 1
            self.points.set(self.score)
            #Remove one from guessCounter and let user know number of guesses
            #remaining
            self.guessCounter -= 1
            self.guesses.set(self.guessCounter)
            #Print the hangman figure when player makes wrong guess
            if self.guessCounter == 7:
                self.person.set(hangmanHard[0])
            elif self.guessCounter == 6:
                self.person.set(hangmanHard[1])
            elif self.guessCounter == 5:
                self.person.set(hangmanHard[2])
            elif self.guessCounter == 4:
                self.person.set(hangmanHard[3])
            elif self.guessCounter == 3:
                self.person.set(hangmanHard[4])
            elif self.guessCounter == 2:
                self.person.set(hangmanHard[5])
            elif self.guessCounter == 1:
                self.person.set(hangmanHard[6])
            elif self.guessCounter == 0:
                self.person.set(hangmanHard[7])
            #Check to see if game ends due to no more guesses left
            if self.guessCounter == 0:
                self.text.set("\nSorry, you did not guess the word in time.")
                self.answer.set(self.word)
                self.userName = self.name.get()
                if self.score > self.hiScore:
                    self.hiScore = self.score
                    self.highScore.set(self.hiScore)
                    self.text.set("You have a new high score!")
                else:
                    self.hiScore = self.hiScore
                self.dataList = [self.userName, str(self.hiScore)]
                self.outputText = ','.join(self.dataList)
                writeFile(self.DATA_FILE_PATH, self.outputText)
                self.score = 0
        #Remove the player's guess from the choices list so that it is no
        #longer an option
        self.choices.remove(self.guess)
        self.lettersGuessed.append(self.guess) 
        self.letterBank.set(sorted(self.lettersGuessed))
        #Check if game ends because player guessed all letters in the word
        if "_" not in self.letters:
            self.directions.set("You guessed the word! To play again press PLAY.")
            self.answer.set(self.word)
            #If player guesses 3 words in a row, get bonus points
            self.comboBonus = self.comboBonus + 1
            if self.comboBonus == 3:
                self.text.set("Nice job! You correctly guessed 3 words in a row.")
                self.score += 3
                #Reset the combo tracker back to 0
                self.comboBonus = 0
    #Thread to prevent the GUI from crashing
    def threading5(self):
        t5 = Thread(target = self.letter)
        t5.start()
    #Player guesses the word
    def wordguess(self):
        self.guess = self.entry.get()
        #If correct, add to player score and break loop
        if self.guess.lower() == self.word:
            self.directions.set("Correct! To play again press PLAY.")
            self.answer.set(self.word)
            self.score = self.score + 10
            self.points.set(self.score)
            self.userName = self.name.get()
            #Check for high score and save data
            if self.score > self.hiScore:
                self.hiScore = self.score
                self.highScore.set(self.hiScore)
                self.text.set("You have a new high score!")
            else:
                self.hiScore = self.hiScore
            self.dataList = [self.userName, str(self.hiScore)]
            self.outputText = ','.join(self.dataList)
            writeFile(self.DATA_FILE_PATH, self.outputText)
            #If player guesses 3 words in a row, get bonus points
            self.comboBonus = self.comboBonus + 1
            if self.comboBonus == 3:
                self.text.set("Nice job! You correctly guessed 3 words in a row.")
                self.score += 3
                self.points.set(self.score)
                self.score =self.score + self.addScore
                self.points.set(self.score)
                self.userName = self.name.get()
                #Check for high score and save data
                if self.score > self.hiScore:
                    self.hiScore = self.score
                    self.highScore.set(self.hiScore)
                    self.text.set("You have a new high score!")
                else:
                    self.hiScore = self.hiScore
                self.dataList = [self.userName, str(self.hiScore)]
                self.outputText = ','.join(self.dataList)
                writeFile(self.DATA_FILE_PATH, self.outputText)
                #Reset the combo tracker back to 0
                self.comboBonus = 0
            #If player guess incorrect
        else:
            self.text.set("Sorry, that's not the correct word or spelling.")
            #Lose points for wrong guess
            self.score = self.score - 5
            self.points.set(self.score)
            self.guessCounter -= 1
            self.guesses.set(self.guessCounter)
            #Print the hangman figure when player makes wrong guess
            if self.guessCounter == 7:
                self.person.set(hangmanHard[0])
            elif self.guessCounter == 6:
                self.person.set(hangmanHard[1])
            elif self.guessCounter == 5:
                self.person.set(hangmanHard[2])
            elif self.guessCounter == 4:
                self.person.set(hangmanHard[3])
            elif self.guessCounter == 3:
                self.person.set(hangmanHard[4])
            elif self.guessCounter == 2:
                self.person.set(hangmanHard[5])
            elif self.guessCounter == 1:
                self.person.set(hangmanHard[6])
            elif self.guessCounter == 0:
                self.person.set(hangmanHard[7])
            #Check if player has run out of guesses
            if self.guessCounter == 0:
                self.text.set("Sorry, you did not guess the word in time.")
                self.answer.set(self.word)
                self.userName = self.name.get()
                if self.score > self.hiScore:
                    self.hiScore = self.score
                    self.highScore.set(self.hiScore)
                    self.text.set("You have a new high score!")
                else:
                    self.hiScore = self.hiScore
                self.dataList = [self.userName, str(self.hiScore)]
                self.outputText = ','.join(self.dataList)
                writeFile(self.DATA_FILE_PATH, self.outputText)
                self.score = 0
    #Thread to prevent the GUI from crashing
    def threading6(self):
        t6 = Thread(target = self.wordguess)
        t6.start()
        
    #Creates hard mode
class ExtremeMode(EasyMode):
    #Creates username and checks if a file for it exists
    def user(self):
        #Set score, comboBonus, and guessCounter variables here so they won't reset with a new game
        self.score = 0
        self.points.set(self.score)
        self.comboBonus = 0
        self.guessCounter = 20
        self.guesses.set(self.guessCounter)
        #Display username in tkinter
        self.userName = self.entry.get()
        self.userName = self.name.set(self.userName)
        
        #Save the user's file based on their username
        self.DATA_FILE_PATH = f"{self.name.get()}Extreme.txt"
        #Check if the file already exists
        if not fileExists(self.DATA_FILE_PATH):
            self.hiScore = 0
            self.highScore.set(self.hiScore)
            self.text.set("Welcome to extreme mode! Press the PLAY button to begin.")
        else:
            self.savedDataString = readFile(self.DATA_FILE_PATH)
            self.savedDataList = self.savedDataString.split(',')
            self.userName = self.savedDataList[0]
            self.hiScore = self.savedDataList[1]
            self.hiScore = int(self.hiScore)
            self.highScore.set(self.hiScore)
            self.text.set("Welcome back! Press the PLAY button to begin.")
    #Thread to prevent the GUI from crashing  
    def threading2(self):
        t2 = Thread(target = self.user)
        t2.start()
    #Sets up the game with key lists/variables and has the player choose a category    
    def play(self):
        #Reset all text boxes
        self.entry.set("")
        self.directions.set("")
        self.text.set("")
        self.answer.set("")
        #List of all possible player choices
        self.choices = []
        self.choices.append("a")
        self.choices.append("b")
        self.choices.append("c")
        self.choices.append("d")
        self.choices.append("e")
        self.choices.append("f")
        self.choices.append("g")
        self.choices.append("h")
        self.choices.append("i")
        self.choices.append("j")
        self.choices.append("k")
        self.choices.append("l")
        self.choices.append("m")
        self.choices.append("n")
        self.choices.append("o")
        self.choices.append("p")
        self.choices.append("q")
        self.choices.append("r")
        self.choices.append("s")
        self.choices.append("t")
        self.choices.append("u")
        self.choices.append("v")
        self.choices.append("w")
        self.choices.append("x")
        self.choices.append("y")
        self.choices.append("z")
        # Prompt user to select category
        while True:
            # Return random word based on category selection    
            # assign variables for random dictionary value
            self.countries = random.choice(data['countries']).lower()
            self.fruitVeg = random.choice(data['fruitVeg']).lower()
            self.elements = random.choice(data['elements']).lower()
            self.mammals = random.choice(data['mammals']).lower()
            self.dinosaurs = random.choice(data['dinosaurs']).lower()
            self.insects = random.choice(data['insects']).lower()
            self.herbSpice = random.choice(data['herbSpice']).lower()
            self.science = random.choice(data['science']).lower()
            self.chemicals = random.choice(data['chemicals']).lower()
            self.usStates = random.choice(data['usStates']).lower()
            self.worldCities = random.choice(data['worldCities']).lower()
            self.people = random.choice(data['people']).lower()
            self.directions.set("Choose a category using the options to the right: ")
            
            self.category = self.entry.get()
            if self.category == 'c':
                self.randomWord = self.countries.lower()
                self.currentCategory.set("Countries")
                break
            elif self.category == 'f':
                self.randomWord = self.fruitVeg.lower()
                self.currentCategory.set("Fruits and Veggies")
                break
            elif self.category == 'e':
                self.randomWord = self.elements.lower()
                self.currentCategory.set("Periodic Elements")
                break
            elif self.category == 'm':
                self.randomWord = self.mammals.lower()
                self.currentCategory.set("Mammals")
                break
            elif self.category == 'd':
                self.randomWord = self.dinosaurs.lower()
                self.currentCategory.set("Dinosaurs")
                break
            elif self.category == 'i':
                self.randomWord = self.insects.lower()
                self.currentCategory.set("Insects")
                break
            elif self.category == 'h':
                self.randomWord = self.herbSpice.lower()
                self.currentCategory.set("Herbs and Spices")
                break
            elif self.category == 's':
                self.randomWord = self.science.lower()
                self.currentCategory.set("Science")
                break
            elif self.category == 'a':
                self.randomWord = self.chemicals.lower()
                self.currentCategory.set("Chemicals")
                break
            elif self.category == 'u':
                self.randomWord = self.usStates.lower()
                self.currentCategory.set("U.S. States")
                break
            elif self.category == 'w':
                self.randomWord = self.worldCities.lower()
                self.currentCategory.set("World Cities")
                break
            elif self.category == 'p':
                self.randomWord = self.people.lower()
                self.currentCategory.set("Historical Figures")
                break
            #else:
             #   text.set("That was not a category option. Press PLAY again.")
        
        self.directions.set("Word selected. Press the GUESS button to begin guessing.")
        #Clear the entry text
        self.entry.set("")
        self.word = self.randomWord
        #Empty list to store letters in the word.
        self.letters = []
        #Empty list to store letters that the player guesses
        self.lettersGuessed = []
        #Changes all letters in the word into an underscore symbol.
        for self.character in list(self.word):
            self.letters.append("_")
        #Change any spaces from an underscore back into a space
        for i in range(len(self.word)):
            self.character = self.word[i]
            if self.character == " ":
                self.letters[i] = self.word[i]    
        #Print out the underscores for the word joined by a space before each guess
        self.current.set("The current word is: " + " ".join(self.letters))
    #Thread to prevent the GUI from crashing
    def threading3(self):
        t3 = Thread(target = self.play)
        t3.start()
    #Player begins guessing by choosing what to guess
    def guess(self):
        self.entry.set("")
        self.text.set("")
        self.directions.set("Enter your guess then press LETTER or WORD.")
        if self.guessCounter == 20:
            self.person.set(hangmanExtreme[0])
    #Player guesses a letter
    def letter(self):
        #Player guess input
        self.guess = self.entry.get()
        while True:
            #Break if user guesses a letter in the list of choices
            if self.guess in self.choices:
                break
            #Repeat input message if user guesses something not in the choices list
            else:
                self.text.set("You either guessed that letter, or you typed something else.")
                self.entry.set("")
                #self.directions.set("Press GUESS to guess again.")
        #For correct guess
        if self.guess.lower() in list(self.word):
             self.text.set("You are correct!")
             self.entry.set("")
             #self.directions.set("Press GUESS.")
             
             #Iterate through the word to change all instances of a correct
             #guess from underscores to the letter
             for i in range(len(self.word)):
                 self.character = self.word[i]
                 if self.character == self.guess:
                     self.letters[i] = self.word[i]
             #This adds to the user's score based on the number of times
             #the correct guess appears in the word
             self.addScore = self.letters.count(self.guess) * 2
             self.score = self.score + self.addScore
             self.points.set(self.score)
             self.userName = self.name.get()
             #Check for high score and save data
             if self.score > self.hiScore:
                 self.hiScore = self.score
                 self.highScore.set(self.hiScore)
                 self.text.set("You have a new high score!")
             else:
                 self.hiScore = self.hiScore
             self.dataList = [self.userName, str(self.hiScore)]
             self.outputText = ','.join(self.dataList)
             writeFile(self.DATA_FILE_PATH, self.outputText)
             self.current.set("The current word is: " + " ".join(self.letters))
        #Wrong guess
        else:
            self.text.set("Sorry, that letter is not in the word.")
            self.entry.set("")
            #Lose points for wrong guess
            self.score = self.score - 1
            self.points.set(self.score)
            #Remove one from guessCounter and let user know number of guesses
            #remaining
            self.guessCounter -= 1
            self.guesses.set(self.guessCounter)
            #Print the hangman figure when player makes wrong guess
            if self.guessCounter == 20:
                self.person.set(hangmanExtreme[0])
            elif self.guessCounter == 19:
                self.person.set(hangmanExtreme[1])
            elif self.guessCounter == 18:
                self.person.set(hangmanExtreme[2])
            elif self.guessCounter == 17:
                self.person.set(hangmanExtreme[3])
            elif self.guessCounter == 16:
                self.person.set(hangmanExtreme[4])
            elif self.guessCounter == 15:
                self.person.set(hangmanExtreme[5])
            elif self.guessCounter == 14:
                self.person.set(hangmanExtreme[6])
            elif self.guessCounter == 13:
                self.person.set(hangmanExtreme[7])
            elif self.guessCounter == 12:
                self.person.set(hangmanExtreme[8])
            elif self.guessCounter == 11:
                self.person.set(hangmanExtreme[9])
            elif self.guessCounter == 10:
                self.person.set(hangmanExtreme[10])
            elif self.guessCounter == 9:
                self.person.set(hangmanExtreme[11])
            elif self.guessCounter == 8:
                self.person.set(hangmanExtreme[12])
            elif self.guessCounter == 7:
                self.person.set(hangmanExtreme[13])
            elif self.guessCounter == 6:
                self.person.set(hangmanExtreme[14])
            elif self.guessCounter == 5:
                self.person.set(hangmanExtreme[15])
            elif self.guessCounter == 4:
                self.person.set(hangmanExtreme[16])
            elif self.guessCounter == 3:
                self.person.set(hangmanExtreme[17])
            elif self.guessCounter == 2:
                self.person.set(hangmanExtreme[18])
            elif self.guessCounter == 1:
                self.person.set(hangmanExtreme[19])
            elif self.guessCounter == 0:
                self.person.set(hangmanExtreme[20])
            #Check to see if game ends due to no more guesses left
            if self.guessCounter == 0:
                self.text.set("Sorry, you did not guess the word in time.")
                self.answer.set(self.word)
                self.userName = self.name.get()
                if self.score > self.hiScore:
                    self.hiScore = self.score
                    self.highScore.set(self.hiScore)
                    self.text.set("You have a new high score!")
                else:
                    self.hiScore = self.hiScore
                self.dataList = [self.userName, str(self.hiScore)]
                self.outputText = ','.join(self.dataList)
                writeFile(self.DATA_FILE_PATH, self.outputText)
                self.score = 0
        #Remove the player's guess from the choices list so that it is no
        #longer an option
        self.choices.remove(self.guess)
        self.lettersGuessed.append(self.guess) 
        self.letterBank.set(sorted(self.lettersGuessed))
        #Check if game ends because player guessed all letters in the word
        if "_" not in self.letters:
            self.directions.set("You guessed the word! To play again press PLAY.")
            self.answer.set(self.word)
            #If player guesses 3 words in a row, get bonus points
            self.comboBonus = self.comboBonus + 1
            if self.comboBonus == 3:
                self.text.set("Nice job! You correctly guessed 3 words in a row.")
                self.score += 3
                #Reset the combo tracker back to 0
                self.comboBonus = 0
    #Thread to prevent the GUI from crashing
    def threading5(self):
        t5 = Thread(target = self.letter)
        t5.start()
    #Player guesses the word
    def wordguess(self):
        self.guess = self.entry.get()
        #If correct, add to player score and break loop
        if self.guess.lower() == self.word:
            self.directions.set("Correct! To play again press PLAY.")
            self.answer.set(self.word)
            self.score = self.score + 10
            self.points.set(self.score)
            self.userName = self.name.get()
            #Check for high score and save data
            if self.score > self.hiScore:
                self.hiScore = self.score
                self.highScore.set(self.hiScore)
                self.text.set("You have a new high score!")
            else:
                self.hiScore = self.hiScore
            self.dataList = [self.userName, str(self.hiScore)]
            self.outputText = ','.join(self.dataList)
            writeFile(self.DATA_FILE_PATH, self.outputText)
            #If player guesses 3 words in a row, get bonus points
            self.comboBonus = self.comboBonus + 1
            if self.comboBonus == 3:
                self.text.set("Nice job! You correctly guessed 3 words in a row.")
                self.score += 3
                self.points.set(self.score)
                self.score =self.score + self.addScore
                self.points.set(self.score)
                self.userName = self.name.get()
                #Check for high score and save data
                if self.score > self.hiScore:
                    self.hiScore = self.score
                    self.highScore.set(self.hiScore)
                    self.text.set("You have a new high score!")
                else:
                    self.hiScore = self.hiScore
                self.dataList = [self.userName, str(self.hiScore)]
                self.outputText = ','.join(self.dataList)
                writeFile(self.DATA_FILE_PATH, self.outputText)
                #Reset the combo tracker back to 0
                self.comboBonus = 0
            #If player guess incorrect
        else:
            self.text.set("Sorry, that's not the correct word or spelling.")
            #Lose points for wrong guess
            self.score = self.score - 5
            self.points.set(self.score)
            self.guessCounter -= 1
            self.guesses.set(self.guessCounter)
            #Print the hangman figure when player makes wrong guess
            if self.guessCounter == 20:
                self.person.set(hangmanExtreme[0])
            elif self.guessCounter == 19:
                self.person.set(hangmanExtreme[1])
            elif self.guessCounter == 18:
                self.person.set(hangmanExtreme[2])
            elif self.guessCounter == 17:
                self.person.set(hangmanExtreme[3])
            elif self.guessCounter == 16:
                self.person.set(hangmanExtreme[4])
            elif self.guessCounter == 15:
                self.person.set(hangmanExtreme[5])
            elif self.guessCounter == 14:
                self.person.set(hangmanExtreme[6])
            elif self.guessCounter == 13:
                self.person.set(hangmanExtreme[7])
            elif self.guessCounter == 12:
                self.person.set(hangmanExtreme[8])
            elif self.guessCounter == 11:
                self.person.set(hangmanExtreme[9])
            elif self.guessCounter == 10:
                self.person.set(hangmanExtreme[10])
            elif self.guessCounter == 9:
                self.person.set(hangmanExtreme[11])
            elif self.guessCounter == 8:
                self.person.set(hangmanExtreme[12])
            elif self.guessCounter == 7:
                self.person.set(hangmanExtreme[13])
            elif self.guessCounter == 6:
                self.person.set(hangmanExtreme[14])
            elif self.guessCounter == 5:
                self.person.set(hangmanExtreme[15])
            elif self.guessCounter == 4:
                self.person.set(hangmanExtreme[16])
            elif self.guessCounter == 3:
                self.person.set(hangmanExtreme[17])
            elif self.guessCounter == 2:
                self.person.set(hangmanExtreme[18])
            elif self.guessCounter == 1:
                self.person.set(hangmanExtreme[19])
            elif self.guessCounter == 0:
                self.person.set(hangmanExtreme[20])
            #Check if player has run out of guesses
            if self.guessCounter == 0:
                self.text.set("Sorry, you did not guess the word in time.")
                self.answer.set(self.word)
                self.userName = self.name.get()
                if self.score > self.hiScore:
                    self.hiScore = self.score
                    self.highScore.set(self.hiScore)
                    self.text.set("You have a new high score!")
                else:
                    self.hiScore = self.hiScore
                self.dataList = [self.userName, str(self.hiScore)]
                self.outputText = ','.join(self.dataList)
                writeFile(self.DATA_FILE_PATH, self.outputText)
                self.score = 0
    #Thread to prevent the GUI from crashing
    def threading6(self):
        t6 = Thread(target = self.wordguess)
        t6.start()
#Creates the two player "traditional" hangman mode
class TwoPlay(tk.Frame):
    #Set up the frame and game buttons
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg ='LightCyan2', width = 1000, height = 700)
        self.label1 = tk.Label(self.frame, text = 'Hangman' , font='arial 20 bold')
        self.label1.place(x=500, y=15)
        self.label2 = tk.Label(self.frame, text = "Scores:", font='arial 15 bold')
        self.label2.place(x = 400,y=50)
        self.user1 = tk.StringVar()
        self.label3 = tk.Label(self.frame, textvariable = self.user1, font='arial 15 bold')
        self.label3.place(x = 400,y=85)
        self.points1 = tk.StringVar()
        self.label4 = tk.Label(self.frame, textvariable = self.points1, font='arial 15 bold', bg = 'seashell2')
        self.label4.place(x = 400,y=120)
        self.user2 = tk.StringVar()
        self.label5 = tk.Label(self.frame, textvariable = self.user2, font='arial 15 bold', bg = 'seashell2')
        self.label5.place(x = 400,y=155)
        self.points2 = tk.StringVar()
        self.label25 = tk.Label(self.frame, textvariable = self.points2, font='arial 15 bold', bg = 'seashell2')
        self.label25.place(x = 400,y=190)
        self.label26 = tk.Label(self.frame, text = "Player turn:", font='arial 15 bold')
        self.label26.place(x = 25,y=40)
        self.name = tk.StringVar()
        self.label6 = tk.Label(self.frame, font = 'arial 15 bold', textvariable = self.name, bg ='antiquewhite2')
        self.label6.place(x=150, y = 40)       
        
        self.directions = tk.StringVar()
        self.entry1 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.directions, bg ='antiquewhite2',width = 50,)
        self.entry1.place(x=25, y = 70)
        self.directions.set("Type a name and press PLAYER 1:")
        self.entry = tk.StringVar()
        self.entry2 = tk.Entry(self.frame, font = 'arial 15', textvariable = self.entry , bg = 'antiquewhite2')
        self.entry2.place(x=25, y = 90)
        self.text = tk.StringVar()
        self.entry3 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.text, bg ='antiquewhite2',width = 60)
        self.entry3.place(x=25, y = 275)
        self.label7 = tk.Label(self.frame, text = "Current category:", font='arial 12 bold', bg = 'seashell2')
        self.label7.place(x = 25,y=300)
        self.currentCategory = tk.StringVar()
        self.label8 = tk.Label(self.frame, textvariable = self.currentCategory, font='arial 12 bold', bg = 'seashell2')
        self.label8.place(x = 210,y=300)
        self.label9 = tk.Label(self.frame, text = "Letters guessed:", font='arial 12 bold', bg = 'seashell2')
        self.label9.place(x = 25,y=325)
        self.letterBank = tk.StringVar()
        self.label10 = tk.Label(self.frame, textvariable = self.letterBank, font='arial 12 bold', bg = 'seashell2')
        self.label10.place(x = 210,y=325)
        self.label11 = tk.Label(self.frame, text = "Guesses left:", font='arial 12 bold', bg = 'seashell2')
        self.label11.place(x = 25,y=350)
        self.guesses = tk.StringVar()
        self.label12 = tk.Label(self.frame, textvariable = self.guesses, font='arial 12 bold', bg = 'seashell2')
        self.label12.place(x = 210,y=350)
        self.person = tk.StringVar()
        self.label13 = tk.Label(self.frame, font = 'arial 10 bold', textvariable = self.person, bg ='antiquewhite2',width = 60)
        self.label13.place(x=25, y = 380, height = 200)
        self.current = tk.StringVar()
        self.entry4 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.current, bg ='antiquewhite2',width = 60)
        self.entry4.place(x=25, y = 590)
        self.label14 = tk.Label(self.frame, text = "Answer:", font='arial 15 bold', bg = 'seashell2')
        self.label14.place(x = 25,y=615)
        self.answer = tk.StringVar()
        self.label15 = tk.Label(self.frame, textvariable = self.answer, font='arial 15 bold', bg = 'seashell2')
        self.label15.place(x = 120,y=615)
        self.categoryList = tk.Text(self.frame, height = 100, width = 50)
        self.button10 = tk.Button(self.frame, font = 'arial 13 bold', text = 'PLAYER 1'  ,padx =5,bg ='LightCyan3' ,command = self.threading1)
        self.button10.place(x=25,y=150)
        self.button11 = tk.Button(self.frame, font = 'arial 13 bold', text = 'PLAYER 2'  ,padx =5,bg ='LightCyan3' ,command = self.threading2)
        self.button11.place(x=25,y=190)
        self.button12 = tk.Button(self.frame, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='LightCyan3' ,command = self.threading3)
        self.button12.place(x=25,y=230)
        self.button13 = tk.Button(self.frame, font = 'arial 13 bold', text = 'GUESS'  ,padx =5,bg ='LightCyan3' ,command = self.guess)
        self.button13.place(x=225,y=150)
        self.button14 = tk.Button(self.frame, font = 'arial 13 bold', text = 'LETTER'  ,padx =5,bg ='LightCyan3' ,command = self.threading5)
        self.button14.place(x=225,y=190)
        self.button15 = tk.Button(self.frame, font = 'arial 13 bold', text = 'WORD'  ,padx =5,bg ='LightCyan3' ,command = self.threading6)
        self.button15.place(x=225,y=230)
        self.button16 = tk.Button(self.frame, font = 'arial 13 bold', text = 'MAIN MENU'  ,padx =5,bg ='LightCyan2' ,command = self.mainMenu)
        self.button16.place(x=25,y=650)
        self.button17 = tk.Button(self.frame, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='LightCyan2' ,command = self.exit)
        self.button17.place(x=900,y=650)
        
        #Separate Entry texts for each category in order to display them one above the other
        self.label16 = tk.Label(self.frame, font = 'arial 10 bold', text = "List of categories:", bg ='LightCyan2')
        self.label16.place(x=700, y = 30)
        self.countries = tk.StringVar()
        self.entry5 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.countries, bg ='LightCyan2',width = 40,)
        self.entry5.place(x=700, y = 50)
        self.fruit = tk.StringVar()
        self.entry6 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.fruit, bg ='LightCyan2',width = 40,)
        self.entry6.place(x=700, y = 70)
        self.elements = tk.StringVar()
        self.entry7 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.elements, bg ='LightCyan2',width = 40,)
        self.entry7.place(x=700, y = 90)
        self.mammals = tk.StringVar()
        self.entry8 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.mammals, bg ='LightCyan2',width = 40,)
        self.entry8.place(x=700, y = 110)
        self.dinosaurs = tk.StringVar()
        self.entry9 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.dinosaurs, bg ='LightCyan2',width = 40,)
        self.entry9.place(x=700, y = 130)
        self.insects = tk.StringVar()
        self.entry10 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.insects, bg ='LightCyan2',width = 40,)
        self.entry10.place(x=700, y = 150)
        self.herbs = tk.StringVar()
        self.entry11 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.herbs, bg ='LightCyan2',width = 40,)
        self.entry11.place(x=700, y = 170)
        self.science = tk.StringVar()
        self.entry12 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.science, bg ='LightCyan2',width = 40,)
        self.entry12.place(x=700, y = 190)
        self.chemicals = tk.StringVar()
        self.entry13 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.chemicals, bg ='LightCyan2',width = 40,)
        self.entry13.place(x=700, y = 210)
        self.states = tk.StringVar()
        self.entry14 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.states, bg ='LightCyan2',width = 40,)
        self.entry14.place(x=700, y = 230)
        self.cities = tk.StringVar()
        self.entry15 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.cities, bg ='LightCyan2',width = 40,)
        self.entry15.place(x=700, y = 250)
        self.figures = tk.StringVar()
        self.entry16 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.figures, bg ='LightCyan2',width = 40,)
        self.entry16.place(x=700, y = 250)
        
        #These are the labels to show the list of categories
        self.label17 = tk.Label(self.frame, font = 'arial 10 bold', text = "List of categories:", bg ='LightCyan2',width = 40,)
        self.label17.place(x=700, y = 30)
        self.countries = tk.StringVar()
        self.entry17 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.countries, bg ='LightCyan2',width = 40,)
        self.entry17.place(x=700, y = 50)
        self.fruit = tk.StringVar()
        self.entry18 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.fruit, bg ='LightCyan2',width = 40,)
        self.entry18.place(x=700, y = 70)
        self.elements = tk.StringVar()
        self.entry19 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.elements, bg ='LightCyan2',width = 40,)
        self.entry19.place(x=700, y = 90)
        self.mammals = tk.StringVar()
        self.entry20 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.mammals, bg ='LightCyan2',width = 40,)
        self.entry20.place(x=700, y = 110)
        self.dinosaurs = tk.StringVar()
        self.entry21 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.dinosaurs, bg ='LightCyan2',width = 40,)
        self.entry21.place(x=700, y = 130)
        self.insects = tk.StringVar()
        self.entry22 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.insects, bg ='LightCyan2',width = 40,)
        self.entry22.place(x=700, y = 150)
        self.herbs = tk.StringVar()
        self.entry23 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.herbs, bg ='LightCyan2',width = 40,)
        self.entry23.place(x=700, y = 170)
        self.science = tk.StringVar()
        self.entry24 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.science, bg ='LightCyan2',width = 40,)
        self.entry24.place(x=700, y = 190)
        self.chemicals = tk.StringVar()
        self.entry25 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.chemicals, bg ='LightCyan2',width = 40,)
        self.entry25.place(x=700, y = 210)
        self.states = tk.StringVar()
        self.entry26 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.states, bg ='LightCyan2',width = 40,)
        self.entry26.place(x=700, y = 230)
        self.cities = tk.StringVar()
        self.entry27 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.cities, bg ='LightCyan2',width = 40,)
        self.entry27.place(x=700, y = 250)
        self.figures = tk.StringVar()
        self.entry28 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.figures, bg ='LightCyan2',width = 40,)
        self.entry28.place(x=700, y = 270)
        self.countries.set("'c' - countries")
        self.fruit.set("'f' - fruits & vegetables")
        self.elements.set("'e' - periodic elements")
        self.mammals.set("'m' - mammals")
        self.dinosaurs.set("'d' - dinosaurs")
        self.insects.set("'i' - insects")
        self.herbs.set("'h' - herbs & spices")
        self.science.set("'s' - science")
        self.chemicals.set("'a' - chemicals")
        self.states.set("'u' - U.S. states")
        self.cities.set("'w' - world cities")
        self.figures.set("'p' - historical figures")
        
        #Directions for how to use the buttons
        self.label18 = tk.Label(self.frame, font = 'arial 14 bold', text = "How to play:", bg ='LightCyan2',width = 40,)
        self.label18.place(x=500, y = 350)
        self.label19 = tk.Label(self.frame, font = 'arial 10 bold', text = "PLAYER ONE: Press this after player one has typed a name.", bg ='LightCyan2',width = 50,)
        self.label19.place(x=550, y = 380)
        self.label20 = tk.Label(self.frame, font = 'arial 10 bold', text = "PLAYER TWO: Press this after player two has typed a name.", bg ='LightCyan2',width = 50,)
        self.label20.place(x=550, y = 410)
        self.label21 = tk.Label(self.frame, font = 'arial 10 bold', text = "PLAY: Press this to begin a game or play again.", bg ='LightCyan2',width = 50,)
        self.label21.place(x=550, y = 440)
        self.label22 = tk.Label(self.frame, font = 'arial 10 bold', text = "GUESS: Press this after pressing PLAY to begin guessing.", bg ='LightCyan2',width = 50,)
        self.label22.place(x=550, y = 470)
        self.label23 = tk.Label(self.frame, font = 'arial 10 bold', text = "LETTER: After typing a letter, press this button to make a guess.", bg ='LightCyan2',width = 50,)
        self.label23.place(x=550, y = 500)
        self.label24 = tk.Label(self.frame, font = 'arial 10 bold', text = "WORD: After typing a word, press this button to make a guess.", bg ='LightCyan2',width = 50,)
        self.label24.place(x=550, y = 530)
        self.frame.pack()
        
    #This begins the game    
    def playerOne(self):
        #Get player one name
        self.player1 = self.entry.get()
        #Reset text boxes and enter some
        self.entry.set("")
        self.directions.set("")
        self.text.set("")
        self.name.set(self.player1)
        self.user1.set(self.player1)
        #Set score and comboBonus variables here so they won't reset with a new game
        self.score1 = 0
        self.points1.set(self.score1)
        #Set in tkinter
        self.directions.set("Second player, enter a name and press PLAYER 2:")
    #Thread to prevent the GUI from crashing
    def threading1(self):
        t1 = Thread(target = self.playerOne)
        t1.start()
    #Creates username and checks if a file for it exists
    def playerTwo(self):
        #Get player two name
        self.player2 = self.entry.get()
        self.user2.set(self.player2)
        self.entry.set("")
        #Set score and comboBonus variables here so they won't reset with a new game
        self.score2 = 0
        self.points2.set(self.score2)
        #Provide instructions for next step
        self.directions.set("Press PLAY to begin.")
    #Thread to prevent the GUI from crashing  
    def threading2(self):
        t2 = Thread(target = self.playerTwo)
        t2.start()
    #Sets up the game with key lists/variables and has the player choose a category    
    def play(self):
        #Reset all text boxes
        self.entry.set("")
        self.directions.set("")
        self.text.set("")
        self.answer.set("")
        #List of all possible player choices
        self.choices = []
        self.choices.append("a")
        self.choices.append("b")
        self.choices.append("c")
        self.choices.append("d")
        self.choices.append("e")
        self.choices.append("f")
        self.choices.append("g")
        self.choices.append("h")
        self.choices.append("i")
        self.choices.append("j")
        self.choices.append("k")
        self.choices.append("l")
        self.choices.append("m")
        self.choices.append("n")
        self.choices.append("o")
        self.choices.append("p")
        self.choices.append("q")
        self.choices.append("r")
        self.choices.append("s")
        self.choices.append("t")
        self.choices.append("u")
        self.choices.append("v")
        self.choices.append("w")
        self.choices.append("x")
        self.choices.append("y")
        self.choices.append("z")
        #Number of guesses the user has
        self.guessCounter = 10
        self.guesses.set(self.guessCounter)
        # Prompt user to select category
        while True:
            # Return random word based on category selection    
            # assign variables for random dictionary value
            self.countries = random.choice(data['countries']).lower()
            self.fruitVeg = random.choice(data['fruitVeg']).lower()
            self.elements = random.choice(data['elements']).lower()
            self.mammals = random.choice(data['mammals']).lower()
            self.dinosaurs = random.choice(data['dinosaurs']).lower()
            self.insects = random.choice(data['insects']).lower()
            self.herbSpice = random.choice(data['herbSpice']).lower()
            self.science = random.choice(data['science']).lower()
            self.chemicals = random.choice(data['chemicals']).lower()
            self.usStates = random.choice(data['usStates']).lower()
            self.worldCities = random.choice(data['worldCities']).lower()
            self.people = random.choice(data['people']).lower()
            self.directions.set("Choose a category by typing a letter to the right: ")
            
            self.category = self.entry.get()
            if self.category == 'c':
                self.randomWord = self.countries.lower()
                self.currentCategory.set("Countries")
                break
            elif self.category == 'f':
                self.randomWord = self.fruitVeg.lower()
                self.currentCategory.set("Fruits and Veggies")
                break
            elif self.category == 'e':
                self.randomWord = self.elements.lower()
                self.currentCategory.set("Periodic Elements")
                break
            elif self.category == 'm':
                self.randomWord = self.mammals.lower()
                self.currentCategory.set("Mammals")
                break
            elif self.category == 'd':
                self.randomWord = self.dinosaurs.lower()
                self.currentCategory.set("Dinosaurs")
                break
            elif self.category == 'i':
                self.randomWord = self.insects.lower()
                self.currentCategory.set("Insects")
                break
            elif self.category == 'h':
                self.randomWord = self.herbSpice.lower()
                self.currentCategory.set("Herbs and Spices")
                break
            elif self.category == 's':
                self.randomWord = self.science.lower()
                self.currentCategory.set("Science")
                break
            elif self.category == 'a':
                self.randomWord = self.chemicals.lower()
                self.currentCategory.set("Chemicals")
                break
            elif self.category == 'u':
                self.randomWord = self.usStates.lower()
                self.currentCategory.set("U.S. States")
                break
            elif self.category == 'w':
                self.randomWord = self.worldCities.lower()
                self.currentCategory.set("World Cities")
                break
            elif self.category == 'p':
                self.randomWord = self.people.lower()
                self.currentCategory.set("Historical Figures")
                break
            #else:
             #   text.set("That was not a category option. Press PLAY again.")
        
        self.directions.set("Word selected. Press GUESS to begin guessing.")
        #Clear the entry text
        self.entry.set("")
        self.word = self.randomWord
        #Empty list to store letters in the word.
        self.letters = []
        #Empty list to store letters that the player guesses
        self.lettersGuessed = []
        #Changes all letters in the word into an underscore symbol.
        for self.character in list(self.word):
            self.letters.append("_")
        #Change any spaces from an underscore back into a space
        for i in range(len(self.word)):
            self.character = self.word[i]
            if self.character == " ":
                self.letters[i] = self.word[i]    
        #Print out the underscores for the word joined by a space before each guess
        self.current.set("The current word is: " + " ".join(self.letters))
    #Thread to prevent the GUI from crashing
    def threading3(self):
        t3 = Thread(target = self.play)
        t3.start()
    #Player begins guessing by choosing what to guess
    def guess(self):
        self.entry.set("")
        self.text.set("")
        self.directions.set("Enter your guess then press LETTER or WORD.")
        if self.guessCounter == 10:
            self.person.set(hangmanEasy[0])
    #Player guesses a letter
    def letter(self):
        #Player guess input
        self.guess = self.entry.get()
        while True:
            #Break if user guesses a letter in the list of choices
            if self.guess in self.choices:
                break
            #Repeat input message if user guesses something not in the choices list
            else:
                self.text.set("You either guessed that letter, or you typed something else.")
                self.entry.set("")
                #self.directions.set("Press GUESS to guess again.")
        #For correct guess
        if self.guess.lower() in list(self.word):
             self.text.set("You are correct!")
             self.entry.set("")
             #self.directions.set("Press GUESS.")
             
             #Iterate through the word to change all instances of a correct
             #guess from underscores to the letter
             for i in range(len(self.word)):
                 self.character = self.word[i]
                 if self.character == self.guess:
                     self.letters[i] = self.word[i]
             #Print out the underscores for the word joined by a space before each guess
             self.current.set("The current word is: " + " ".join(self.letters))
             #This adds to the user's score based on the number of times
             #the correct guess appears in the word.
             #First we check which player is guessing
             if self.name.get() == self.player1:
                 self.addScore = self.letters.count(self.guess) * 2
                 self.score1 = self.score1 + self.addScore
                 self.points1.set(self.score1)
                 self.name.set(self.player2)
             else:
                 self.addScore = self.letters.count(self.guess) * 2
                 self.score2 = self.score2 + self.addScore
                 self.points2.set(self.score2)
                 self.name.set(self.player1)
        #Wrong guess
        else:
            self.text.set("Sorry, that letter is not in the word.")
            self.entry.set("")
            #self.directions.set("Press GUESS.")
            #Change players
            if self.name.get() == self.player1:
                self.name.set(self.player2)
            else:
                self.name.set(self.player1)
            #Remove one from guessCounter and let user know number of guesses
            #remaining
            self.guessCounter -= 1
            self.guesses.set(self.guessCounter)
            #Print the hangman figure when player makes wrong guess
            if self.guessCounter == 10:
                self.person.set(hangmanEasy[0])
            elif self.guessCounter == 9:
                self.person.set(hangmanEasy[1])
            elif self.guessCounter == 8:
                self.person.set(hangmanEasy[2])
            elif self.guessCounter == 7:
                self.person.set(hangmanEasy[3])
            elif self.guessCounter == 6:
                self.person.set(hangmanEasy[4])
            elif self.guessCounter == 5:
                self.person.set(hangmanEasy[5])
            elif self.guessCounter == 4:
                self.person.set(hangmanEasy[6])
            elif self.guessCounter == 3:
                self.person.set(hangmanEasy[7])
            elif self.guessCounter == 2:
                self.person.set(hangmanEasy[8])
            elif self.guessCounter == 1:
                self.person.set(hangmanEasy[9])
            elif self.guessCounter == 0:
                self.person.set(hangmanEasy[10])
            #Check to see if game ends due to no more guesses left
            if self.guessCounter == 0:
                self.text.set("\nSorry, you did not guess the word in time.")
                self.answer.set(self.word)
                self.score1 = 0
                self.score2 = 0
        #Remove the player's guess from the choices list so that it is no
        #longer an option
        self.choices.remove(self.guess)
        self.lettersGuessed.append(self.guess) 
        self.letterBank.set(sorted(self.lettersGuessed))
        #Check if game ends because player guessed all letters in the word
        if "_" not in self.letters:
            self.directions.set("You guessed the word! To play again press PLAY.")
            self.answer.set(self.word)
            #If player guesses 3 words in a row, get bonus points
            self.comboBonus = self.comboBonus + 1
            if self.comboBonus == 3:
                self.text.set("Nice job! You correctly guessed 3 words in a row.")
                self.score += 3
                #Reset the combo tracker back to 0
                self.comboBonus = 0
    #Thread to prevent the GUI from crashing
    def threading5(self):
        t5 = Thread(target = self.letter)
        t5.start()
    #Player guesses the word
    def wordguess(self):
        self.guess = self.entry.get()
        #If correct, add to player score and break loop
        if self.guess.lower() == self.word:
            self.directions.set("Correct! To play again press PLAY.")
            self.answer.set(self.word)
            if self.name.get() == self.player1:
                self.score1 = self.score1 + 10
                self.points1.set(self.score1)
                self.name.set(self.player2)
            else:
                self.score2 = self.score2 +10
                self.points2.set(self.score2)
                self.name.set(self.player1)
        #If player guess incorrect
        else:
            self.text.set("Sorry, that's not the correct word or spelling.")
            self.guessCounter -= 1
            self.guesses.set(self.guessCounter)
            #Change players
            if self.name.get() == self.player1:
                self.name.set(self.player2)
            else:
                self.name.set(self.player1)
            #Print the hangman figure when player makes wrong guess
            if self.guessCounter == 10:
                self.person.set(hangmanEasy[0])
            elif self.guessCounter == 9:
                self.person.set(hangmanEasy[1])
            elif self.guessCounter == 8:
                self.person.set(hangmanEasy[2])
            elif self.guessCounter == 7:
                self.person.set(hangmanEasy[3])
            elif self.guessCounter == 6:
                self.person.set(hangmanEasy[4])
            elif self.guessCounter == 5:
                self.person.set(hangmanEasy[5])
            elif self.guessCounter == 4:
                self.person.set(hangmanEasy[6])
            elif self.guessCounter == 3:
                self.person.set(hangmanEasy[7])
            elif self.guessCounter == 2:
                self.person.set(hangmanEasy[8])
            elif self.guessCounter == 1:
                self.person.set(hangmanEasy[9])
            elif self.guessCounter == 0:
                self.person.set(hangmanEasy[10])
            #Check if player has run out of guesses
            if self.guessCounter == 0:
                self.text.set("Sorry, you did not guess the word in time.")
                self.answer.set(self.word)
    #Thread to prevent the GUI from crashing
    def threading6(self):
        t6 = Thread(target = self.wordguess)
        t6.start()
        
    #Take user back to main menu
    def mainMenu(self):
        self.master.destroy()
    #Exit the system
    def exit(self):
        root.destroy()
        
#Creates the two player Wheel of Fortune hangman mode
class Wheel(tk.Frame):
    #Set up the frame and game buttons
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg ='LightCyan2', width = 1000, height = 700)
        self.label1 = tk.Label(self.frame, text = 'Hangman' , font='arial 20 bold')
        self.label1.place(x=500, y=15)
        self.label2 = tk.Label(self.frame, text = "Scores:", font='arial 15 bold')
        self.label2.place(x = 400,y=50)
        self.user1 = tk.StringVar()
        self.label3 = tk.Label(self.frame, textvariable = self.user1, font='arial 15 bold')
        self.label3.place(x = 400,y=85)
        self.points1 = tk.StringVar()
        self.label4 = tk.Label(self.frame, textvariable = self.points1, font='arial 15 bold', bg = 'seashell2')
        self.label4.place(x = 400,y=120)
        self.user2 = tk.StringVar()
        self.label5 = tk.Label(self.frame, textvariable = self.user2, font='arial 15 bold', bg = 'seashell2')
        self.label5.place(x = 400,y=155)
        self.points2 = tk.StringVar()
        self.label25 = tk.Label(self.frame, textvariable = self.points2, font='arial 15 bold', bg = 'seashell2')
        self.label25.place(x = 400,y=190)
        self.label26 = tk.Label(self.frame, text = "Player turn:", font='arial 15 bold')
        self.label26.place(x = 25,y=40)
        self.name = tk.StringVar()
        self.label6 = tk.Label(self.frame, font = 'arial 15 bold', textvariable = self.name, bg ='antiquewhite2')
        self.label6.place(x=150, y = 40)       
        
        self.directions = tk.StringVar()
        self.entry1 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.directions, bg ='antiquewhite2',width = 50,)
        self.entry1.place(x=25, y = 70)
        self.directions.set("Type a name and press PLAYER 1:")
        self.entry = tk.StringVar()
        self.entry2 = tk.Entry(self.frame, font = 'arial 15', textvariable = self.entry , bg = 'antiquewhite2')
        self.entry2.place(x=25, y = 90)
        self.text = tk.StringVar()
        self.entry3 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.text, bg ='antiquewhite2',width = 60)
        self.entry3.place(x=25, y = 275)
        self.label7 = tk.Label(self.frame, text = "Current category:", font='arial 12 bold', bg = 'seashell2')
        self.label7.place(x = 25,y=300)
        self.currentCategory = tk.StringVar()
        self.label8 = tk.Label(self.frame, textvariable = self.currentCategory, font='arial 12 bold', bg = 'seashell2')
        self.label8.place(x = 210,y=300)
        self.label9 = tk.Label(self.frame, text = "Letters guessed:", font='arial 12 bold', bg = 'seashell2')
        self.label9.place(x = 25,y=325)
        self.letterBank = tk.StringVar()
        self.label10 = tk.Label(self.frame, textvariable = self.letterBank, font='arial 12 bold', bg = 'seashell2')
        self.label10.place(x = 210,y=325)
        self.person = tk.StringVar()
        self.label13 = tk.Label(self.frame, font = 'arial 10 bold', textvariable = self.person, bg ='antiquewhite2',width = 60)
        self.label13.place(x=25, y = 380, height = 200)
        self.current = tk.StringVar()
        self.entry4 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.current, bg ='antiquewhite2',width = 60)
        self.entry4.place(x=25, y = 590)
        self.label14 = tk.Label(self.frame, text = "Answer:", font='arial 15 bold', bg = 'seashell2')
        self.label14.place(x = 25,y=615)
        self.answer = tk.StringVar()
        self.label15 = tk.Label(self.frame, textvariable = self.answer, font='arial 15 bold', bg = 'seashell2')
        self.label15.place(x = 120,y=615)
        self.categoryList = tk.Text(self.frame, height = 100, width = 50)
        self.button10 = tk.Button(self.frame, font = 'arial 13 bold', text = 'PLAYER 1'  ,padx =5,bg ='LightCyan3' ,command = self.threading1)
        self.button10.place(x=25,y=150)
        self.button11 = tk.Button(self.frame, font = 'arial 13 bold', text = 'PLAYER 2'  ,padx =5,bg ='LightCyan3' ,command = self.threading2)
        self.button11.place(x=25,y=190)
        self.button12 = tk.Button(self.frame, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='LightCyan3' ,command = self.threading3)
        self.button12.place(x=25,y=230)
        self.button13 = tk.Button(self.frame, font = 'arial 13 bold', text = 'SPIN'  ,padx =5,bg ='LightCyan3' ,command = self.spin)
        self.button13.place(x=225,y=150)
        self.button14 = tk.Button(self.frame, font = 'arial 13 bold', text = 'LETTER'  ,padx =5,bg ='LightCyan3' ,command = self.threading5)
        self.button14.place(x=225,y=190)
        self.button15 = tk.Button(self.frame, font = 'arial 13 bold', text = 'WORD'  ,padx =5,bg ='LightCyan3' ,command = self.threading6)
        self.button15.place(x=225,y=230)
        self.button16 = tk.Button(self.frame, font = 'arial 13 bold', text = 'MAIN MENU'  ,padx =5,bg ='LightCyan2' ,command = self.mainMenu)
        self.button16.place(x=25,y=650)
        self.button17 = tk.Button(self.frame, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='LightCyan2' ,command = self.exit)
        self.button17.place(x=900,y=650)
        
        #Separate Entry texts for each category in order to display them one above the other
        self.label16 = tk.Label(self.frame, font = 'arial 10 bold', text = "List of categories:", bg ='LightCyan2')
        self.label16.place(x=700, y = 30)
        self.countries = tk.StringVar()
        self.entry5 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.countries, bg ='LightCyan2',width = 40,)
        self.entry5.place(x=700, y = 50)
        self.fruit = tk.StringVar()
        self.entry6 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.fruit, bg ='LightCyan2',width = 40,)
        self.entry6.place(x=700, y = 70)
        self.elements = tk.StringVar()
        self.entry7 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.elements, bg ='LightCyan2',width = 40,)
        self.entry7.place(x=700, y = 90)
        self.mammals = tk.StringVar()
        self.entry8 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.mammals, bg ='LightCyan2',width = 40,)
        self.entry8.place(x=700, y = 110)
        self.dinosaurs = tk.StringVar()
        self.entry9 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.dinosaurs, bg ='LightCyan2',width = 40,)
        self.entry9.place(x=700, y = 130)
        self.insects = tk.StringVar()
        self.entry10 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.insects, bg ='LightCyan2',width = 40,)
        self.entry10.place(x=700, y = 150)
        self.herbs = tk.StringVar()
        self.entry11 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.herbs, bg ='LightCyan2',width = 40,)
        self.entry11.place(x=700, y = 170)
        self.science = tk.StringVar()
        self.entry12 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.science, bg ='LightCyan2',width = 40,)
        self.entry12.place(x=700, y = 190)
        self.chemicals = tk.StringVar()
        self.entry13 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.chemicals, bg ='LightCyan2',width = 40,)
        self.entry13.place(x=700, y = 210)
        self.states = tk.StringVar()
        self.entry14 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.states, bg ='LightCyan2',width = 40,)
        self.entry14.place(x=700, y = 230)
        self.cities = tk.StringVar()
        self.entry15 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.cities, bg ='LightCyan2',width = 40,)
        self.entry15.place(x=700, y = 250)
        self.figures = tk.StringVar()
        self.entry16 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.figures, bg ='LightCyan2',width = 40,)
        self.entry16.place(x=700, y = 250)
        
        #These are the labels to show the list of categories
        self.label17 = tk.Label(self.frame, font = 'arial 10 bold', text = "List of categories:", bg ='LightCyan2',width = 40,)
        self.label17.place(x=700, y = 30)
        self.countries = tk.StringVar()
        self.entry17 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.countries, bg ='LightCyan2',width = 40,)
        self.entry17.place(x=700, y = 50)
        self.fruit = tk.StringVar()
        self.entry18 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.fruit, bg ='LightCyan2',width = 40,)
        self.entry18.place(x=700, y = 70)
        self.elements = tk.StringVar()
        self.entry19 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.elements, bg ='LightCyan2',width = 40,)
        self.entry19.place(x=700, y = 90)
        self.mammals = tk.StringVar()
        self.entry20 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.mammals, bg ='LightCyan2',width = 40,)
        self.entry20.place(x=700, y = 110)
        self.dinosaurs = tk.StringVar()
        self.entry21 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.dinosaurs, bg ='LightCyan2',width = 40,)
        self.entry21.place(x=700, y = 130)
        self.insects = tk.StringVar()
        self.entry22 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.insects, bg ='LightCyan2',width = 40,)
        self.entry22.place(x=700, y = 150)
        self.herbs = tk.StringVar()
        self.entry23 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.herbs, bg ='LightCyan2',width = 40,)
        self.entry23.place(x=700, y = 170)
        self.science = tk.StringVar()
        self.entry24 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.science, bg ='LightCyan2',width = 40,)
        self.entry24.place(x=700, y = 190)
        self.chemicals = tk.StringVar()
        self.entry25 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.chemicals, bg ='LightCyan2',width = 40,)
        self.entry25.place(x=700, y = 210)
        self.states = tk.StringVar()
        self.entry26 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.states, bg ='LightCyan2',width = 40,)
        self.entry26.place(x=700, y = 230)
        self.cities = tk.StringVar()
        self.entry27 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.cities, bg ='LightCyan2',width = 40,)
        self.entry27.place(x=700, y = 250)
        self.figures = tk.StringVar()
        self.entry28 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.figures, bg ='LightCyan2',width = 40,)
        self.entry28.place(x=700, y = 270)
        self.countries.set("'c' - countries")
        self.fruit.set("'f' - fruits & vegetables")
        self.elements.set("'e' - periodic elements")
        self.mammals.set("'m' - mammals")
        self.dinosaurs.set("'d' - dinosaurs")
        self.insects.set("'i' - insects")
        self.herbs.set("'h' - herbs & spices")
        self.science.set("'s' - science")
        self.chemicals.set("'a' - chemicals")
        self.states.set("'u' - U.S. states")
        self.cities.set("'w' - world cities")
        self.figures.set("'p' - historical figures")
        
        #Directions for how to use the buttons
        self.label18 = tk.Label(self.frame, font = 'arial 14 bold', text = "How to play:", bg ='LightCyan2',width = 40,)
        self.label18.place(x=500, y = 350)
        self.label19 = tk.Label(self.frame, font = 'arial 10 bold', text = "PLAYER ONE: Press this after player one has typed a name.", bg ='LightCyan2',width = 50,)
        self.label19.place(x=550, y = 380)
        self.label20 = tk.Label(self.frame, font = 'arial 10 bold', text = "PLAYER TWO: Press this after player two has typed a name.", bg ='LightCyan2',width = 50,)
        self.label20.place(x=550, y = 410)
        self.label21 = tk.Label(self.frame, font = 'arial 10 bold', text = "PLAY: Press this to begin a game or play again.", bg ='LightCyan2',width = 50,)
        self.label21.place(x=550, y = 440)
        self.label22 = tk.Label(self.frame, font = 'arial 10 bold', text = "SPIN: Press this to spin the wheel. Must spin before guessing a letter.", bg ='LightCyan2',width = 50,)
        self.label22.place(x=550, y = 470)
        self.label23 = tk.Label(self.frame, font = 'arial 10 bold', text = "LETTER: After typing a letter, press this button to make a guess.", bg ='LightCyan2',width = 50,)
        self.label23.place(x=550, y = 500)
        self.label24 = tk.Label(self.frame, font = 'arial 10 bold', text = "WORD: After typing a word, press this button to make a guess.", bg ='LightCyan2',width = 50,)
        self.label24.place(x=550, y = 530)
        self.frame.pack()
        
    #This begins the game    
    def playerOne(self):
        #Get player one name
        self.player1 = self.entry.get()
        #Reset text boxes and enter some
        self.entry.set("")
        self.directions.set("")
        self.text.set("")
        self.name.set(self.player1)
        self.user1.set(self.player1)
        #Set score and comboBonus variables here so they won't reset with a new game
        self.score1 = 0
        self.points1.set(self.score1)
        #Set in tkinter
        self.directions.set("Second player, enter a name and press PLAYER 2:")
    #Thread to prevent the GUI from crashing
    def threading1(self):
        t1 = Thread(target = self.playerOne)
        t1.start()
    #Creates username and checks if a file for it exists
    def playerTwo(self):
        #Get player two name
        self.player2 = self.entry.get()
        self.user2.set(self.player2)
        self.entry.set("")
        #Set score and comboBonus variables here so they won't reset with a new game
        self.score2 = 0
        self.points2.set(self.score2)
        #Provide instructions for next step
        self.directions.set("Press PLAY to begin.")
    #Thread to prevent the GUI from crashing  
    def threading2(self):
        t2 = Thread(target = self.playerTwo)
        t2.start()
    #Sets up the game with key lists/variables and has the player choose a category    
    def play(self):
        #Reset all text boxes
        self.entry.set("")
        self.directions.set("")
        self.text.set("")
        self.answer.set("")
        self.spin = 0
        #List of all possible player choices
        self.choices = []
        self.choices.append("a")
        self.choices.append("b")
        self.choices.append("c")
        self.choices.append("d")
        self.choices.append("e")
        self.choices.append("f")
        self.choices.append("g")
        self.choices.append("h")
        self.choices.append("i")
        self.choices.append("j")
        self.choices.append("k")
        self.choices.append("l")
        self.choices.append("m")
        self.choices.append("n")
        self.choices.append("o")
        self.choices.append("p")
        self.choices.append("q")
        self.choices.append("r")
        self.choices.append("s")
        self.choices.append("t")
        self.choices.append("u")
        self.choices.append("v")
        self.choices.append("w")
        self.choices.append("x")
        self.choices.append("y")
        self.choices.append("z")
        # Prompt user to select category
        while True:
            # Return random word based on category selection    
            # assign variables for random dictionary value
            self.countries = random.choice(data['countries']).lower()
            self.fruitVeg = random.choice(data['fruitVeg']).lower()
            self.elements = random.choice(data['elements']).lower()
            self.mammals = random.choice(data['mammals']).lower()
            self.dinosaurs = random.choice(data['dinosaurs']).lower()
            self.insects = random.choice(data['insects']).lower()
            self.herbSpice = random.choice(data['herbSpice']).lower()
            self.science = random.choice(data['science']).lower()
            self.chemicals = random.choice(data['chemicals']).lower()
            self.usStates = random.choice(data['usStates']).lower()
            self.worldCities = random.choice(data['worldCities']).lower()
            self.people = random.choice(data['people']).lower()
            self.directions.set("Choose a category by typing a letter to the right: ")
            
            self.category = self.entry.get()
            if self.category == 'c':
                self.randomWord = self.countries.lower()
                self.currentCategory.set("Countries")
                break
            elif self.category == 'f':
                self.randomWord = self.fruitVeg.lower()
                self.currentCategory.set("Fruits and Veggies")
                break
            elif self.category == 'e':
                self.randomWord = self.elements.lower()
                self.currentCategory.set("Periodic Elements")
                break
            elif self.category == 'm':
                self.randomWord = self.mammals.lower()
                self.currentCategory.set("Mammals")
                break
            elif self.category == 'd':
                self.randomWord = self.dinosaurs.lower()
                self.currentCategory.set("Dinosaurs")
                break
            elif self.category == 'i':
                self.randomWord = self.insects.lower()
                self.currentCategory.set("Insects")
                break
            elif self.category == 'h':
                self.randomWord = self.herbSpice.lower()
                self.currentCategory.set("Herbs and Spices")
                break
            elif self.category == 's':
                self.randomWord = self.science.lower()
                self.currentCategory.set("Science")
                break
            elif self.category == 'a':
                self.randomWord = self.chemicals.lower()
                self.currentCategory.set("Chemicals")
                break
            elif self.category == 'u':
                self.randomWord = self.usStates.lower()
                self.currentCategory.set("U.S. States")
                break
            elif self.category == 'w':
                self.randomWord = self.worldCities.lower()
                self.currentCategory.set("World Cities")
                break
            elif self.category == 'p':
                self.randomWord = self.people.lower()
                self.currentCategory.set("Historical Figures")
                break
            #else:
             #   text.set("That was not a category option. Press PLAY again.")
        
        self.directions.set("Word selected. Press SPIN to spin the wheel.")
        #Clear the entry text
        self.entry.set("")
        self.word = self.randomWord
        #Empty list to store letters in the word.
        self.letters = []
        #Empty list to store letters that the player guesses
        self.lettersGuessed = []
        #Changes all letters in the word into an underscore symbol.
        for self.character in list(self.word):
            self.letters.append("_")
        #Change any spaces from an underscore back into a space
        for i in range(len(self.word)):
            self.character = self.word[i]
            if self.character == " ":
                self.letters[i] = self.word[i]    
        #Print out the underscores for the word joined by a space before each guess
        self.current.set("The current word is: " + " ".join(self.letters))
    #Thread to prevent the GUI from crashing
    def threading3(self):
        t3 = Thread(target = self.play)
        t3.start()
    #Player begins guessing by choosing what to guess
    def spin(self):
        self.entry.set("")
        self.text.set("")
        self.spin = random.choice(wheel)
        if self.spin == 1:
            self.addPoints = 1
            self.person.set(fortune[0])
            self.directions.set("Type a letter and type LETTER to guess.")
        elif self.spin == 2:
            self.addPoints = 2
            self.person.set(fortune[1])
            self.directions.set("Type a letter and type LETTER to guess.")
        elif self.spin == 3:
            self.addPoints = 3
            self.person.set(fortune[2])
            self.directions.set("Type a letter and type LETTER to guess.")
        elif self.spin == 4:
            self.addPoints = 4
            self.person.set(fortune[3])
            self.directions.set("Type a letter and type LETTER to guess.")
        elif self.spin == 5:
            self.addPoints = 5
            self.person.set(fortune[4])
            self.directions.set("Type a letter and type LETTER to guess.")
        elif self.spin == 6:
            self.addPoints = 6
            self.person.set(fortune[5])
            self.directions.set("Type a letter and type LETTER to guess.")
        elif self.spin == 7:
            self.addPoints = 7
            self.person.set(fortune[6])
            self.directions.set("Type a letter and type LETTER to guess.")
        elif self.spin == 8:
            self.addPoints = 8
            self.person.set(fortune[7])
            self.directions.set("Type a letter and type LETTER to guess.")
        elif self.spin == 9:
            self.addPoints = 9
            self.person.set(fortune[8])
            self.directions.set("Type a letter and type LETTER to guess.")
        elif self.spin == 10:
            self.addPoints = 10
            self.person.set(fortune[9])
            self.directions.set("Type a letter and type LETTER to guess.")
        elif self.spin == "L":
            self.person.set(fortune[10])
            #Change players
            if self.name.get() == self.player1:
                self.name.set(self.player2)
                self.spin = 0
                self.directions.set("Press SPIN to spin the wheel.")
            else:
                self.name.set(self.player1)
                self.spin = 0
                self.directions.set("Press SPIN to spin the wheel.")
        elif self.spin == "B":
            self.person.set(fortune[11])
            #Change players
            if self.name.get() == self.player1:
                self.name.set(self.player2)
                self.score1 = 0
                self.points1.set(self.score1)
                self.spin = 0
                self.directions.set("Press SPIN to spin the wheel.")
            else:
                self.name.set(self.player1)
                self.score2 = 0
                self.points2.set(self.score2)
                self.spin = 0
                self.directions.set("Press SPIN to spin the wheel.")
    #Player guesses a letter
    def letter(self):
        if self.spin == 0:
            self.directions.set("You must press SPIN before you can guess a letter.")
        else:    
            #Player guess input
            self.guess = self.entry.get()
            while True:
                #Break if user guesses a letter in the list of choices
                if self.guess in self.choices:
                    break
                #Repeat input message if user guesses something not in the choices list
                else:
                    self.text.set("You either guessed that letter, or you typed something else.")
                    self.entry.set("")
                    #self.directions.set("Press GUESS to guess again.")
            #For correct guess
            if self.guess.lower() in list(self.word):
                 self.text.set("You are correct!")
                 self.directions.set("Press SPIN to spin the wheel.")
                 self.entry.set("")
                 #self.directions.set("Press GUESS.")
                 
                 #Iterate through the word to change all instances of a correct
                 #guess from underscores to the letter
                 for i in range(len(self.word)):
                     self.character = self.word[i]
                     if self.character == self.guess:
                         self.letters[i] = self.word[i]
                 #Print out the underscores for the word joined by a space before each guess
                 self.current.set("The current word is: " + " ".join(self.letters))
                 #This adds to the user's score based on the number of times
                 #the correct guess appears in the word.
                 #First we check which player is guessing
                 if self.name.get() == self.player1:
                     self.addScore = self.letters.count(self.guess) * self.addPoints
                     self.score1 = self.score1 + self.addScore
                     self.points1.set(self.score1)
                 else:
                     self.addScore = self.letters.count(self.guess) * self.addPoints
                     self.score2 = self.score2 + self.addScore
                     self.points2.set(self.score2)
            #Wrong guess
            else:
                self.text.set("Sorry, that letter is not in the word.")
                self.entry.set("")
                #self.directions.set("Press GUESS.")
                #Change players
                if self.name.get() == self.player1:
                    self.name.set(self.player2)
                    self.directions.set("Press SPIN to spin the wheel.")
                else:
                    self.name.set(self.player1)
                    self.directions.set("Press SPIN to spin the wheel.")
            #Remove the player's guess from the choices list so that it is no
            #longer an option
            self.choices.remove(self.guess)
            self.lettersGuessed.append(self.guess) 
            self.letterBank.set(sorted(self.lettersGuessed))
            self.spin = 0
            #Check if game ends because player guessed all letters in the word
            if "_" not in self.letters:
                self.directions.set("You guessed the word! To play again press PLAY.")
                self.answer.set(self.word)
    #Thread to prevent the GUI from crashing
    def threading5(self):
        t5 = Thread(target = self.letter)
        t5.start()
    #Player guesses the word
    def wordguess(self):
        self.guess = self.entry.get()
        #If correct, add to player score and break loop
        if self.guess.lower() == self.word:
            self.directions.set("Correct! To play again press PLAY.")
            self.answer.set(self.word)
            self.spin = 0
            if self.name.get() == self.player1:
                self.score1 = self.score1 + 10
                self.points1.set(self.score1)
                self.name.set(self.player2)
            else:
                self.score2 = self.score2 +10
                self.points2.set(self.score2)
                self.name.set(self.player1)
        #If player guess incorrect
        else:
            self.text.set("Sorry, that's not the correct word or spelling.")
            self.spin = 0
            if self.name.get() == self.player1:
                self.name.set(self.player2)
            else:
                self.name.set(self.player1)
    #Thread to prevent the GUI from crashing
    def threading6(self):
        t6 = Thread(target = self.wordguess)
        t6.start()
        
    #Take user back to main menu
    def mainMenu(self):
        self.master.destroy()
    #Exit the system
    def exit(self):
        root.destroy()

#####################################
#RUN SCRIPT
#####################################
#Main function that runs the tkinter framework
if __name__ == "__main__":
    #main()
    root = tk.Tk()
    root.geometry('500x500')
    root.resizable(0,0)
    root.title("Thompson-Hangman")
    root.config(bg ='LightCyan2')
    app = MainMenu(root)
    
    
    
    root.mainloop()