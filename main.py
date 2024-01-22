from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class mainmenu(FloatLayout):
    def __init__(self, **kwargs):
        super(mainmenu, self).__init__(**kwargs)

        Window.size = (360, 640)
        

        label = Label(text="MENU UTAMA", pos_hint={'center_x': 0.5, 'center_y': 0.8})
        button = Button(text="bacaan", pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.5, 0.1))
        button.bind(on_press=self.switch_screen)
        self.add_widget(label)
        self.add_widget(button)

    def switch_screen(self, instance):
        # Hapus semua widget di layar dan tambahkan widget untuk halaman berikutnya
        self.clear_widgets()
        next_page = bacaan()
        self.add_widget(next_page)

class bacaan(FloatLayout):
    def __init__(self, **kwargs):
        super(bacaan, self).__init__(**kwargs)

        irisan = """   
        A irisan B { A∩B } adalah himpunan semua anggota yang merupakan 
        anggota A dan juga anggota B. 
        Dengan notasi pembentuk himpunan : A∩B = { x | x ∈ A dan x ∈ B }
        """
        irisan = Label(text = irisan)

        label = Label(text="IRISAN", pos_hint={'center_x': 0.5, 'center_y': 0.9})
        back = Button(text="back", pos_hint={'center_x': 0.1, 'center_y': 0.9}, size_hint=(0.1, 0.1))
        back.bind(on_press=self.home_button)
        nextt = Button(text="next", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(0.1, 0.1))
        nextt.bind(on_press=self.next_button)
        self.add_widget(label)
        self.add_widget(irisan)
        self.add_widget(back)
        self.add_widget(nextt)
    
        text_box = TextInput(multiline = False, text ='', 
         size_hint=(None, 0.1), height=30, pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.add_widget(text_box)

        text_box2 = TextInput(multiline = False, text='', 
         size_hint=(None, 0.1), height=30, pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.add_widget(text_box2)

        calculate_button = Button(text='Hitung Hasil', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        calculate_button.bind(on_press=lambda instance: self.perform_set_operation(text_box.text, text_box2.text))
        self.add_widget(calculate_button)

        self.result_label = Label(text='', pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.add_widget(self.result_label)

    def perform_set_operation(self, text_box, text_box2):
        try:
            # Mengonversi input teks menjadi set data
            data1 = set(text_box.split(','))
            data2 = set(text_box2.split(','))

            # Menggabungkan elemen dari dua set
            result_set = sorted(set(data1) & set(data2))

            # Menampilkan hasil
            self.result_label.text = f"Hasil dari {data1} n {data2}: {result_set}"
        except ValueError:
            self.result_label.text = "Format input tidak valid."
   
    def home_button(self, instance):
        # Hapus semua widget di layar dan tambahkan widget untuk halaman awal
        self.clear_widgets()
        home_page = mainmenu()
        self.add_widget(home_page)

    def next_button(self, instance):
        # Hapus semua widget di layar dan tambahkan widget untuk halaman awal
        self.clear_widgets()
        next_page = GABUNGAN()
        self.add_widget(next_page)

class GABUNGAN(FloatLayout):
    def __init__(self, **kwargs):
        super(GABUNGAN, self).__init__(**kwargs)

        gabungan = """   
        Gabungan himpunan A dan B adalah suatu himpunan 
        yang anggota anggotanya merupakan anggota 
        himpunan A atau anggota himpunan B.
        A∪B = { x | x∈A atau x∈B}
        """
        gabungan = Label(text = gabungan)

        label = Label(text="GABUNGAN", pos_hint={'center_x': 0.5, 'center_y': 0.9})
        back = Button(text="back", pos_hint={'center_x': 0.1, 'center_y': 0.9}, size_hint=(0.1, 0.1))
        back.bind(on_press=self.switch_screen)
        nextt = Button(text="next", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(0.1, 0.1))
        nextt.bind(on_press=self.next_button)
        self.add_widget(label)
        self.add_widget(gabungan)
        self.add_widget(back)
        self.add_widget(nextt)
    
    
        text_box = TextInput(multiline = False, text ='', 
         size_hint=(None, 0.1), height=30, pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.add_widget(text_box)

        text_box2 = TextInput(multiline = False, text='', 
         size_hint=(None, 0.1), height=30, pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.add_widget(text_box2)

        calculate_button = Button(text='Hitung Hasil', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        calculate_button.bind(on_press=lambda instance: self.perform_set_operation(text_box.text, text_box2.text))
        self.add_widget(calculate_button)

        self.result_label = Label(text='', pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.add_widget(self.result_label)

    def perform_set_operation(self, text_box, text_box2):
        try:
            # Mengonversi input teks menjadi set data
            data1 = set(text_box.split(','))
            data2 = set(text_box2.split(','))

            # Menggabungkan elemen dari dua set
            result_set = sorted(set(data1) | set(data2))

            # Menampilkan hasil
            self.result_label.text = f"Hasil dari {data1} u {data2}: {result_set}"
        except ValueError:
            self.result_label.text = "Format input tidak valid."
   
    def switch_screen(self, instance):
        # Hapus semua widget di layar dan tambahkan widget untuk halaman awal
        self.clear_widgets()
        home_page = mainmenu()
        self.add_widget(home_page)
    
    def next_button(self, instance):
        # Hapus semua widget di layar dan tambahkan widget untuk halaman awal
        self.clear_widgets()
        next_page = PENJUMLAHAN()
        self.add_widget(next_page)

class PENJUMLAHAN(FloatLayout):
    def __init__(self, **kwargs):
        super(PENJUMLAHAN, self).__init__(**kwargs)

        penjumlahan = """   
        Penjumlahan himpunan A dan B adalah suatu himpunan yang 
        anggota anggotanya merupakan anggota himpunan A atau anggota himpunan B, 
        tetapi bukan anggota A ∩ B
        """
        penjumlahan = Label(text = penjumlahan)

        label = Label(text="PENJUMLAHAN", pos_hint={'center_x': 0.5, 'center_y': 0.9})
        back = Button(text="back", pos_hint={'center_x': 0.1, 'center_y': 0.9}, size_hint=(0.1, 0.1))
        back.bind(on_press=self.switch_screen)
        nextt = Button(text="next", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(0.1, 0.1))
        nextt.bind(on_press=self.next_button)
        self.add_widget(label)
        self.add_widget(penjumlahan)
        self.add_widget(back)
        self.add_widget(nextt)
        
        text_box = TextInput(multiline = False, text ='', 
         size_hint=(None, 0.1), height=30, pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.add_widget(text_box)

        text_box2 = TextInput(multiline = False, text='', 
         size_hint=(None, 0.1), height=30, pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.add_widget(text_box2)

        calculate_button = Button(text='Hitung Hasil', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        calculate_button.bind(on_press=lambda instance: self.perform_set_operation(text_box.text, text_box2.text))
        self.add_widget(calculate_button)

        self.result_label = Label(text='', pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.add_widget(self.result_label)

    def perform_set_operation(self, text_box, text_box2):
        try:
            # Mengonversi input teks menjadi set data
            data1 = set(text_box.split(','))
            data2 = set(text_box2.split(','))

            # Menggabungkan elemen dari dua set
            result_set = sorted(set(data1) | set(data2))

            # Menampilkan hasil
            self.result_label.text = f"Hasil dari {data1} u {data2}: {result_set}"
        except ValueError:
            self.result_label.text = "Format input tidak valid."
   
    def switch_screen(self, instance):
        # Hapus semua widget di layar dan tambahkan widget untuk halaman awal
        self.clear_widgets()
        home_page = mainmenu()
        self.add_widget(home_page)

    def next_button(self, instance):
        # Hapus semua widget di layar dan tambahkan widget untuk halaman awal
        self.clear_widgets()
        next_page = PENGURANGAN()
        self.add_widget(next_page)


class PENGURANGAN(FloatLayout):
    def __init__(self, **kwargs):
        super(PENGURANGAN, self).__init__(**kwargs)

        pengurangan = """   
        Selisih himpunan A dan B adalah suatu himpunan yang 
        anggota-anggotanya merupakan anggota himpunan A 
        tetapi bukan anggota himpunan B. A - B = { x | x∈A, x∉B}
        """
        pengurangan = Label(text = pengurangan)

        label = Label(text="PENGURANGAN", pos_hint={'center_x': 0.5, 'center_y': 0.9})
        back = Button(text="back", pos_hint={'center_x': 0.1, 'center_y': 0.9}, size_hint=(0.1, 0.1))
        back.bind(on_press=self.switch_screen)
        #nextt = Button(text="next", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(0.1, 0.1))
        #nextt.bind(on_press=self.next_button)
        self.add_widget(label)
        self.add_widget(pengurangan)
        self.add_widget(back)
        #self.add_widget(nextt)
        
        text_box = TextInput(multiline = False, text ='', 
         size_hint=(None, 0.1), height=30, pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.add_widget(text_box)

        text_box2 = TextInput(multiline = False, text='', 
         size_hint=(None, 0.1), height=30, pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.add_widget(text_box2)

        calculate_button = Button(text='Hitung Hasil', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        calculate_button.bind(on_press=lambda instance: self.perform_set_operation(text_box.text, text_box2.text))
        self.add_widget(calculate_button)

        self.result_label = Label(text='', pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.add_widget(self.result_label)

    def perform_set_operation(self, text_box, text_box2):
        try:
            # Mengonversi input teks menjadi set data
            data1 = set(text_box.split(','))
            data2 = set(text_box2.split(','))

            # Menggabungkan elemen dari dua set
            result_set = sorted(set(data1) | set(data2))

            # Menampilkan hasil
            self.result_label.text = f"Hasil dari {data1} u {data2}: {result_set}"
        except ValueError:
            self.result_label.text = "Format input tidak valid."
   
    def switch_screen(self, instance):
        # Hapus semua widget di layar dan tambahkan widget untuk halaman awal
        self.clear_widgets()
        home_page = mainmenu()
        self.add_widget(home_page)

    #def next_button(self, instance):
        # Hapus semua widget di layar dan tambahkan widget untuk halaman awal
        #self.clear_widgets()
        #next_page = PENGURANGAN()
        #self.add_widget(next_page)


class MyApp(App):
    def build(self):
        # Mulai dengan halaman awal
        return mainmenu()

if __name__ == '__main__':
    MyApp().run()


