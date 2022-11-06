"""
Seizure Tracking Application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import pandas as pd
import numpy as np
import data_calcs

#from data_calcs import test

class seizuretracker(toga.App):

    def startup(self):
        
        # Main Box
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Hours of sleep
        self.sleep_hours = toga.Label('')

        label_sleep = toga.Label(
            'How many hours of sleep did you get last night (0 - 10 or more)'
        )

        # Hours of sleep slider
        def set_hours_of_sleep(widget):
            self.sleep_hours.text = f"Hours of sleep: {sleep_slider.value}"
            yield 0
        
        sleep_slider = toga.Slider(
            on_slide = set_hours_of_sleep,
            style=Pack(flex=1,padding=10),
            range=(0,10),
            tick_count = 11,
            value = 0.0 
        )
        
        main_box.add(label_sleep)
        main_box.add(sleep_slider)
        main_box.add(self.sleep_hours)

        # Alcohol consumption
        label_alcohol_consumption = toga.Label(
            'How many alcoholic beverages have you consumed in the past 24 hours? (0 - 3 or more)'
        )

        def get_alcohol_use(widget):
            print(alcohol_slider.value)
        
        alcohol_slider = toga.Slider(
            on_slide = get_alcohol_use,
            style=Pack(flex=1,padding=10),
            range=(0,3),
            tick_count = 4, # range from 0 to 3 or more
            value = 0.0
        )
        
        main_box.add(label_alcohol_consumption)
        main_box.add(alcohol_slider)

        # Alcohol consumption
        label_stress_level = toga.Label(
            'How stressed do you feel right now? (None at all to Very Stressed)'
        )

        def get_stress_level(widget):
            print(stress_slider.value)
            return stress_slider.value
        
        stress_slider = toga.Slider(
            on_slide = get_stress_level,
            style=Pack(flex=1,padding=10),
            range=(0,3),
            tick_count = 4, # range from 0 to 3 or more
            value = 0.0
        )
        
        main_box.add(label_stress_level)
        main_box.add(stress_slider)

        # Medication
        print("Took Medication")

        label_medication = toga.Label(
            'Have you taken medication?'
        )
        
        box_took_medication = toga.Box() 
        button_yes_medication = toga.Button('Yes')
        button_yes_medication.style.padding_top = 20
        
        button_no_medication = toga.Button('No')
        button_no_medication.style.padding_top = 20

        box_took_medication.add(button_yes_medication)
        box_took_medication.add(button_no_medication)

        main_box.add(label_medication)
        main_box.add(box_took_medication)
        
        # Menstruation
        label_menstrual_cycle = toga.Label(
            'Are you currently menstruating?'
        )

        box_on_menstrual_cycle = toga.Box() 
        button_yes_menstrual = toga.Button('Yes')
        button_yes_menstrual.style.padding_top = 20

        button_no_menstrual = toga.Button('No')
        button_no_menstrual.style.padding_top = 20

        box_on_menstrual_cycle.add(button_yes_menstrual)
        box_on_menstrual_cycle.add(button_no_menstrual)

        main_box.add(label_menstrual_cycle)
        main_box.add(box_on_menstrual_cycle)

        button_submit = toga.Button(
            'Submit',
            on_press=set_hours_of_sleep,
            style=Pack(padding_top=20)
        )
    
        main_box.add(button_submit)

        self.main_window = toga.MainWindow(title='Seizure Tracker')
        self.main_window.content = main_box
        self.main_window.show()

    def show_output_window(self, widget):
        label = toga.Label(f"Hours of sleep:")
        outer_box = toga.Box()
        self.second_window = toga.Window(title='Result')
        self.windows.add(self.second_window)
        self.second_window.content = outer_box
        self.second_window.show()

def main():
    return seizuretracker()