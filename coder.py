from tkinter import*
from tkinter import messagebox
from tkinter import filedialog



root=Tk()

root.geometry("1350x700+0+0")
root.title("billing software")
bg_color="dark Blue"
label=Label(root,text="BILLING SOFTWARE",bd=12,relief=GROOVE,bg=bg_color ,fg="white",font=('times new roman',30,'bold'),pady=2).pack(fill=X)

# Set window properties for resizing
root.geometry("1350x700+0+0")
root.title("Billing Software")
root.minsize(800, 600)  # Set minimum width and height
root.maxsize(1600, 900)  # Set maximum width and height
######### Variables  ########


cname=StringVar()
cphone=StringVar()
cbill=StringVar()



E11_name=StringVar()
E11_price=IntVar()

E21_name=StringVar()
E21_price=IntVar()

E31_name=StringVar()
E31_price=IntVar()

E41_name=StringVar()
E41_price=IntVar()

E51_name=StringVar()
E51_price=IntVar()

E61_name=StringVar()
E61_price=IntVar()

E12_name=StringVar()
E12_price=IntVar()

E22_name=StringVar()
E22_price=IntVar()

E32_name=StringVar()
E32_price=IntVar()

E42_name=StringVar()
E42_price=IntVar()

E52_name=StringVar()
E52_price=IntVar()

E62_name=StringVar()
E62_price=IntVar()

E13_name=StringVar()
E13_price=IntVar()

E23_name=StringVar()
E23_price=IntVar()

E33_name=StringVar()
E33_price=IntVar()

E43_name=StringVar()
E43_price=IntVar()

E53_name=StringVar()
E53_price=IntVar()

E63_name=StringVar()
E63_price=IntVar()


Total=StringVar()
GST=StringVar()
Total_payable=StringVar()

######### customer detail frame ###########

f1=LabelFrame(root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
f1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(f1,text="Customer Name",bg=bg_color,fg="white",font=("time new roman",18,"bold")).grid(row=0,column=0,pady=5,padx=20)
cname_txt=Entry(f1,width=15,textvariable=cname,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5)

cphone_lbl=Label(f1,text="Contact Number",bg=bg_color,fg="white",font=("time new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(f1,width=15,textvariable=cphone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

cbill_lbl=Label(f1,text="Bill Number ",bg=bg_color,fg="white",font=("time new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
cbill_txt=Entry(f1,width=15,textvariable=cbill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)


################# frame1 ###################

f2=LabelFrame(root,bd=10,relief=GROOVE,text="   PRODUCT       PRICE  ",font=("time new roman",16,"bold"),fg="gold",bg=bg_color)
f2.place(x=0,y=180,width=325,height=380)



E11=Entry(f2,width=10,textvariable=E11_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=0,pady=10,padx=10)
E11_xt=Entry(f2,width=8,textvariable=E11_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=5)

E21_txt=Entry(f2,width=10,textvariable=E21_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=0,pady=10,padx=10)
E21_xt=Entry(f2,width=8,textvariable=E21_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=5)

E31_txt=Entry(f2,width=10,textvariable=E31_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=0,pady=10,padx=10)
E31_xt=Entry(f2,width=8,textvariable=E31_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=5)

E41_txt=Entry(f2,width=10,textvariable=E41_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=0,pady=10,padx=10)
E41_xt=Entry(f2,width=8,textvariable=E41_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=5)

E51_txt=Entry(f2,width=10,textvariable=E51_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=0,pady=10,padx=10)
E51_xt=Entry(f2,width=8,textvariable=E51_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=5)

E61_txt=Entry(f2,width=10,textvariable=E61_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=0,pady=10,padx=10)
E61_xt=Entry(f2,width=8,textvariable=E61_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=5)


######################## FRAME 2 ######################

f3=LabelFrame(root,bd=10,relief=GROOVE,text="   PRODUCT       PRICE  ",font=("time new roman",16,"bold"),fg="gold",bg=bg_color)
f3.place(x=325,y=180,width=325,height=380)

E12_txt=Entry(f3,width=10,textvariable=E12_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=0,pady=10,padx=10)
E12_xt=Entry(f3,width=8,textvariable=E12_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=5)

E22_txt=Entry(f3,width=10,textvariable=E22_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=0,pady=10,padx=10)
E22_xt=Entry(f3,width=8,textvariable=E22_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=5)

E32_txt=Entry(f3,width=10,textvariable=E32_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=0,pady=10,padx=10)
E32_xt=Entry(f3,width=8,textvariable=E32_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=5)

E42_txt=Entry(f3,width=10,textvariable=E42_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=0,pady=10,padx=10)
E42_xt=Entry(f3,width=8,textvariable=E42_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=5)

E52_txt=Entry(f3,width=10,textvariable=E52_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=0,pady=10,padx=10)
E52_xt=Entry(f3,width=8,textvariable=E52_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=5)

E62_txt=Entry(f3,width=10,textvariable=E62_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=0,pady=10,padx=10)
E62_xt=Entry(f3,width=8,textvariable=E62_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=5)

##################### FRAME3 #################

f4=LabelFrame(root,bd=10,relief=GROOVE,text="   PRODUCT       PRICE  ",font=("time new roman",16,"bold"),fg="gold",bg=bg_color)
f4.place(x=650,y=180,width=325,height=380)

E13_txt=Entry(f4,width=10,textvariable=E13_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=0,pady=10,padx=10)
E13_xt=Entry(f4,width=8,textvariable=E13_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=5)

E23_txt=Entry(f4,width=10,textvariable=E23_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=0,pady=10,padx=10)
E23_xt=Entry(f4,width=8,textvariable=E23_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=5)

E33_txt=Entry(f4,width=10,textvariable=E33_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=0,pady=10,padx=10)
E33_xt=Entry(f4,width=8,textvariable=E33_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=5)

E43_txt=Entry(f4,width=10,textvariable=E43_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=0,pady=10,padx=10)
E43_xt=Entry(f4,width=8,textvariable=E43_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=5)

E53_txt=Entry(f4,width=10,textvariable=E53_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=0,pady=10,padx=10)
E53_xt=Entry(f4,width=8,textvariable=E53_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=5)

E63_txt=Entry(f4,width=10,textvariable=E63_name,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=0,pady=10,padx=10)
E63_xt=Entry(f4,width=8,textvariable=E63_price,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=5)

############## BILL AREA #############

f5=Frame(root,bd=10,relief=GROOVE)
f5.place(x=975,y=180,width=375,height=380)

bill_title=Label(f5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(f5,orient=VERTICAL)
txtarea=Text(f5,yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=txtarea.yview)
txtarea.pack(fill=BOTH,expand=1)

###################  button frame #############
f6=LabelFrame(root,bd=10,relief=GROOVE,text="Bill menu",font=("time new roman",16,"bold"),fg="gold",bg=bg_color)
f6.place(x=0,y=560,relwidth=1,height=140)

m1=Label(f6,text="GRAND TOTAL",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,)
m1_txt=Entry(f6,width=30,textvariable=Total,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

m2=Label(f6,text="GST",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,)
m2_txt=Entry(f6,width=30,textvariable=GST,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

m3=Label(f6,text="TOTAL PAYABLE PRICE",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,)
m3_txt=Entry(f6,width=30,textvariable=Total_payable,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

def cost():

    total_price= float(

        (E11_price.get())+
        (E21_price.get())+
        (E31_price.get())+
        (E41_price.get())+
        (E51_price.get())+
        (E61_price.get())+
        (E12_price.get())+
        (E22_price.get())+
        (E32_price.get())+
        (E42_price.get())+
        (E52_price.get())+
        (E62_price.get())+
        (E13_price.get())+
        (E23_price.get())+
        (E33_price.get())+
        (E43_price.get())+
        (E53_price.get())+
        (E63_price.get())

    )

    Total.set(str(total_price))

    GST.set(str(round((total_price * 0.07), 2)))

    Total_payable.set(round((total_price * 0.07), 2) + total_price)

def welcome_bill():

    txtarea.insert(END, "\n\t WELCOME")
    txtarea.insert(END, f"\n Bill Number : {cbill.get()}")
    txtarea.insert(END, f"\n Customer Name : {cname.get()}")
    txtarea.insert(END, f"\n Phone Number : {cphone.get()}")
    txtarea.insert(END, f"\n ****************************************")
    txtarea.insert(END, f"\n Products\t\t\t Price")
    txtarea.insert(END, f"\n ****************************************")
def save_bill():
    bill_data = txtarea.get("1.0", "end-1c")
    
    # Specify the fixed folder path
    folder_path = "C:/Users/user/Desktop/Billing System"  # Change this to the desired folder path
    
    # Set the default file name
    default_filename = f"{cbill.get()}.txt"
    print(cbill);
    
    # Construct the file path
    file_path = f"{folder_path}/{default_filename}"
    
    # Save the file directly
    with open(file_path, "w") as file:
        file.write(bill_data)
    
    # Show confirmation
    messagebox.showinfo("Success", f"Bill saved as {file_path}")



def bill_area():

    welcome_bill()

    if E11_price.get()!=0:
        txtarea.insert(END,f"\n {E11_name.get()}\t\t\t {E11_price.get()}")
    if E21_price.get()!=0:
        txtarea.insert(END,f"\n {E21_name.get()}\t\t\t {E21_price.get()}")
    if E31_price.get()!=0:
        txtarea.insert(END,f"\n {E31_name.get()}\t\t\t {E31_price.get()}")
    if E41_price.get()!=0:
        txtarea.insert(END,f"\n {E41_name.get()}\t\t\t {E41_price.get()}")
    if E51_price.get()!=0:
        txtarea.insert(END,f"\n {E51_name.get()}\t\t\t {E51_price.get()}")
    if E61_price.get()!=0:
        txtarea.insert(END,f"\n {E61_name.get()}\t\t\t {E61_price.get()}")
    if E12_price.get()!=0:
        txtarea.insert(END,f"\n {E12_name.get()}\t\t\t {E12_price.get()}")
    if E22_price.get()!=0:
        txtarea.insert(END,f"\n {E22_name.get()}\t\t\t {E22_price.get()}")
    if E32_price.get()!=0:
        txtarea.insert(END,f"\n {E32_name.get()}\t\t\t {E32_price.get()}")
    if E42_price.get()!=0:
        txtarea.insert(END,f"\n {E42_name.get()}\t\t\t {E42_price.get()}")
    if E52_price.get()!=0:
        txtarea.insert(END,f"\n {E52_name.get()}\t\t\t {E52_price.get()}")
    if E62_price.get()!=0:
        txtarea.insert(END,f"\n {E62_name.get()}\t\t\t {E62_price.get()}")
    if E13_price.get()!=0:
        txtarea.insert(END,f"\n {E13_name.get()}\t\t\t {E13_price.get()}")
    if E23_price.get()!=0:
        txtarea.insert(END,f"\n {E23_name.get()}\t\t\t {E23_price.get()}")
    if E33_price.get()!=0:
        txtarea.insert(END,f"\n {E33_name.get()}\t\t\t {E33_price.get()}")
    if E43_price.get()!=0:
        txtarea.insert(END,f"\n {E43_name.get()}\t\t\t {E43_price.get()}")
    if E53_price.get()!=0:
        txtarea.insert(END,f"\n {E53_name.get()}\t\t\t {E53_price.get()}")
    if E63_price.get()!=0:
        txtarea.insert(END,f"\n {E63_name.get()}\t\t\t {E63_price.get()}")

    txtarea.insert(END, "\n ----------------------------------------")
    txtarea.insert(END, f"\n Total \t\t\t {Total.get()}")
    txtarea.insert(END, f"\n Tax \t\t\t {GST.get()}")
    txtarea.insert(END,f"\n Total cost \t\t\t {Total_payable.get()}")

def clear_data():

    cname.set("")
    cphone.set("")
    cbill.set("")
    E11_name.set("")
    E11_price.set(0)

    E21_name.set("")
    E21_price.set(0)

    E31_name.set("")
    E31_price.set(0)

    E41_name.set("")
    E41_price.set(0)

    E51_name.set("")
    E51_price.set(0)

    E61_name.set("")
    E61_price.set(0)

    E12_name.set("")
    E12_price.set(0)

    E22_name.set("")
    E22_price.set(0)

    E32_name.set("")
    E32_price.set(0)

    E42_name.set("")
    E42_price.set(0)

    E52_name.set("")
    E52_price.set(0)

    E62_name.set("")
    E62_price.set(0)

    E13_name.set("")
    E13_price.set(0)

    E23_name.set("")
    E23_price.set(0)

    E33_name.set("")
    E33_price.set(0)

    E43_name.set("")
    E43_price.set(0)

    E53_name.set("")
    E53_price.set(0)

    E63_name.set("")
    E63_price.set(0)


    Total.set("")
    GST.set("")
    Total_payable.set("")

    txtarea.delete('1.0', END)

def Exit():

    root.destroy()


############### BUTTON ############

btn_f=Frame(f6,bd=7,relief=GROOVE)
btn_f.place(x=750,width=580,height=105)

total_btn=Button(btn_f,text="Total",command=cost,bg="cadetblue",fg="white",bd=2,pady=15,width=8,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
gbill_btn=Button(btn_f,text="Genrate",command=bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=8,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
clear_btn=Button(btn_f,text="Clear",command=clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=8,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
exit_btn=Button(btn_f,text="Exit",command=Exit,bg="cadetblue",fg="white",bd=2,pady=15,width=8,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
save_btn = Button(btn_f, text="Save", command=save_bill, bg="cadetblue", fg="white", bd=2, pady=15, width=7, font="arial 15 bold")
save_btn.grid(row=0, column=4, padx=5, pady=5)

root.mainloop()