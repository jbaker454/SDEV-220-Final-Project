import asyncio
import threading
import Data_Handler
import UI_Handler

def main():
    
    threading.Thread(target=start_step_event()).start()
    UI_Handler.window.mainloop()

def start_step_event():
    """set up for seperate thread"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(event_main())
    loop.close()

async def event_main():
    UI_Handler.EventTest.bind("<Button-1>", lambda event, newMenu="mainMenuFrame": changeMenu(newMenu))

def changeMenu(newMenuName):
    print(newMenuName)

main()