import numpy as np
import pandas as pd
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class Calculator(toga.App):
    
    def startup(self):
        
        main_box = toga.Box()
        
        self.main_window = toga.MainWindow(title=self.format_name)
        self.main_window.content = main_box
        self.main_window.show()

# Inputs:
medication: bool
sleep: int
stress: int
alcohol: bool or int
menstruation: bool
