import PySimpleGUI as sg
layout = [[]]
win = sg.Window("Virtual Butterfly World", layout)

while True:
    e, v = win.read()
    if e == None :break
win.close()
