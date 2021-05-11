from tkinter import *
from Child import Segitiga, Persegi, Lingkaran
from Parent import BangunDatar


if __name__ == '__main__':
	obj1 = Lingkaran()
	obj1.Kali('hitungLuasLingkaran')

	obj2 = Segitiga()
	obj2.Kali('hitungLuasSegitiga')

	obj3 = Persegi()
	obj3.Kali('hitungLuasPersegi')