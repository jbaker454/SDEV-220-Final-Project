import asyncio
import threading
import Data_Handler
import UI_Handler

def main():
    
    threading.Thread(target=start_asycronous_thread()).start()
    window = UI_Handler.widgets.Widget.get_instance(UI_Handler.widgets.Widget,"Wonkas Chocolate")
    window.mainloop()

def start_asycronous_thread():
    """set up for seperate thread"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(event_main())
    loop.close()

async def event_main():
    """an asyncronous funtion for events"""
    mainToInventoryButton = UI_Handler.widgets.Widget.get_instance(UI_Handler.widgets.Widget,"mainToInventoryButton")
    mainToInventoryButton.bind("<Button-1>", lambda event, newMenu="inventorymenuFrame": change_menu(newMenu))

    inventoryToMainButton = UI_Handler.widgets.Widget.get_instance(UI_Handler.widgets.Widget,"inventoryToMainButton")
    inventoryToMainButton.bind("<Button-1>", lambda event, newMenu="mainMenuFrame": change_menu(newMenu))

    inventoryToShipmentButton = UI_Handler.widgets.Widget.get_instance(UI_Handler.widgets.Widget,"inventoryToShipmentButton")
    inventoryToShipmentButton.bind("<Button-1>", lambda event, newMenu="shipmentMenuFrame": change_menu(newMenu))

    inventoryToOrderButton = UI_Handler.widgets.Widget.get_instance(UI_Handler.widgets.Widget,"inventoryToOrderButton")
    inventoryToOrderButton.bind("<Button-1>", lambda event, newMenu="orderMenuFrame": change_menu(newMenu))

    shipmentToInventoryButton = UI_Handler.widgets.Widget.get_instance(UI_Handler.widgets.Widget,"shipmentToInventoryButton")
    shipmentToInventoryButton.bind("<Button-1>", lambda event, newMenu="inventorymenuFrame": change_menu(newMenu))

    orderToInventory = UI_Handler.widgets.Widget.get_instance(UI_Handler.widgets.Widget,"orderToInventory")
    orderToInventory.bind("<Button-1>", lambda event, newMenu="inventorymenuFrame": change_menu(newMenu))

def change_menu(newMenuName):
    UI_Handler.change_menu(newMenuName)

main()