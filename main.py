# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:29:06 2021

@author: -
"""

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import ScreenManager

#define different screen


class testNewWindow(Screen):
    pass

class testSecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class TheLabApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Indigo'
        #defining layouts
        screen = Screen()
        layout = BoxLayout()
        leftPanel = BoxLayout(orientation = 'vertical',size_hint = (0.5,1))
        rightPanel = BoxLayout(orientation = 'vertical')
        
        #adding widgets to left panel
        leftPanel.add_widget(Button(text = 'Select Start Date'))
        leftPanel.add_widget(Label())
        leftPanel.add_widget(Button(text = 'Select End Date'))
        leftPanel.add_widget(Label())
        leftPanel.add_widget(Button(text = 'Search'))
        
        #adding widgets to right panel
        labelList = ['Aphelion (Furthest) Distance (AU): ',
                     'Perihelion (Closest) Distance (AU): ',
                     'Perihelion Argument (deg): ',
                     'Orbital Period (Days): ',
                     'Mean Motion (deg/d): ',
                     'Semi Maj Ax. (AU): ',
                     'Ascending Node Longitude (deg): ',
                     'Inclination (deg): ',
                     'Estimated Diameter (meters): ']
        for i in range(len(labelList)):
            print(i)
            rightPanel.add_widget(Label(text = labelList[i],color = (1,0,0)))
        
        #adding to list
        list_view = MDList()
        scroll_view = ScrollView()
        item1 = OneLineListItem(text = 'item 1')
        item2 = OneLineListItem(text = 'item 2')
        list_view.add_widget(item1)
        list_view.add_widget(item2)
        scroll_view.add_widget(list_view)
        
        layout.add_widget(leftPanel)
        layout.add_widget(scroll_view)
        layout.add_widget(rightPanel)
        screen.add_widget(layout)
        return screen
    
TheLabApp().run()