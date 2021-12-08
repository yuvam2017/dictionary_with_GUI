from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk
from tkinter import messagebox
import subprocess

class App:
	def __init__(self,root):
		self.root = root
		root.title("Dictionary")
		root.configure(bg="white")
		root.geometry("1300x800+0+0")
		root.bind('<Return>',self.findMeaning)

		self.makeFrame()

	def makeFrame(self):
		###### Heading ######
		# self.label_heading = ttk.Label(self.root,text="Dictionary",background="white",foreground="blue",font="Poppins 60 bold")
		# self.label_heading.place(relx=0.5,rely=0.1,anchor=CENTER)

		###### Entry and label ######
		self.label_entry = ttk.Label(self.root,text="Enter the word : ",background="white",foreground="black",font="Poppins 40 bold")
		self.label_entry.place(x=350,y=50,anchor=CENTER)

		self.entry_word = ttk.Entry(self.root,font="Poppins 25",foreground="purple",width="30")
		self.entry_word.place(x=890,y=50,anchor=CENTER)

		self.button = ttk.Button(self.root,text="Submit")
		self.button.place(x=645,y=100,anchor=CENTER)

	def findMeaning(self,event):
		self.word = self.entry_word.get();
		if self.word == "" or self.word == " ":
			# alert the user
			messagebox.showerror("Word Not Found", "Check the spelling of the word!\n The word not found in database")
		else :
			self.text = subprocess.getoutput(f"dict {self.word}")
			print(self.text)
			self.createScrollableText()

	def createScrollableText(self):
		try:
			self.output.destroy()
			self.vert.destroy()
			self.hori.destroy()
		except Exception as e:

			print(e)

		self.hori = Scrollbar(root, orient = 'horizontal')
		self.hori.pack(side = BOTTOM, fill = X)
		self.vert = Scrollbar(root)
		self.vert.pack(side = RIGHT, fill = Y)
		self.output = Text(self.root, width = 20, height = 20, wrap = NONE,
				xscrollcommand = self.hori.set,
				yscrollcommand = self.vert.set)
		self.output.insert(END,f'{self.text}\n')
		# self.output.pack(side=BOTTOM,fill=X)
		self.output.place(x=0,rely=0.2,relwidth=1,relheight=1)
		self.hori.config(command=self.output.xview)
		self.vert.config(command=self.output.yview)


if __name__ == "__main__":
	root = ThemedTk(theme="adapta")
	App(root)
	root.mainloop()
