"""
Seizure Tracking Application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import pandas as pd
import numpy as np
from calculations import data_calc

#from data_calcs import test

class seizuretracker(toga.App):

    def startup(self):
        
        # Main Box
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Hours of sleep
        self.sleep_hours = 0

        label_sleep = toga.Label(
            'How many hours of sleep did you get last night (0 - 10 or more)'
        )

        # Hours of sleep slider
        def set_hours_of_sleep(widget):
            self.sleep_hours = sleep_slider.value
        
        sleep_slider = toga.Slider(
            on_change = set_hours_of_sleep,
            style=Pack(flex=1,padding=10),
            range=(0,10),
            tick_count = 11,
            value = 0.0 
        )
        
        main_box.add(label_sleep)
        main_box.add(sleep_slider)

        # Alcohol consumption
        self.alcohol_consumption = 0

        label_alcohol_consumption = toga.Label(
            'How many alcoholic beverages have you consumed in the past 24 hours? (0 - 3 or more)'
        )

        def set_alcohol_consumption(widget):
            self.alcohol_consumption = alcohol_slider.value
        
        alcohol_slider = toga.Slider(
            on_change = set_alcohol_consumption,
            style=Pack(flex=1,padding=10),
            range=(0,3),
            tick_count = 4, # range from 0 to 3 or more
            value = 0.0
        )
        
        main_box.add(label_alcohol_consumption)
        main_box.add(alcohol_slider)

        # Stress level
        self.stress_level = 0

        label_stress_level = toga.Label(
            'How stressed do you feel right now? (Not at all to Very Stressed)'
        )

        def update_stress_level(widget):
            self.stress_level = stress_slider.value
        
        stress_slider = toga.Slider(
            on_change = update_stress_level,
            style=Pack(flex=1,padding=10),
            range=(0,3),
            tick_count = 4, # range from 0 to 3 or more
            value = 0.0
        )
        
        main_box.add(label_stress_level)
        main_box.add(stress_slider)

        # Medication
        self.took_medication = False

        def set_medication_true(widget):
            self.took_medication = True
            print(self.took_medication)

        def set_medication_false(widget):
            self.took_medication = False
            print(self.took_medication)
        
        label_medication = toga.Label(
            'Have you taken medication?'
        )

        button_yes_medication = toga.Button(
            'Yes',
            on_press = set_medication_true,
            style=Pack(padding_top=20)
        )
        
        button_no_medication = toga.Button(
            'No',
            on_press = set_medication_false,
            style=Pack(padding_top=20)
        )

        box_took_medication = toga.Box() 
        box_took_medication.add(button_yes_medication)
        box_took_medication.add(button_no_medication)

        main_box.add(label_medication)
        main_box.add(box_took_medication)
        
        # Menstruation
        self.menstruating = False

        def set_menstruate_true(widget):
            self.menstruating = True
            print(self.menstruating)

        def set_menstruate_false(widget):
            self.menstruating = False
            print(self.menstruating)
        
        label_menstrual_cycle = toga.Label(
            'Are you currently menstruating?'
        )

        button_yes_menstruate = toga.Button(
            'Yes',
            on_press=set_menstruate_true,
            style=Pack(padding_top=20)
        )

        button_no_menstruate = toga.Button(
            'No',
            on_press = set_menstruate_false,
            style=Pack(padding_top=20)
        )

        box_on_menstrual_cycle = toga.Box() 
        box_on_menstrual_cycle.add(button_yes_menstruate)
        box_on_menstrual_cycle.add(button_no_menstruate)

        main_box.add(label_menstrual_cycle)
        main_box.add(box_on_menstrual_cycle)

        #Submit and calculate
        self.output_label = toga.Label('')
        self.calculated_risk = 0

        def update_output_label(widget):
            self.calculated_risk = data_calc.calculate_risk(True, self.took_medication, self.alcohol_consumption, self.stress_level, self.sleep_hours, self.menstruating)
            self.output_label.text = f"Your risk of having a seizure today is {int(self.calculated_risk)}%"
        
        button_submit = toga.Button(
            'Calculate Risk',
            on_press=update_output_label,
            style=Pack(padding_top=20)
        )

        main_box.add(button_submit)
        main_box.add(self.output_label)

        self.main_window = toga.MainWindow(title='Seizure Tracker')
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return seizuretracker()