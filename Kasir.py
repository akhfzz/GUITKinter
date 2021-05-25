from tkinter import *

class Kasir(object):
	def __init__(self, no=None, nm_barang=None, harga=None, Qty=None):
		self.no = no
		self.nm_barang = nm_barang
		self.harga = harga
		self.Qty = Qty
		
class Kasir:
	def __init__(self, master):
		self.master = master
		master.title('Kasir Toko Kelontong')
		master.geometry('450x300+35+35')
		self.dataList = []

		self.brg = ''
		self.qty = 0
		self.harga = 0

		def validation(valid):
			if not valid:
				self.brg = ''
				self.qty = 0
				self.harga = 0
			try:
				self.brg = str(valid)
				self.qty = int(valid)
				self.harga = int(valid)
				return True
			except ValueError:
				return False

		valid = master.register(self.validation)

		self.Lb_barang = Label(self.master, text='Nama Barang : ').grid(row=1, column=0, padx=20, columnspan=6,  pady=10)
		self.EnBarang = Entry(self.master, width=40, validate='focus', validatecommand=(valid, '%P'))
		self.EnBarang.grid(row=1, column=6, columnspan=8, pady=10)

		self.Lb_harga = Label(self.master, text='Harga Barang : ').grid(row=2, column=0, padx=20, columnspan=6,pady=10)
		self.EnHarga = self.Entry(master, width=40,validate='focus', validatecommand=(valid, '%P'))
		self.EnHarga.grid(row=2, column=6, columnspan=8, pady=10)

		self.Lb_jumlah = Label(self.master, text='QTY : ').grid(row=3, column=0, padx=20, columnspan=6, pady=10)
		self.EnJumlah = Entry(self.master, width=40, validate='focus', validatecommand=(valid, '%P'))
		self.EnJumlah.grid(row=3, column=6, columnspan=8,pady=10)

		def Add(ket):
			if ket == 'tambah':
				i = 0
				self.listHarga = []
				self.listJumlah = []
				for index in range(0, len(self.dataList)+1):
					i += 1
					self.dataList.append(Kasir(i, self.EnBarang.get(), self.EnHarga.get(), self.EnJumlah.get()))
					Label(self.master, text=f'{i}').grid(row=i+10,column=0,  pady=10,columnspan=3)
					Label(self.master, text=f'{self.dataList[index].nm_barang}').grid(row=i+10,column=3,  pady=10,columnspan=3)
					Label(self.master, text=f'{int(dataList[index].harga) * int(self.dataList[index].Qty)}').grid(row=i+10,column=11,  pady=10,columnspan=3)
					Label(self.master, text=f'{self.dataList[index].Qty}').grid(row=i+10,column=7,  pady=10,columnspan=3)
					self.listHarga.append(int(self.dataList[index].harga))
					self.listJumlah.append(int(self.dataList[index].Qty))
					h = 0
					for x in range(0, len(self.listJumlah)):
						h += self.listHarga[x] * self.listJumlah[x]
						Label(self.master, text='Payment',borderwidth=1,relief='raised', width=20 ).grid(row=30, column=5, padx=20, columnspan=6, pady=10)
						Label(self.master,text=f'{h}').grid(row=30,column=11,  pady=20,columnspan=3)

		btn_add = Button(self.master, text='Add', command=lambda:self.Add('tambah'), bg='red', fg='white').grid(row=4, column=11, columnspan=4)

		no_brg = Label(self.master, text='No', borderwidth=1, width=20, relief='raised', bg='black', fg='white').grid(row=10, column=0, pady=20,columnspan=3)
		nm_brg = Label(self.master, text='Nama Barang', borderwidth=1, width=20, relief='raised', bg='black', fg='white').grid(row=10, column=3, pady=20,columnspan=4)
		Qty = Label(self.master, text='Qty', borderwidth=1, width=20, relief='raised', bg='black', fg='white').grid(row=10, column=7,pady=20,columnspan=4)
root = Tk()
obj = Kasir(root)
root.mainloop()
		Total = Label(self.master, text='Total', borderwidth=1, width=20, relief='raised', bg='black', fg='white').grid(row=10, column=11,pady=20,columnspan=4)
