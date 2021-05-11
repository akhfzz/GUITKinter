from tkinter import *

class BangunDatar:
	def __init__(self):
		#setting display
		self.master = Tk()
		self.master.geometry(("400x500+30+30"))
		self.firstDisp = 0
		self.enterAlas = 0
		self.enterTinggi = 0
		self.enterPanjang = 0
		self.enterLebar = 0
		self.enterJari = 0
		self.total_number = IntVar()
		self.total_number.set(self.firstDisp)

		self.label_input_alas = Label(self.master, text='sisiAlas: ')
		self.label_input_tinggi = Label(self.master, text='sisiTinggi: ')
		self.label_input_panjang = Label(self.master, text='sisiPanjang: ')
		self.label_input_lebar = Label(self.master, text='sisiLebar: ')
		self.label_input_jari = Label(self.master, text='Jari2: ')
		self.label_text = Label(self.master, textvariable=self.total_number)

		valid= self.master.register(self.validate)

		self.entry_jari = Entry(self.master, validate='key', validatecommand=(valid, '%P'))
		self.entry_panjang = Entry(self.master, validate='key', validatecommand=(valid, '%P'))
		self.entry_lebar = Entry(self.master, validate='key', validatecommand=(valid, '%P'))
		self.entry_alas = Entry(self.master, validate='key', validatecommand=(valid, '%P'))
		self.entry_tinggi = Entry(self.master, validate='key', validatecommand=(valid, '%P'))

		self.hitung_Lsegitiga = Button(self.master, text='Luas Segitiga', command=lambda:self.Kali('hitungLuasSegitiga'))
		self.hitung_LPersegi = Button(self.master, text='Luas Persegi', command=lambda:self.Kali('hitungLuasPersegi'))
		self.hitung_LLingkaran = Button(self.master, text='Luas Lingkaran', command=lambda:self.Kali('hitungLuasLingkaran'))
		self.reset_data = Button(self.master, text='Reset', command=lambda:self.Kali('reset'))
		self.keluar_app = Button(self.master, text='Exit', command=self.master.quit)

		self.label_input_alas.grid(row=0, column=0, sticky=W)
		self.label_input_tinggi.grid(row=1, column=0, sticky=W)
		self.label_input_panjang.grid(row=2, column=0, sticky=W)
		self.label_input_lebar.grid(row=3, column=0, sticky=W)
		self.label_input_jari.grid(row=4, column=0, sticky=W)

		self.entry_alas.grid(row=0, column=1, sticky=E)
		self.entry_tinggi.grid(row=1, column=1, sticky=E)
		self.entry_panjang.grid(row=2, column=1, sticky=E)
		self.entry_lebar.grid(row=3, column=1, sticky=E)
		self.entry_jari.grid(row=4, column=1, sticky=E)

		self.hitung_Lsegitiga.grid(row=5, column=1, sticky=W+E)
		self.hitung_LPersegi.grid(row=6, column=1, sticky=W+E)
		self.hitung_LLingkaran.grid(row=7, column=1, sticky=W+E)
		self.reset_data.grid(row=8, column=0, sticky=W+E)
		self.keluar_app.grid(row=8, column=1, sticky=W+E)
		self.label_text.grid(row=9, column=0, sticky=W, columnspan=4)

	def validate(self, luas):
		if not luas:
			self.enterAlas = 0
			self.enterTinggi = 0
			self.enterPanjang = 0
			self.enterLebar = 0
			self.enterJari= 0
			return True

		try:
			self.enterAlas = float(luas)
			self.enterTinggi = float(luas)
			self.enterPanjang = float(luas)
			self.enterLebar = float(luas)
			self.enterJari = float(luas)
			return True

		except ValueError:
			return False