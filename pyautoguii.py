import time
import pyautogui as py
def sleep2():
    time.sleep(1)

for i in range(150):
    sleep2()
    #Move to the First Item and copy
    def move2FristItem():
        py.moveTo(2506, 320,1)
        py.hotkey('esc')
        py.leftClick(2506, 320)
        py.hotkey('ctrl', 'c')
    move2FristItem()

    sleep2()

    # Search For the Item Copied Above Code
    def SearchItem():
        py.moveTo(-2091, 273,1)
        py.leftClick(-2091, 273)
        py.hotkey('ctrl','v')
    SearchItem()

    sleep2()

    # Click The First Item Search (Item Number)
    def clickSearchedItem():
        py.leftClick(-2269, 404)
    clickSearchedItem()

    sleep2()

    #Clicked the Blocked Item
    def ClikedBlocked():
        py.moveTo(-1810, 561,2)
        py.leftClick(-1810, 561)
    ClikedBlocked()

    sleep2()

    #Clicked Back Button
    def Click_Back_Button():
        py.moveTo(-2312, 223,1)
        py.leftClick(-2312, 223)
    Click_Back_Button()


    # Clear Search Area
    def searchArea():
        py.moveTo(-1986, 275,1)
        py.leftClick(-1986, 275)
        py.hotkey('ctrl', 'a')
        py.hotkey('backspace')
    searchArea()

    sleep2()

    # Hide the item finished
    def hide_FinishedItems():
        py.moveTo(2855, 506,1)
        py.click(2855, 506)
        py.hotkey('esc')
    hide_FinishedItems()

    sleep2()
    # Hide the item finished
    def Hide_Item():
        py.moveTo(2410, 320,1)
        py.leftClick(2410, 320)
        py.leftClick(2410, 320)
        py.rightClick(2410, 320)
        py.moveTo(2485, 751,1)
        py.leftClick(2485, 751)
    Hide_Item()






