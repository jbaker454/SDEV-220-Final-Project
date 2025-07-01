import asyncio
import threading
import Data_Handler
import UI_Handler

def main():
    
    threading.Thread(target=start_step_event()).start()
    window = UI_Handler.widgets.Widget.get_instance(UI_Handler.widgets.Widget,"Wonkas Chocolate")
    window.mainloop()

def start_step_event():
    """set up for seperate thread"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(event_main())
    loop.close()

async def event_main():
    eventTest = UI_Handler.widgets.Widget.get_instance(UI_Handler.widgets.Widget,"eventTest")
    eventTest.bind("<Button-1>", lambda event, newMenu="mainMenuFrame": change_menu(newMenu))

def change_menu(newMenuName):
    print(newMenuName)

main()