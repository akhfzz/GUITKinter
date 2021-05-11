from Parent import BangunDatar
from tkinter import *

class Segitiga(BangunDatar):
	def __init__(self):
		BangunDatar.__init__(self)
		self.master.title('Segitiga')
		self.master.mainloop()

	def Kali(self, bintang):
		if bintang=='hitungLuasSegitiga':
			self.firstDisp +=  self.enterAlas*(self.enterTinggi * 1/2)
		elif bintang == 'reset':
			self.firstDisp = 0

		self.total_number.set(self.firstDisp)

class Persegi(BangunDatar):
	def __init__(self):
		BangunDatar.__init__(self)
		self.master.title('Persegi')
		self.master.mainloop()

	def Kali(self, bintang):
		if bintang=='hitungLuasPersegi':
			self.firstDisp +=  self.enterPanjang * self.enterLebar
		elif bintang == 'reset':
			self.firstDisp = 0

		self.total_number.set(self.firstDisp)

class Lingkaran(BangunDatar):
	def __init__(self):
		BangunDatar.__init__(self)
		self.master.title('Lingkaran')
		self.master.mainloop()

	def Kali(self, bintang):
		if bintang=='hitungLuasLingkaran':
			self.firstDisp += 22/7 *  self.enterJari ** 2
		elif bintang == 'reset':
			self.firstDisp = 0

		self.total_number.set(self.firstDisp)

