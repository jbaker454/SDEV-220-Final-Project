import asyncio
import threading
import Data_Handler
import UI_Handler

class UI_Publisher ():
    pass

class UI_Event_Reciever ():
    def bind_events():
        shipmentAddButton = UI_Handler.widgets.Widget.get_instance(UI_Handler.widgets.Widget,"shipmentAddButton")
        shipmentAddButton.bind("<Button-1>", func())

        orderAddButton = UI_Handler.widgets.Widget.get_instance(UI_Handler.widgets.Widget,"shipmentAddButton")
        orderAddButton.bind("<Button-1>", func())     

class Data_Publisher ():
    pass

class Data_Reciever ():
    pass

def main():
    """main function for window and program start"""
    UI_Handler.main_UI()
    threading.Thread(target=start_asycronous_thread()).start()
    window = UI_Handler.widgets.Widget.get_instance(UI_Handler.widgets.Widget,"Wonkas Chocolate")
    window.mainloop()

def start_asycronous_thread():
    """set up for seperate thread for program"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(event_main())
    loop.close()

async def event_main():
    """an asyncronous funtion for events"""
    UI_Event_Reciever.bind_events()

def func():
    pass

main()

