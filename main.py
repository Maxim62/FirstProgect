
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.core.window import Window

class MainScreen(Screen):
	pass

class PravScreen(Screen):
	pass

class St_18_Screen(Screen):
	with open('Text_dlya_kivy/Statya_18.txt', 'r', encoding='utf-8') as t: 
		text = StringProperty(t.read())

class St_19_Screen(Screen):
	with open('Text_dlya_kivy/Statya_19.txt', 'r', encoding='utf-8') as t: 
		text = StringProperty(t.read())	

class St_23_Screen(Screen):
	with open('Text_dlya_kivy/Statya_23.txt', 'r', encoding='utf-8') as t: 
		text = StringProperty(t.read())
		
class St_24_Screen(Screen):
	with open('Text_dlya_kivy/Statya_24.txt', 'r', encoding='utf-8') as t: 
		text = StringProperty(t.read())

class MenuScreen(Screen):
	pass 	

class MeryScreen(Screen):
	with open('Text_dlya_kivy/Mery_bez.txt', 'r', encoding='utf-8') as t: 
		text = StringProperty(t.read())

class PmScreen(Screen):
	pass

class ObshPmScreen(Screen):
	with open('Text_dlya_kivy/Nazn_pm.txt', 'r', encoding='utf-8') as f: 
		text = StringProperty(f.read())
	
class RazbPmScreen(Screen):
	pass

class UstrPmScreen(Screen):
	pass

class WorkPmScreen(Screen):
	pass

class LookPmScreen(Screen):
	pass

class CheckPmScreen(Screen):
	pass

class AkScreen(Screen):
	pass

class DeistvScreen(Screen):
	pass

class Deistv_pmScreen(Screen):
	with open('Text_dlya_kivy/Deistviya_pm.txt', 'r', encoding='utf-8') as t:	
		text = StringProperty(t.read())

class Deistv_akScreen(Screen):
	with open('Text_dlya_kivy/Deistviya_ak.txt', 'r', encoding='utf-8') as t:	
		text = StringProperty(t.read())

class Norm_pmScreen(Screen):
	pass

class Norm1pmScreen(Screen):
	with open('Text_dlya_kivy/Norm_pm_1.txt', 'r', encoding='utf-8') as t:	
		text = StringProperty(t.read())

class Norm2pmScreen(Screen):
	with open('Text_dlya_kivy/Norm_pm_2.txt', 'r', encoding='utf-8') as t:	
		text = StringProperty(t.read())

class Norm3pmScreen(Screen):
	with open('Text_dlya_kivy/Norm_pm_3.txt', 'r', encoding='utf-8') as t:	
		text = StringProperty(t.read())

class Norm4pmScreen(Screen):
	with open('Text_dlya_kivy/Norm_pm_4.txt', 'r', encoding='utf-8') as t:	
		text = StringProperty(t.read())

class Norm5pmScreen(Screen):
	with open('Text_dlya_kivy/Norm_pm_5.txt', 'r', encoding='utf-8') as t:	
		text = StringProperty(t.read())


class Norm6pmScreen(Screen):
	with open('Text_dlya_kivy/Norm_pm_6.txt', 'r', encoding='utf-8') as t:	
		text = StringProperty(t.read())

class ScreenManager(ScreenManager):
	pass

class TestApp(App):
	#def build(self):
	#	Window.clearcolor =  1, 204/255, 153/255, 1
	pass
	

if __name__ == '__main__':
	TestApp().run()
