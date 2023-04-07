import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from kivy.uix.carousel import Carousel
from kivy.clock import Clock


Window.size = (750, 650)
Window.top = 50
Window.left = 250


class ExitButton(Button):
    def on_press(self):
        App.get_running_app().stop()    


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        carousel = Carousel(direction='right', loop=True)
        src_list = ["1.jpg", "2.jpg", "8.jpg", "9.jpg", "3.jpg", "4.jpg", "5.jpg", "7.jpg", "6.jpg"]
        for src in src_list:
            image = AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)

        # функция для прокрутки слайдов
        def scroll_callback(dt):
            carousel.load_next()

        # запускаем прокрутку слайдов каждую секунду
        Clock.schedule_interval(scroll_callback, 1.5)

        exit_button = ExitButton(text='Start application')
        exit_button.size_hint = (None, None)
        exit_button.size = (200, 50)
        exit_button.background_color = (0, 1, 0, 1)

        self.add_widget(carousel)
        self.add_widget(exit_button)


class CarouselApp(App):
    def build(self):
        return RootWidget()

CarouselApp().run()

    
class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'


        # создаем экземпляры кнопок
        btn1 = Button(text='Ukraine',
                      background_normal="ukraine.jpg")
        btn1.bind(on_press=lambda instance: self.show_popup("Ukraine (Ukrainian: Україна, romanized: Ukraïna, pronounced [ʊkrɐˈjinɐ] is a country in Eastern Europe. It is the second-largest European country after Russia, which it borders to the east and northeast. Ukraine covers approximately 600,000 square kilometres (230,000 sq mi).[b] Prior to the ongoing Russian invasion, it was the eighth-most populous country in Europe, with a population of around 41 million people. On 1 January 2023, the United Nations estimated the Ukrainian population to be 34.1 million, with record low birth rates. It is also bordered by Belarus to the north; by Poland, Slovakia, and Hungary to the west; and by Romania and Moldova to the southwest; with a coastline along the Black Sea and the Sea of Azov to the south and southeast. Kyiv is the nation's capital and largest city. Ukraine's state language is Ukrainian", "ukraine-2.jpg", instance))

        btn2 = Button(text='Flag',
                      background_normal="flag.jpg")
        btn2.bind(on_press=lambda instance: self.show_popup("The national flag of Ukraine (Ukrainian: Прапор України, romanized: Prapor Ukrayiny) consists of equally sized horizontal bands of blue and yellow. The blue and yellow bicolour first appeared during the 1848 Spring of Nations in Lemberg, then part of the Austrian Empire. It was adopted as a state flag for the first time in the aftermath of the Russian Revolution by the Ukrainian People's Republic, the West Ukrainian People's Republic and the Ukrainian State. It was also later adopted by Carpatho-Ukraine in March 1939. When Ukraine was part of the Soviet Union, the bicolour was banned and it used flag of the Ukrainian Soviet Socialist Republic which featured a red flag along with the azure bottom with a golden hammer and sickle and a golden bordered red star on top. During the dissolution of the Soviet Union, the bicolour gradually returned in use before officially being adopted again on 28 January 1992 by the Ukrainian parliament. Ukraine has celebrated the Day of the National Flag on 23 August since 2004.", "flag-2.png", instance))

        btn3 = Button(text='Trident',
                      background_normal="emblem.jpg")
        btn3.bind(on_press=lambda instance: self.show_popup("The modern ''trident'' symbol was adopted as the coat of arms of the Ukrainian People's Republic in February 1918, designed by Vasyl Krychevsky. The design has precedents in seals of the Kyivan Rus. The first known archaeological and historical evidence of this symbol can be found on the seals of the Rurik dynasty. However, according to Pritsak, the stylized trident tamga, or seal which was used by Rus rulers such as Sviatoslav I of Kiev and similar tamgas that were found in ruins are Khazar in origin. It was stamped on the gold and silver coins issued by Prince Volodymyr the Great (980–1015), who might have inherited the symbol from his ancestors (such as Svyatoslav I Igorevich) as a dynastic coat of arms, and he passed it on to his sons, Svyatopolk I (1015–19) and Yaroslav the Wise (1019–54). The symbol was also found on the bricks of the Church of the Tithes in Kyiv, the tiles of the Dormition Cathedral in Volodymyr, and the stones of other churches, castles, and palaces. There are many examples of it used on ceramics, weapons, rings, medallions, seals, and manuscripts.", "emblem-2.png", instance))

        btn4 = Button(text='Kyiv',
                      background_normal="kyiv.jpg")
        btn4.bind(on_press=lambda instance: self.show_popup("Kyiv, also spelled Kiev, is the capital and most populous city of Ukraine. It is in north-central Ukraine along the Dnieper River. As of 1 January 2022, its population was 2,952,301, making Kyiv the seventh-most populous city in Europe. Kyiv is an important industrial, scientific, educational, and cultural center in Eastern Europe. It is home to many high-tech industries, higher education institutions, and historical landmarks. The city has an extensive system of public transport and infrastructure, including the Kyiv Metro.The city's name is said to derive from the name of Kyi, one of its four legendary founders. During its history, Kyiv, one of the oldest cities in Eastern Europe, passed through several stages of prominence and obscurity. The city probably existed as a commercial center as early as the 5th century. A Slavic settlement on the great trade route between Scandinavia and Constantinople, Kyiv was a tributary of the Khazars, until its capture by the Varangians (Vikings) in the mid-9th century. Under Varangian rule, the city became a capital of Kievan Rus', the first East Slavic state. Completely destroyed during the Mongol invasions in 1240, the city lost most of its influence for the centuries to come. Following the collapse of the Soviet Union and Ukrainian independence in 1991, Kyiv remained Ukraine's capital and experienced a steady influx of ethnic Ukrainian migrants from other regions of the country. During the country's transformation to a market economy and electoral democracy, Kyiv has continued to be Ukraine's largest and wealthiest city.", "kyiv-2.jpg", instance))

        # добавляем кнопки в BoxLayout
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)

        # добавляем анимацию для каждой кнопки
        for btn in [btn1, btn2, btn3, btn4]:
            anim = Animation(font_size=10) + Animation(font_size=50)
            anim.repeat = False
            anim.start(btn)

      
    def show_popup(self, text, image, button_instance):
        # создаем виджет Popup
        content = BoxLayout(orientation="vertical")
        image_widget = Image(source=image, size_hint=(1, 1))
        label_widget = Label(text=text, size_hint=(1, None), height=dp(200), text_size=(700, None), valign='top')
        
        # создаем ScrollView и добавляем в нее Label
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(label_widget)
        
        close_button = Button(text="Close", size_hint=(1, 0.2))
        content.add_widget(image_widget)
        
        # добавляем ScrollView вместо Label
        content.add_widget(scroll_view)
        content.add_widget(close_button)
        
        popup = Popup(title="", content=content, size_hint=(None, None), size=(750, dp(400)))
        close_button.bind(on_press=popup.dismiss)
        popup.open()



    def hide_popup(self):
        if self.popup_window:
           self.popup_window.dismiss()



class MyApp(App):
    
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MyApp().run()
exit()

