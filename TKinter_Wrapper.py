#Tkinter wrapper for scrolling frame and naming
import tkinter as tk

tkinterAttributes = {
    "widgetName","master","tk","_name","_w","children","_tclCommands","_last_child_ids"
}

def getGeometryManager(widget):
    try:
        widget.place_info()
        return "place"
    except:
        pass
    try:
        widget.pack_info()
        return "pack"
    except:
        pass
    try:
        widget.grid_info()
        return "grid"
    except:
        pass
    return "None"

#UI config

class Config():
    instances = {}
    def __init__(self, configName = "name", configDict = {"key":"value"}):
        self.__class__.instances[configName] = self
        self.configName = configName
        self.configDict = configDict

    def getCustomConfigByName(cls, configName):
        """Retrieve an instance by its name, ensuring it returns a dictionary."""
        instance = cls.instances.get(configName)

        if hasattr(instance, "configDict") and isinstance(instance.configDict, dict):
            return instance.configDict

        raise TypeError(f"Expected a dictionary in instance '{configName}', but got {type(instance).__name__}")

#UI widgets

class Widget:
    instances = {}
    def __init__(self, name, size, config=None):
        self.__class__.instances[name] = self
        self.name = name
        self.size = size
        self.config = config
        if config != None:
            self.configure(**config)
        if size[1] == None:
            self.configure(width=size[0])
        else:
            self.configure(width=size[0], height=size[1])

    def get_instance(cls, name):
        """Retrieve an instance by its name."""
        return cls.instances.get(name)
    
    def reparentWidget(self, newParent, newLocation, offset = 6):
        """reparents a widget by reconstruction"""
        widgetClass = type(self)

        widgetAttributes = {key: value for key, value in self.__dict__.items() if key not in tkinterAttributes}

        widgetAttributes["parent"] = newParent

        del Widget.instances[widgetAttributes["name"]]
        newWidget = widgetClass(**widgetAttributes)

        if widgetClass != ScrollingFrame:
            children = self.winfo_children()
        else:
            children = self.scrollable_frame.winfo_children()
        
        for child in children:
            childLocation = [child.winfo_x(),child.winfo_y()]
            child.reparentWidget(newWidget,childLocation, offset = offset +- 2)

        geometry = getGeometryManager(self)
        if geometry == "place":
            newWidget.place(x=newLocation[0] - offset,y=newLocation[1] - offset)
        elif geometry == "grid":
            newWidget.grid(column=newLocation[0] - offset,row=newLocation[1] - offset)
        elif geometry == "pack":
            newWidget.pack(x=newLocation[0] - offset,y=newLocation[1] - offset)
        else:
            pass
        
        self.destroy()

class Window(Widget, tk.Tk):
    def __init__(self, name, size):
        tk.Tk.__init__(self)
        Widget.__init__(self, name, size)
        self.title(name)

class ScrollingFrame(Widget, tk.Frame):
    def __init__(self, name, size, config, canvasConfig, parent, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        Widget.__init__(self, name, size, config)
        self.canvasConfig = canvasConfig

        self.canvas = tk.Canvas(self, width=size[0] - 17, height=size[1], **canvasConfig)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame = tk.Frame(self.canvas)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        self.scrollbar.pack(side="right", fill="y",padx=2,pady=2)
        self.canvas.pack(side="left", fill="both", expand=True,ipadx=2,ipady=2)

        self.scrollable_frame.bind(
            "<Configure>", 
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.bind("<MouseWheel>", self.onMouseWheel)

        self.pack(fill="both", expand=True)

    def addWidget(self, widget, gridPosition):
        """add a widget to the scrolling frame"""
        widget.grid(column=gridPosition[0], row=gridPosition[1])
        widget.bind("<MouseWheel>", self.onMouseWheel)
    
    def onMouseWheel(self, event):
        """event for controlling scrolling"""
        self.canvas.yview_scroll(-1 if event.delta > 0 else 1, "units")
    
class CustomFrame(Widget, tk.Frame):
    def __init__(self, name, size, config, parent, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        Widget.__init__(self, name, size, config)

class CustomLabel(Widget, tk.Label):
    def __init__(self, name, size, config, parent, **kwargs):
        tk.Label.__init__(self, parent, **kwargs)
        Widget.__init__(self, name, size, config)

class CustomEntry(Widget, tk.Entry):
    def __init__(self, name, size, config, parent, **kwargs):
        tk.Entry.__init__(self, parent, **kwargs)
        Widget.__init__(self, name, [size[0],None], config)

class CustomButton(Widget, tk.Button):
    def __init__(self, name, size, config, parent, **kwargs):
        tk.Button.__init__(self, parent, **kwargs)
        Widget.__init__(self, name, size, config)
