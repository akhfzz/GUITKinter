from tkinter import *

class Kasir(object):
	def __init__(self, no=None, nm_barang=None, harga=None, Qty=None):
		self.no = no
		self.nm_barang = nm_barang
		self.harga = harga
		self.Qty = Qty

master= Tk()
master.title('Kasir Toko Kelontong')
master.geometry('450x300+35+35')
dataList = []

brg = ''
qty = 0
harga = 0

def validation(valid):
	if not valid:
		brg = ''
		qty = 0
		harga = 0
	try:
		brg = str(valid)
		qty = int(valid)
		harga = int(valid)
		return True
	except ValueError:
		return False

valid = master.register(validation)

Lb_barang = Label(master, text='Nama Barang : ').grid(row=1, column=0, padx=20, columnspan=6,  pady=10)
EnBarang = Entry(master, width=40, validate='focus', validatecommand=(valid, '%P'))
EnBarang.grid(row=1, column=6, columnspan=8, pady=10)

Lb_harga = Label(master, text='Harga Barang : ').grid(row=2, column=0, padx=20, columnspan=6,pady=10)
EnHarga = Entry(master, width=40,validate='focus', validatecommand=(valid, '%P'))
EnHarga.grid(row=2, column=6, columnspan=8, pady=10)

Lb_jumlah = Label(master, text='QTY : ').grid(row=3, column=0, padx=20, columnspan=6, pady=10)
EnJumlah = Entry(master, width=40, validate='focus', validatecommand=(valid, '%P'))
EnJumlah.grid(row=3, column=6, columnspan=8,pady=10)

def Add(ket):
	if ket == 'tambah':
		i = 0
		listHarga = []
		listJumlah = []
		for index in range(0, len(dataList)+1):
			i += 1
			dataList.append(Kasir(i, EnBarang.get(), EnHarga.get(), EnJumlah.get()))
			Label(master, text=f'{i}').grid(row=i+10,column=0,  pady=10,columnspan=3)
			Label(master, text=f'{dataList[index].nm_barang}').grid(row=i+10,column=3,  pady=10,columnspan=3)
			Label(master, text=f'{int(dataList[index].harga) * int(dataList[index].Qty)}').grid(row=i+10,column=11,  pady=10,columnspan=3)
			Label(master, text=f'{dataList[index].Qty}').grid(row=i+10,column=7,  pady=10,columnspan=3)
			listHarga.append(int(dataList[index].harga))
			listJumlah.append(int(dataList[index].Qty))
			h = 0
			for x in range(0, len(listJumlah)):
				h += listHarga[x] * listJumlah[x]
				Label(master, text='Payment',borderwidth=1,relief='raised', width=20 ).grid(row=30, column=5, padx=20, columnspan=6, pady=10)
				Label(master,text=f'{h}').grid(row=30,column=11,  pady=20,columnspan=3)

btn_add = Button(master, text='Add', command=lambda:Add('tambah'), bg='red', fg='white').grid(row=4, column=11, columnspan=4)

no_brg = Label(master, text='No', borderwidth=1, width=20, relief='raised', bg='black', fg='white').grid(row=10, column=0, pady=20,columnspan=3)
nm_brg = Label(master, text='Nama Barang', borderwidth=1, width=20, relief='raised', bg='black', fg='white').grid(row=10, column=3, pady=20,columnspan=4)
Qty = Label(master, text='Qty', borderwidth=1, width=20, relief='raised', bg='black', fg='white').grid(row=10, column=7,pady=20,columnspan=4)
Total = Label(master, text='Total', borderwidth=1, width=20, relief='raised', bg='black', fg='white').grid(row=10, column=11,pady=20,columnspan=4)

master.mainloop()