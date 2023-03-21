from tkinter import *
from tkinter import messagebox
import os

class bill_app:
    def __init__(self,root):
        self.root = root
        self.root.title("Billing Software")
        self.root.iconbitmap("Lgp85-Magic-Christmas-My-Documents.ico")
        self.root.geometry("1920x1080+0+0")
        bg_color = "#FB3597"
        font_color = "#FBFBFB"
        font_style = "Times New Roman"
        label1 = Label(self.root, text="WHITE HOUSE DRYCLEANERS", bg=bg_color, fg=font_color, font=(font_style, 30, "bold"), relief="raised", bd=5, pady=5)
        label1.pack(fill=X)

#==========variables============


        self.cname = StringVar()
        self.c_ph_no = StringVar()
        self.c_email = StringVar()
        self.c_bill_no = StringVar()
        self.billno = IntVar()
        self.billno = 1
        self.searchBill = StringVar()

        self.d_blanket = IntVar()
        self.d_saree = IntVar()
        self.d_shirt = IntVar()

        self.s_blanket = IntVar()
        self.s_saree = IntVar()
        self.s_shirt = IntVar()

        self.c_saree = IntVar()

        self.DryClean_price = StringVar()
        self.SteamPress_price = StringVar()
        self.Charak_price = StringVar()

        #==========details==============

        f1 = LabelFrame(self.root, text="Costumer Details: ",bd=5, pady=2, font=(font_style, 15, "bold"), fg=font_color, bg=bg_color)
        f1.place(x=0, y=60, relwidth = 1)

        lbl_name = Label(f1, text="Name: ", font=(font_style, 15, "bold"))
        lbl_name.grid(row=0, column=0, padx=10)
        e1 = Entry(f1,width=20,borderwidth=5, textvariable = self.cname)
        e1.grid(row=0,column=1, padx=10)

        lbl_ph_no = Label(f1, text="Phone No: ", font=(font_style, 15, "bold"))
        lbl_ph_no.grid(row=0, column=2, padx=10)
        e2 = Entry(f1, width=20, borderwidth=5, textvariable = self.c_ph_no)
        e2.grid(row=0, column=3, padx=10)

        lbl_email = Label(f1, text="E-mail", font=(font_style,15,"bold"))
        lbl_email.grid(row=0, column=4, padx=10)
        e4 = Entry(f1, width=40, borderwidth=5, textvariable = self.c_email,)
        e4.grid(row=0,column=5, padx=10)
        e4.insert(0,"nil")

        lbl_bill_no = Label(f1, text="Bill No: ", font=(font_style, 15, "bold"))
        lbl_bill_no.grid(row=0, column=6, padx=10)
        e3 = Entry(f1, width=20, borderwidth=5, textvariable = self.c_bill_no)
        e3.grid(row=0, column=7, padx=10)

        btn1 = Button(f1, text="Search",bd=5, bg="White", fg="Black", relief="raised", font=(font_style,15,"bold"),command=self.search_bill)
        btn1.grid(row=0, column=8,padx=20,pady=10)

#=========drycleaning==============

        f2=LabelFrame(self.root,text="DryCleaning", bd=5, font=(font_style,15,"bold"), bg=bg_color, fg=font_color)
        f2.place(x=2,y=160)

        lbl_blanket = Label(f2, text="Blanket", font=(font_style,15,"bold"))
        lbl_blanket.grid(row=0, column=0,padx=5, pady=4, sticky="w")
        blanket_e = Entry(f2, width=5, borderwidth = 5, textvariable = self.d_blanket)
        blanket_e.grid(row=0, column=1, padx=10)

        lbl_saree = Label(f2, text="Saree", font=(font_style, 15, "bold"))
        lbl_saree.grid(row=1, column=0, padx=5, pady=4, sticky="w")
        saree_e = Entry(f2, width=5, borderwidth=5, textvariable = self.d_saree)
        saree_e.grid(row=1, column=1, padx=10)

        lbl_shirt = Label(f2, text="Shirt", font=(font_style, 15, "bold"))
        lbl_shirt.grid(row=2, column=0, padx=5, pady=4, sticky="w")
        shirt_e = Entry(f2, width=5, borderwidth=5, textvariable = self.d_shirt)
        shirt_e.grid(row=2, column=1, padx=10)

#===========press=============

        f3 = LabelFrame(self.root, text="Steam-Press", font=(font_style, 15, "bold"), bg=bg_color, fg=font_color, bd=5)
        f3.place(x=250, y=160)

        lbl_blanket_sp = Label(f3, text="Blanket", font=(font_style, 15, "bold"))
        lbl_blanket_sp.grid(row=0, column=0, padx=5, pady=4, sticky="w")
        blanket_sp_e = Entry(f3, width=5, borderwidth=5, textvariable=self.s_blanket)
        blanket_sp_e.grid(row=0, column=1, padx=10)

        lbl_saree_sp = Label(f3, text="Saree", font=(font_style, 15, "bold"))
        lbl_saree_sp.grid(row=1, column=0, padx=5, pady=4, sticky="w")
        saree_sp_e = Entry(f3, width=5, borderwidth=5, textvariable=self.s_saree)
        saree_sp_e.grid(row=1, column=1, padx=10)

        lbl_shirt_sp = Label(f3, text="Shirt", font=(font_style, 15, "bold"))
        lbl_shirt_sp.grid(row=2, column=0, padx=5, pady=4, sticky="w")
        shirt_sp_e = Entry(f3, width=5, borderwidth=5, textvariable=self.s_shirt)
        shirt_sp_e.grid(row=2, column=1, padx=10)

#=========charak===============

        f4 = LabelFrame(self.root, text="Charak", font=(font_style, 15, "bold"), fg=font_color, bg=bg_color, bd=5)
        f4.place(x=250, y=305)

        lbl_saree_c = Label(f4, text="Saree", font=(font_style, 15, "bold"))
        lbl_saree_c.grid(row=0, column=0)
        saree_c_e = Entry(f4, width=5, borderwidth=5, textvariable=self.c_saree)
        saree_c_e.grid(row=0, column=1, padx=10)

#=========display=========
        f5 = Frame(self.root, bd=5, relief="groove")
        f5.place(x=870, y=160, width=400, height=400)
        bill_label = Label(f5, text="Bill Area", font=("arial", 15, "bold"), bd=5, relief=GROOVE)
        bill_label.pack(fill=X)
        scroll = Scrollbar(f5, orient=VERTICAL)
        self.textarea = Text(f5,yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

#===============buttons==============

        f6=LabelFrame(self.root, text="Bill Menu", relief=GROOVE, bg=bg_color,fg=font_color,font=(font_style,15,"bold"),bd=5)
        # f6.place(x=870,y=560)
        f6.place(x=0, y=560, relwidth=1, height=140)

        lbl_total_dc = Label(f6, text="Dry-Clean Total", font=(font_style, 15, "bold"))
        lbl_total_dc.grid(row=0, column=0, padx=5, pady=4, sticky="w")
        total_dc_e = Entry(f6, width=18, borderwidth=5, textvariable=self.DryClean_price)
        total_dc_e.grid(row=0, column=1, padx=10)

        lbl_total_sp = Label(f6, text="Steam-Press Total", font=(font_style, 15, "bold"))
        lbl_total_sp.grid(row=0, column=2, padx=5, pady=4, sticky="w")
        total_sp_e = Entry(f6, width=18, borderwidth=5, textvariable=self.SteamPress_price)
        total_sp_e.grid(row=0, column=3, padx=10)

        lbl_total_ck = Label(f6, text="Charak Total", font=(font_style, 15, "bold"))
        lbl_total_ck.grid(row=0, column=4, padx=5, pady=4, sticky="w")
        total_ck_e = Entry(f6, width=18, borderwidth=5, textvariable=self.Charak_price)
        total_ck_e.grid(row=0, column=5, padx=10)

        total_btn = Button(f6,text="TOTAL",bd=5, bg="White", fg="Black", relief="raised", font=(font_style,15,"bold"), command=self.total_bill)
        total_btn.grid(row=0,column=8,padx=9,pady=5)

        bill_btn = Button(f6, text="BILL", bd=5, bg="White", fg="Black", relief="raised", font=(font_style, 15, "bold"), command = self.bill_area)
        bill_btn.grid(row=0, column=9,padx=9,pady=5)

        # clear_btn = Button(f6, text="CLEAR", bd=5, bg="White", fg="Black", relief="raised", font=(font_style, 15, "bold"),command=self.clear_bill)
        # clear_btn.grid(row=0, column=10, padx=9,pady=5)

        new_bill_btn = Button(f6, text="New Bill", bd=5, bg="White", fg="Black", relief="raised", font=(font_style, 15, "bold"), command=self.bill_no)
        new_bill_btn.grid(row=0, column=10, padx=9,pady=5)


        # self.bill_layout()

    def total_bill(self):
        self.blanket_dry = 160
        self.saree_dry = 120
        self.shirt_dry = 60
        self.price_blanket_dry = self.d_blanket.get() * self.blanket_dry
        self.price_saree_dry = self.d_saree.get() * self.saree_dry
        self.price_shirt_dry = self.d_shirt.get() * self.shirt_dry


        self.blanket_sp = 0
        self.saree_sp = 30
        self.shirt_sp = 20
        self.price_blanket_sp = self.s_blanket.get() * self.blanket_sp
        self.price_saree_sp = self.s_saree.get() * self.saree_sp
        self.price_shirt_sp = self.s_shirt.get() * self.shirt_sp

        self.saree_c = 15
        self.price_saree_c = self.c_saree.get() * self.saree_c

        self.total_dry_clean_cost = float(
            (self.price_blanket_dry) +
            (self.price_saree_dry) +
            (self.price_shirt_dry)
        )
        self.total_steam_press_cost = float(
            (self.price_blanket_sp) +
            (self.price_saree_sp) +
            (self.price_shirt_sp)
        )
        self.total_charak_cost = float(
            (self.price_saree_c)
        )

        self.DryClean_price.set(str(self.total_dry_clean_cost))
        self.SteamPress_price.set(str(self.total_steam_press_cost))
        self.Charak_price.set(str(self.total_charak_cost))
        self.total_cost = ((self.total_dry_clean_cost)+(self.total_steam_press_cost)+(self.total_charak_cost))

    def bill_no(self):
        self.c_bill_no.set(str(self.billno))
        self.billno = self.billno + 1

        self.cname.set("")
        self.c_ph_no.set("")
        self.searchBill.set("")

        self.d_blanket.set(0)
        self.d_saree.set(0)
        self.d_shirt.set(0)

        self.s_blanket.set(0)
        self.s_saree.set(0)
        self.s_shirt.set(0)

        self.c_saree.set(0)

        self.DryClean_price.set("")
        self.SteamPress_price.set("")
        self.Charak_price.set("")



    def welcome(self):
        self.textarea.delete("1.0", END)
        self.textarea.insert(END, "            WHITE HOUSE DRYCLEANERS           \n")
        self.textarea.insert(END, "            Kataria Market  Link Road          \n")
        self.textarea.insert(END, "==============================================\n")
        # self.textarea.insert(END,"\tWelcome to White House Drycleaners")
        self.textarea.insert(END, f"\nBill No: {self.c_bill_no.get()}")
        self.textarea.insert(END, f"\nName: {self.cname.get()}")
        self.textarea.insert(END, f"\nPhone No: {self.c_ph_no.get()}")
        self.textarea.insert(END, "\n==============================================")
        self.textarea.insert(END, "\nProduct\t\t\tQty\t\tPrice")
        self.textarea.insert(END, "\n==============================================")

    def bill_area(self):
        if self.cname.get() == '' or self.c_ph_no.get() == '':
            messagebox.showerror("ERROR","Customer Details are Must !")
        elif self.DryClean_price.get() == '0.0' and self.SteamPress_price.get() == '0.0' and self.Charak_price.get() == '0.0':
            messagebox.showerror("ERROR","Add Something !")
        else:
            self.welcome()
            #=======DryClean==========
            if self.d_blanket.get() !=0:
                self.textarea.insert(END, f"\nBlanket Dry-clean\t\t\t{self.d_blanket.get()}\t\t{self.price_blanket_dry}")
            if self.d_saree.get() != 0:
                self.textarea.insert(END, f"\nSaree Dry-clean\t\t\t{self.d_saree.get()}\t\t{self.price_saree_dry}")
            if self.d_shirt.get() != 0:
                self.textarea.insert(END, f"\nShirt Dry-clean\t\t\t{self.d_shirt.get()}\t\t{self.price_shirt_dry}")
            #=======SteamPress==========
            if self.s_blanket.get() != 0:
                self.textarea.insert(END, f"\nBlanket Steam-Press\t\t\t{self.s_blanket.get()}\t\t{self.price_blanket_sp}")
            if self.s_saree.get() != 0:
                self.textarea.insert(END, f"\nSaree Steam-Press\t\t\t{self.s_saree.get()}\t\t{self.price_saree_sp}")
            if self.s_shirt.get() != 0:
                self.textarea.insert(END, f"\nShirt Steam-Press\t\t\t{self.s_shirt.get()}\t\t{self.price_shirt_sp}")
            #=======Charak==========
            if self.c_saree.get() != 0:
                self.textarea.insert(END, f"\nSaree Charak\t\t\t{self.c_saree.get()}\t\t{self.price_saree_c}")

            #=======Total==========
            self.textarea.insert(END, "\n----------------------------------------------")
            self.textarea.insert(END, f"\nTotal\t\t\t\t\t{self.total_cost}")
            self.textarea.insert(END, "\n----------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("SAVE BILL", "Do you want to save the Bill ?")
        if op>0:
            self.bill_data = self.textarea.get('1.0',END)
            f1=open("bills/"+str(self.c_ph_no.get())+"."+str(self.c_bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved!",f"Bill No: {self.c_bill_no.get()} has been saved !")
        else:
            return

    #

    def search_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split(".")[0] == self.c_bill_no.get() or i.split(".")[1] == self.c_bill_no.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete("1.0",END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("ERROR","Bill not Found !")

    # def clear_bill(self):
    #
    #     self.cname.set("")
    #     self.c_ph_no.set("")
    #     self.searchBill.set("")
    #
    #     self.d_blanket.set(0)
    #     self.d_saree.set(0)
    #     self.d_shirt.set(0)
    #
    #     self.s_blanket.set(0)
    #     self.s_saree.set(0)
    #     self.s_shirt.set(0)
    #
    #     self.c_saree.set(0)
    #
    #     self.DryClean_price.set("")
    #     self.SteamPress_price.set("")
    #     self.Charak_price.set("")






root = Tk()
obj = bill_app(root)
root.mainloop()