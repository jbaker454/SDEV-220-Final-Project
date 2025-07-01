import Data_Handler
import UI_Handler

def main():
    UI_Handler.window.mainloop()

    UI_Handler.EventTest.bind("<Button-1>", lambda event, newMenu="mainMenuFrame": testFuntion())

def testFuntion():
    pass

main()