import PySimpleGUI as sg

def make_window(content,choice1,choice2):
    layout =[[sg.Text(content)],[sg.Button(choice1),sg.Button(choice2)]]
    return sg.Window('Light house', layout, finalize=True)

window0,window1,window2= sg.Window("Light house",[[sg.Text("Welcome to my game")],[sg.Button("Start"),sg.Button("Exit")]],finalize=True),None,None

def lightHouseGUI():
    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Exit'or event=="Restart":
            window.close()
            if window == window2:       # if closing win 2, mark as closed
                window2 = None
            elif window == window0:     # if closing win 1, exit program
                break
        if event == "Start" or event == "Restart":
            window1= make_window("Welcome To the lighthouse,\n You just wake up to find yourself in a cold room with nothing\nbut darkness around, outside only the sound of the ocean and cold gale while you \nlying on the, cold dirty floor. Suddenly loud noise can be hear outside. Looking out the window,\nyou saw a dark shadow with claw climb up the light house.\nWhat do you want to do?",'Jump out the window','Try to escape')
        elif event == "Jump out the window":
            window1.close()
            window2 = make_window("You jump out the window and try to grab the Monster to die with you. \nWhen both of you are falling, you remove the mask to see yourself with a happy smile. The monster whisper in your ear: \n'Wear the mask if you want something new'\nDo you want to wear the mask?","Wear the mask","Just die")
        elif event == "Try to escape":
            window1.close()
            window2 = make_window("Looking at the door tightly locked door. What would you do?","Look for key","Ram the door")
        elif event == "Ram the door":
            window2.close()
            window1 = make_window("You dislocate your shouder and try to look for key instead. but the monster catch up\nSo you die. Too bad.","Restart","Quit")
        elif event == "Look for key":
            window2.close()
            window1 =make_window("Lucky the key is in your pocket somehow. You unlock the door and want to go down the stair but the stair is broken. What do you do?", \
                    "Find a Rope","Jump down")
        elif event == "Find a Rope":
            window1.close() 
            window2 = make_window("Running back you facing the monster. there is a sword nearby\nWould you take the sword and fight for your last chance?","Fight","Beg for Mercy")
        elif event == "Fight":
            window2.close()
            window1 =make_window("Taking the sword and fight for your life. Surpisingly, you seem to know\nThe monster movement like yourself and you win after stabing it heart. Upon\ncoming closer and remove the mask, you saw your face smiling in relieve. \nLooking at the mask, look like it is pulling you over. What would you do?", "Wear the mask","Stab yourself")
        elif event == "Beg for Mercy":
            window2.close()
            window1 =make_window("Too scared from looking at the monster. You begged for your life. Seem like u didnt watch much\nscary movie, why begging then you will die anyway num num. Dont need to say much, You die", \
                    "Restart","Quit")
        elif event =="Stab yourself":
            window1.close()
            window2 =make_window(".Waking up in your room feeling unreal but relieved. Suddenly, you Feel tired and want to go back to sleep.\nWould you sleep again?\n*Note: This is the closest thing of winning this game. Be proud", \
                    "Restart","Quit")
        elif event == "Jump down":
            window1.close() 
            window2 = make_window("you over jump and hurt your leg. The Monster catch up quickly and you die. lol ",\
            "Restart","Quit")
        elif event == "Just die":
            window2.close()
            window1 =make_window("You die, pretty sad, want to start again?", "Restart","Quit")
        elif event == "Wear the mask":
            window2.close()
            window1=make_window("The Monster is inside you and you are the monster, You will keep hunting yourself till you die","Restart","Quit")
if __name__== "__main__":
    lightHouseGUI()
    

# Trying to stay in the same window
# layout = [[sg.Text("Welcome To the lighthouse,\n You just wake up to find yourself in a cold room with nothing\n\
#                     but darkness around, outside only the sound of the ocean and cold gale while you \n\
#                     lying on the, cold dirty floor. Suddenly loud noise can be hear outside. Looking out the window,\n\
#                     you saw a dark shadow with claw climb up the light house.\n\
#                     What do you want to do?",key='-TEXT-') ],\
#         # [sg.Button('Jump out the window',visible=False,key='-14-'), sg.Button('Try to escape',visible=False,key='-16-')],\
#         [sg.Button('Take the mask',visible=False,key='-13-'), sg.Button('Just die, lol',visible=False,key='-14-')],\
#         [sg.Button('Restart',visible=False,key='-11-'), sg.Button('Quit',visible=False,key='-12-')],\
#         [sg.Button('Take the mask',visible=False,key='-9-'), sg.Button('Smash it',visible=False,key='-10-')],\
#         [sg.Button('Fight back',visible=False,key='-7-'), sg.Button('Beg for your life',visible=False,key='-8-')],\
#         [sg.Button('Go back to find a rope',visible=False,key='-5-'), sg.Button('Try to jump',visible=False,key='-6-')],\
#         [sg.Button('Look for key',visible=False,key='-3-'), sg.Button('Ram the door',visible=False,key='-4-')],\
#         [sg.Button('Jump out the window',key='-1-'), sg.Button('Try to escape',key='-2-')]]

# # Create the window
# window = sg.Window('Light house', layout)

# # Display and interact with the Window using an Event Loop

# def choice(content,option1,option2):
#     window[f'-{option1}-'].update(visible=False)
#     window[f'-{option1+1}-'].update(visible=False)
#     window['-TEXT-'].update(content)
#     window[f'-{option2}-'].update(visible=True)
#     window[f'-{option2+1}-'].update(visible=True)

#     # See if user wants to quit or window was closed

#     # Output a message to the window
# while True:
#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED or event == 'Quit':
#         break
#     if event =='-1-':    
#         choice("You jump out the window and try to grab the Monster to die with you. When both of you are falling, you remove the mask to see yourself with a happy smile. The monster whisper in your ear:\n'Wear the mask if you want something new':\n "\
#             ,1,13)
#     if event =='-2-':
#         choice("Looking at the door tightly locked door. What would you do?",1,3)
#     if event =='-3-':
#         choice("Lucky the key is in your pocket somehow. You unlock the door and want to go down the stair but the stair is broken. What do you do?",3,5)
#     if event =='-4-':
#         choice()
#     if event =='-5-':
#         choice()
#     if event =='-6-':
#         choice()
#     if event =='-7-':
#         choice()
#     if event =='-8-':
#         choice()
#     if event =='-9-':
#         choice()
#     if event =='-10-':
#         choice()
#     if event =='-11-':
#         event, values = window.read()
#         break
# # Finish up by removing from the screen
# window.close()