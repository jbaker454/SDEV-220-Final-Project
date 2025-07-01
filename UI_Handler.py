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

    eventTest = widgets.Widget.get_instance(widgets.Widget,"eventTest")
    eventTest = widgets.CustomButton(
           name="eventTest", parent=window, size=[10,2], 
           config=widgets.Config.getCustomConfigByName(widgets.Config,"Yellow"), **{"text":"back"})
    eventTest.place(x=730,y=485)

main_UI()

