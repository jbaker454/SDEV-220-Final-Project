import TKinter_Wrapper as widgets

def main_UI():
    initilize_configurations()
    UI_creation()

def initilize_configurations():
    widgets.Config("Purple",{"bg":"#634ed0", "highlightthickness":2,"highlightbackground":"#000000", "borderwidth":2})
    widgets.Config("DarkGrey",{"bg":"#3d3d5c","highlightthickness":2,"highlightbackground":"#000000","borderwidth":4})
    widgets.Config("ScrollingFrameBlue",{"bg":"#000099","highlightthickness":2,"highlightbackground":"#000000","borderwidth":4})
    widgets.Config("ScrollingFrameBlue2",{"bg":"#000099","highlightthickness":2,"highlightbackground":"#000000","borderwidth":4})
    widgets.Config("LightBlue",{"bg":"#3377ff","highlightthickness":2,"highlightbackground":"#000000","borderwidth":4})
    widgets.Config("Yellow",{"bg":"#b0f943","highlightthickness":2,"highlightbackground":"#000000","borderwidth":2})
    widgets.Config("DarkBlue",{"bg":"#000066","highlightthickness":2,"highlightbackground":"#000000","borderwidth":2})
    widgets.Config("CardRed",{"bg":"#e60000","highlightthickness":2,"highlightbackground":"#000000","borderwidth":2})
    widgets.Config("CardGreen",{"bg":"#00e600","highlightthickness":2,"highlightbackground":"#000000","borderwidth":2})
    widgets.Config("CardLightBlue",{"bg":"#00e6e6","highlightthickness":2,"highlightbackground":"#000000","borderwidth":2})
    widgets.Config("CardGrey",{"bg":"#8c8c8c","highlightthickness":2,"highlightbackground":"#000000","borderwidth":1})



def UI_creation():
    window = widgets.Widget.get_instance(widgets.Widget,"Wonkas Chocolate")
    window = widgets.Window(name="Wonkas Chocolate", size=[1000,600])

    main_menu_UI(window)
    inventory_menu_UI(window)
    shipment_menu_UI(window)
    order_menu_UI(window)

def main_menu_UI(window):
    mainMenuFrame = widgets.CustomFrame(
           name="mainMenuFrame", parent=window, size=[1000,600], 
           config=widgets.Config.getCustomConfigByName(widgets.Config,"DarkGrey"))
    mainMenuFrame.place(x=0,y=0)

    mainToInventoryButton = widgets.Widget.get_instance(widgets.Widget,"mainToInventoryButton")
    mainToInventoryButton = widgets.CustomButton(
           name="mainToInventoryButton", parent=mainMenuFrame, size=[10,2], 
           config=widgets.Config.getCustomConfigByName(widgets.Config,"Yellow"), **{"text":"Inventory"})
    mainToInventoryButton.place(x=450,y=485)

def inventory_menu_UI(window):
    inventorymenuFrame = widgets.CustomFrame(
           name="inventorymenuFrame", parent=window, size=[1000,600], 
           config=widgets.Config.getCustomConfigByName(widgets.Config,"DarkGrey"))

    inventoryToMainButton = widgets.Widget.get_instance(widgets.Widget,"inventoryToMainButton")
    inventoryToMainButton = widgets.CustomButton(
           name="inventoryToMainButton", parent=inventorymenuFrame, size=[10,2], 
           config=widgets.Config.getCustomConfigByName(widgets.Config,"Yellow"), **{"text":"Main"})
    inventoryToMainButton.place(x=450,y=485)

    inventoryToShipmentButton = widgets.Widget.get_instance(widgets.Widget,"inventoryToShipmentButton")
    inventoryToShipmentButton = widgets.CustomButton(
           name="inventoryToShipmentButton", parent=inventorymenuFrame, size=[10,2], 
           config=widgets.Config.getCustomConfigByName(widgets.Config,"Yellow"), **{"text":"Shipments"})
    inventoryToShipmentButton.place(x=170,y=485)

    inventoryToOrderButton = widgets.Widget.get_instance(widgets.Widget,"inventoryToOrderButton")
    inventoryToOrderButton = widgets.CustomButton(
           name="inventoryToOrderButton", parent=inventorymenuFrame, size=[10,2], 
           config=widgets.Config.getCustomConfigByName(widgets.Config,"Yellow"), **{"text":"Orders"})
    inventoryToOrderButton.place(x=730,y=485)

def shipment_menu_UI(window):
    shipmentMenuFrame = widgets.CustomFrame(
           name="shipmentMenuFrame", parent=window, size=[1000,600], 
           config=widgets.Config.getCustomConfigByName(widgets.Config,"DarkGrey"))

    shipmentToInventoryButton = widgets.Widget.get_instance(widgets.Widget,"shipmentToInventoryButton")
    shipmentToInventoryButton = widgets.CustomButton(
           name="shipmentToInventoryButton", parent=shipmentMenuFrame, size=[10,2], 
           config=widgets.Config.getCustomConfigByName(widgets.Config,"Yellow"), **{"text":"Inventory"})
    shipmentToInventoryButton.place(x=170,y=485)

def order_menu_UI(window):
    orderMenuFrame = widgets.CustomFrame(
           name="orderMenuFrame", parent=window, size=[1000,600], 
           config=widgets.Config.getCustomConfigByName(widgets.Config,"DarkGrey"))

    orderToInventory = widgets.Widget.get_instance(widgets.Widget,"orderToInventory")
    orderToInventory = widgets.CustomButton(
           name="orderToInventory", parent=orderMenuFrame, size=[10,2], 
           config=widgets.Config.getCustomConfigByName(widgets.Config,"Yellow"), **{"text":"Inventory"})
    orderToInventory.place(x=730,y=485)

main_UI()

def change_menu(newMenuName):
    """changes the menu"""
    menuNames = ["mainMenuFrame", "inventorymenuFrame", "shipmentMenuFrame", "orderMenuFrame"]

    for menuName in menuNames:
        menu = widgets.Widget.get_instance(widgets.Widget, menuName)
        menu.place_forget()

    newMenu = widgets.Widget.get_instance(widgets.Widget,newMenuName)
    newMenu.place(x=0,y=0)

