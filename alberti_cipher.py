from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Texto claro')
        self.lbl2=Label(win, text='Puntero')
        self.lbl3=Label(win, text='Texto cifrado')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Add')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='Cifrar', command=self.alberti_cipher)
        self.b1.place(x=180, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def preprocess(self, plaintext):
        plaintext = plaintext.replace(' ', '')
        plaintext = plaintext.replace('H',"FF")
        plaintext = plaintext.replace('J',"II")
        plaintext = plaintext.replace('K',"QQ")
        plaintext = plaintext.replace('U',"VV")
        plaintext = plaintext.replace('W',"XX")
        plaintext = plaintext.replace('Y',"ZZ")
        plaintext = plaintext.replace('.','')
        plaintext = plaintext.replace(',','')
        plaintext = plaintext.replace(':','')
        plaintext = plaintext.replace('\n','')
        return plaintext

    def alberti_cipher(self):
        self.t3.delete(0, 'end')

        plaintext = self.t1.get()
        pointer = self.t2.get()

        plaintext = self.preprocess(plaintext)


        stationary_disk = "ABCDEFGILMNOPQRSTVXZ1234"
        movable_disk = "gklnprtuz&xysomqihfdbace"

        ciphertext = ""

        pointer_pos = movable_disk.find(pointer)
        movable_disk = movable_disk[pointer_pos:] + movable_disk[:pointer_pos]
        i = 0
        while (i < len(plaintext)):
            if plaintext[i] == '_':
                i += 1
                ciphertext += plaintext[i]
                point_pos = stationary_disk.find(plaintext[i])
                stationary_disk = stationary_disk[point_pos:] + stationary_disk[:point_pos]
            else:
                letter_pos = stationary_disk.find(plaintext[i])
                ciphertext += movable_disk[letter_pos]
            i += 1

        self.t3.insert(END, str(ciphertext))


window = Tk()
mywin = MyWindow(window)
window.title('Cifrado de Alberti')
window.geometry("400x300+10+10")
window.mainloop()