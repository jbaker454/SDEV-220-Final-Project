import TKinter_Wrapper as widgets


def initilizeConfigurations():
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

initilizeConfigurations()

window = widgets.Widget.get_instance(widgets.Widget,"Wonkas Chocolate")
window = widgets.Window(name="Bible CardDeck Simulation", size=[1000,600])

EventTest = widgets.Widget.get_instance(widgets.Widget,"EventTest")
EventTest = widgets.CustomButton(
           name="EventTest", parent=window, size=[10,2], 
           config=widgets.Config.getCustomConfigByName(widgets.Config,"Yellow"), **{"text":"back"})
EventTest.place(x=730,y=485)

