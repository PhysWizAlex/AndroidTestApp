import certifi
import json
import kivy
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem, MDList
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker
from kivy.network.urlrequest import UrlRequest

Builder.load_file('whatever.kv')

class MyLayout(Widget):
    def select_start_date(self,instance,value,date_range):
        self.ids.start_date_label.text = str(value)
        
    def select_end_date(self,instance,value,date_range):
        self.ids.end_date_label.text = str(value)
               
    def selected_object(self, objId):
        responsekivy = UrlRequest("https://api.nasa.gov/neo/rest/v1/neo/" + str(objId) + "?api_key=eLLQHjpU93iCInMRF8Cvrm3x2wLoQrtDGsinjF48",ca_file=certifi.where())
        responsekivy.wait()
        results = responsekivy.result
        estDiameter = results['estimated_diameter']['meters']
        CAD = results['close_approach_data']
        loadedDump = results['orbital_data']
        
        self.ids.ap.text = 'Aphelion (Furtherst) Distance (AU): ' + str(round(float(loadedDump['aphelion_distance']),2))
        self.ids.per.text = 'Perihelion (Closest) Distance (AU): ' + str(round(float(loadedDump['perihelion_distance']),2))
        self.ids.per_arg.text = 'Perihelion Argument (deg): ' + str(round(float(loadedDump['perihelion_argument']),2))
        self.ids.orb_period.text = 'Orbital Period (Days): ' + str(round(float(loadedDump['orbital_period']),2))
        self.ids.mean_motion.text = 'Mean Motion (deg/d): ' + str(round(float(loadedDump['mean_motion']),2))
        self.ids.sem_maj_ax.text = 'Semi Maj Ax. (AU): ' + str(round(float(loadedDump['semi_major_axis']),2))
        self.ids.asc_node_long.text = 'Ascending Node Longitude (deg): ' + str(round(float(loadedDump['ascending_node_longitude']),2))
        self.ids.incl.text = 'Inclination (deg): ' + str(round(float(loadedDump['inclination']),2))
        self.ids.est_dia.text = 'Est. Diameter (meters)(max/min): ' + str(round(estDiameter['estimated_diameter_max'],2)) + '/' + str(round(estDiameter['estimated_diameter_min'],2))
            
    def search(self):
        startDate = self.ids.start_date_label.text
        endDate = self.ids.end_date_label.text
        response = UrlRequest("https://api.nasa.gov/neo/rest/v1/feed?start_date=" + startDate + "&end_date=" + endDate + "&api_key=eLLQHjpU93iCInMRF8Cvrm3x2wLoQrtDGsinjF48")
        response.wait()
        results = response.result
        idList = []
        objectNames = []
        allObjects = results['near_earth_objects']
        keyList = list(allObjects.keys())
        for i in range(len(allObjects)):
            for j in range(len(allObjects[keyList[i]])):
                idList.append(int(allObjects[keyList[i]][j]['id']))
                objectNames.append(allObjects[keyList[i]][j]['name'])
        for i in range(len(objectNames)):
            self.ids.list_of_objects.add_widget(TwoLineListItem(text='Name: ' + objectNames[i], 
                                                                secondary_text='Object SPK ID: ' + str(idList[i]),
                                                                on_release = lambda x, objId = idList[i]: self.selected_object(objId)))
            
    def show_date_picker(self,button_pressed):
        date_dialog = MDDatePicker()
        if button_pressed.name == 1:
            date_dialog.bind(on_save=self.select_start_date)
            date_dialog.open()
        if button_pressed.name == 2:
            date_dialog.bind(on_save=self.select_end_date)
            date_dialog.open()   
            
    
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.accent_palette = 'Red'
        return MyLayout()
    
if __name__ == '__main__':
    MainApp().run()