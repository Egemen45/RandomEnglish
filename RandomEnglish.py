#RandomEnglish#

import tkinter as tk
import random
from googletrans import Translator

class uygulama():
    
    def __init__(self):
        
        self.doru = 0
        self.yanlis = 0
        
        
        
        
        self.b1 = list(open('C:/Users/Şeref/Desktop/b1.txt', 'r', encoding='utf-8'))
        self.app = tk.Tk()
        self.app.title('RandomEnglish')
        self.app.geometry('1024x800')
        self.app.maxsize(1280, 800)
        self.app.config(bg='gray')
        
        self.etiket = tk.Label(self.app, text="", font='Times 40 italic', bg='gray')
        self.etiket.pack(side=tk.LEFT, expand=1, fill=tk.Y)
        self.etiket.place(relx=0.45, rely=0.5)
        
        self.dogru = tk.Label(self.app , text= 'Doğru sayısı: ' + str(self.doru) , font='Times 20 italic', bg='gray' )
        self.dogru.pack(anchor='nw')
        
        self.yanliss = tk.Label(self.app , text= 'Yanlış sayısı: ' + str(self.yanlis) , font='Times 20 italic', bg='gray' )
        self.yanliss.pack(anchor='nw')
        
        self.cikisyap = tk.Button(self.app, text='Çıkış', font='Times 30 italic', command=self.app.quit)
        self.cikisyap.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.etiket2 = tk.Label(self.app, text='', font='Times 25 italic', bg='gray')
        self.etiket2.pack(side=tk.TOP, fill=tk.X)
        
        self.etiket3 = tk.Label(self.app , text='',font='Times 25 italic', bg='gray')
        self.etiket3.pack(side=tk.TOP, fill=tk.X)
        
        self.guncelle()
        
        self.girdi = tk.Entry(self.app, font='Times 20 italic')
        self.girdi.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.kontrol = tk.Button(self.app, text='Kontrol Et', font='Times 20 italic', command=self.check)
        self.kontrol.pack(side=tk.BOTTOM, fill=tk.X)
        
    def check(self):
        translator = Translator()
        result = translator.translate(self.b1r, dest='tr')
        bilgi = self.girdi.get()
        print(bilgi)
        print(result.text)
        if result.text == bilgi:
            self.doru += 1
            self.etiket2.config(text='Cevabınız doğru', font='Times 25 italic', bg='gray')
            self.etiket3.config(text=' ',font='Times 25 italic', bg='gray')
            self.dogru.config(text= 'Doğru sayısı: ' + str(self.doru) , font='Times 20 italic', bg='gray' )

            self.guncelle()
            
        else:
            self.yanlis += 1
            self.etiket2.config(text='Cevabınız yanlış', font='Times 25 italic', bg='gray')
            self.etiket3.config(text='Doğru cevap : ' + result.text,font='Times 25 italic', bg='gray')
            self.yanliss.config(text= 'Yanlış sayısı: ' + str(self.yanlis) , font='Times 20 italic', bg='gray' )
            self.guncelle()
    
    def guncelle(self):
        self.b1r = random.choice(self.b1)
        self.etiket.config(text=self.b1r, font='Times 40 italic', bg='gray')

uygulama().app.mainloop()