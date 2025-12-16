import customtkinter as ctk #koristimo radi lepseg dizajna i lakseg kodiranja
from math import sqrt       #koristimo sqrt za koren jer je preciznije od 'x ** 0.5'

class Kalkulator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("360x500")
        self.title("Kalkulator")
        self.resizable(False,False)
        self.configure(bg_color="#d3d3d3")
        
        self.prvi_broj=None
        self.operacija=None
        self.dark_mode=False
        self.prosiren=False
        self.extra_btn=[]
        
        
        self.unos=ctk.CTkEntry(self,
                               corner_radius=8,
                               width=330,
                               height=80,
                               fg_color="white",
                               text_color="black",
                               font=("Arial", 24),
                               justify="right")
        self.unos.grid(row=0, column=0, columnspan=4, padx=15, pady=(25, 20))
        
        self.create_btns()
        
    #funkcija za tamnu temu    
    def tamna_tema(self):
        if not self.dark_mode:
            ctk.set_appearance_mode("dark")       #bez ovog dela koda oko dugmica ostaje belo(pretpostavljam zbog corner_radius)
            self.configure(bg_color="#d3d3d3")
            
            for widget in self.winfo_children():
                if isinstance(widget, ctk.CTkButton):       #trazimo samo dugmice kako bismo ih promenili
                    widget.configure(fg_color="#3a3a3a", hover_color="#4a4a4a", text_color="white")
            self.dark_mode=True
        
        else:
            ctk.set_appearance_mode("light")
            self.configure(bg_color="#2e2e2e")
            
            for widget in self.winfo_children():
                if isinstance(widget, ctk.CTkButton):
                    widget.configure(fg_color="#f0f0f0", hover_color="#e0e0e0", text_color="black")
            self.dark_mode=False
    
    def kvadrat(self):
        try:
            broj=float(self.unos.get())
            rezultat=broj ** 2
            if rezultat.is_integer():
                rezultat=int(rezultat)
            
            self.unos.delete(0, ctk.END)
            self.unos.insert(0, rezultat)
        except ValueError:
            self.unos.delete(0, ctk.END)
            self.unos.insert(0, "Greska")
            
    
    def koren(self):
        try:
            broj=float(self.unos.get())
            rezultat=sqrt(broj)
            if rezultat.is_integer():
                rezultat=int(rezultat)
            
            self.unos.delete(0, ctk.END)
            self.unos.insert(0, rezultat)
        except ValueError:
            self.unos.delete(0, ctk.END)
            self.unos.insert(0, "Greska")
    
    def reciprocno(self):
        try:
            broj=float(self.unos.get())
            if broj==0:
                self.unos.delete(0, ctk.END)
                self.unos.insert(0, "Greska")
                return 0
            
            rezultat=1/broj
            if rezultat.is_integer():
                rezultat=int(rezultat)
            
            self.unos.delete(0, ctk.END)
            self.unos.insert(0, rezultat)
        except ValueError:
            self.unos.delete(0, ctk.END)
            self.unos.insert(0, "Greska")
            
    def stepen(self):
        try:
            self.prvi_broj=float(self.unos.get())
        except ValueError:
            self.prvi_broj=0
        
        self.operacija="^"
        self.unos.delete(0, ctk.END)
                    
    def napravi_extra_btns(self):
        
        btn_kvadrat=ctk.CTkButton(self, text="x²", height=60, width=60,
                                fg_color="#f0f0f0", corner_radius=12,
                                hover_color="#e0e0e0", text_color="black",
                                font=("Arial", 18), command=self.kvadrat)
        
        btn_koren=ctk.CTkButton(self, text="√x", height=60, width=60,
                                fg_color="#f0f0f0", corner_radius=12,
                                hover_color="#e0e0e0", text_color="black",
                                font=("Arial", 18), command=self.koren)
        
        btn_rec=ctk.CTkButton(self, text="1/x", height=60, width=60,
                                fg_color="#f0f0f0", corner_radius=12,
                                hover_color="#e0e0e0", text_color="black",
                                font=("Arial", 18), command=self.reciprocno)
        
        btn_stepen=ctk.CTkButton(self, text="xʸ", height=60, width=60,
                                fg_color="#f0f0f0", corner_radius=12,
                                hover_color="#e0e0e0", text_color="black",
                                font=("Arial", 18), command=self.stepen)
        
        self.extra_btn=[btn_kvadrat, btn_koren, btn_rec, btn_stepen]   #ubacujemo u listu zbog kasnijeg uklanjanja iz apl
        
        btn_kvadrat.grid(row=6, column=0, padx=5, pady=5)
        btn_koren.grid(row=6, column=1, padx=5, pady=5)
        btn_rec.grid(row=6, column=2, padx=5, pady=5)
        btn_stepen.grid(row=6, column=3, padx=5, pady=5)
    
    def obrisi_extra_btns(self):
        for btn in self.extra_btn:
            btn.grid_forget()
        self.extra_btn.clear()
    
    def prosiri(self):
        if not self.prosiren:
            self.geometry("360x550")        #povecavamo visinu
            self.napravi_extra_btns()
            self.prosiren=True
        
        else:
            self.geometry("360x500")        #vracamo staru visinu
            self.obrisi_extra_btns()
            self.prosiren=False
    
    def klik(self, taster):
        if "." in self.unos.get() and taster==".":
            return 0
        else:
            self.unos.insert(ctk.END, taster)
    
    def ocisti(self):
        self.unos.delete(0, ctk.END)
        self.prvi_broj=None
        self.operacija=None 
        
    def backspace(self):        
        tekst=self.unos.get()
        if tekst:
            self.unos.delete(len(tekst)-1, ctk.END) 
            
    def izracunaj(self, a, b, op):          #glavna funkcija za racunanje
        if op == "+":
            return a+b
        if op == "-":
            return a-b
        if op == "*":
            return a*b
        if op == "/":
            return "Greska" if b == 0 else a / b  
        if op == "^":
            return a ** b
              
    def izaberi_operaciju(self, op):
        try:
            trenutni=float(self.unos.get())   
        except ValueError:
            trenutni=0
        
        if self.operacija and trenutni:     #ukoliko vec imamo operaciju(onda imamo i prvi broj) radi ovaj deo koda
            drugi=float(trenutni)  
             
            rezultat= self.izracunaj(self.prvi_broj, drugi, self.operacija)  
            
            if isinstance(rezultat, float) and rezultat.is_integer():       #ispitivanje da li je rezultat float
                rezultat=int(rezultat)                                      #i da li je intiger tipa (npr. 3.0, 6.0,...)
                                                                            #ukoliko jeste pretvara u int radi lepseg ispisa u ekran
            self.unos.delete(0, ctk.END)
            self.unos.insert(0, rezultat)
            
            self.prvi_broj=float(rezultat) 
        
        else:                               #ako nemamo operaciju prvi broj je trenutni odozgo
            try:
                self.prvi_broj=float(trenutni)
            except ValueError:
                self.prvi_broj=0
        
        self.operacija=op
        self.unos.delete(0, ctk.END)
    
    def jednako(self):
        try:
            drugi=float(self.unos.get())
        except ValueError:
            drugi=0
            
        if not self.operacija:
            return 0
        else:
            rezultat=self.izracunaj(self.prvi_broj, drugi, self.operacija)  
        
        if isinstance(rezultat, float) and rezultat.is_integer():
                rezultat=int(rezultat)
            
        self.unos.delete(0, ctk.END)
        self.unos.insert(0, rezultat)  
        
        self.prvi_broj=None
        self.operacija=None
        
    def create_btns(self):
        
        btns=[
            ("CE", 1, 0, self.ocisti),
            ("⌫", 1, 1, self.backspace),
            ("⇵", 1, 2, self.prosiri),
            ("🌙", 1, 3, self.tamna_tema),
            
            ("7", 2, 0, lambda: self.klik("7")),
            ("8", 2, 1, lambda: self.klik("8")),
            ("9", 2, 2, lambda: self.klik("9")),
            ("*", 2, 3, lambda: self.izaberi_operaciju("*")),
            
            ("4", 3, 0, lambda: self.klik("4")),
            ("5", 3, 1, lambda: self.klik("5")),
            ("6", 3, 2, lambda: self.klik("6")),
            ("/", 3, 3, lambda: self.izaberi_operaciju("/")),
            
            ("1", 4, 0, lambda: self.klik("1")),
            ("2", 4, 1, lambda: self.klik("2")),
            ("3", 4, 2, lambda: self.klik("3")),
            ("+", 4, 3, lambda: self.izaberi_operaciju("+")),
            
            (".", 5, 0, lambda: self.klik(".")),
            ("0", 5, 1, lambda: self.klik("0")),
            ("=", 5, 2, self.jednako),
            ("-", 5, 3, lambda: self.izaberi_operaciju("-"))    
        ]    
        
        for (tekst, r, c, cmd) in btns:
            ctk.CTkButton(self,
                          text=tekst,
                          corner_radius=12,
                          width=60,
                          height=60,
                          fg_color="#f0f0f0",
                          hover_color="#e0e0e0",
                          text_color="black",
                          font=("Arial", 18),
                          command=cmd
                          ).grid(row=r, column=c, padx=5, pady=5)
            

app=Kalkulator()
app.mainloop()
        
        