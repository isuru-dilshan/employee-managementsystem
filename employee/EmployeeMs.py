from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')

        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg="#fafcfb")
        lbl_title.place(x=0,y=0,width=1530,height=50)

    # Logo ============================================================================================

        img_logo=Image.open(r"C:\Users\Isuru Dilshan\Documents\python\EmployeeMS\Empimg\download.png")
        img_logo=img_logo.resize((60,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=260,y=0,width=60,height=50)

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=163)
    # 1st =============================================================================================

        img1=Image.open(r"C:\Users\Isuru Dilshan\Documents\python\EmployeeMS\Empimg\employees.png")
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)
    # 2nd =============================================================================================

        img2 = Image.open(r"C:\Users\Isuru Dilshan\Documents\python\EmployeeMS\Empimg\employee.jpg")
        img2 = img2.resize((540, 160), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=540, y=0, width=540, height=160)
    # 3rd ==============================================================================================

        img3 = Image.open(r"C:\Users\Isuru Dilshan\Documents\python\EmployeeMS\Empimg\employees.jpg")
        img3 = img3.resize((540, 160), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=1000, y=0, width=540, height=160)

        # Main Frame ===================================================================================

        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=220,width=1500,height=560)

        # upper Frame =================================================================================

        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',12,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # Labels and Entity fields =====================================================================

        lbl_dep=Label(upper_frame,text='Department:',font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=20,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Name ============

        lbl_name=Label(upper_frame,font=("arial",11,"bold"),text="Name:",bg="white")
        lbl_name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_name.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        # PhoneNO =========

        lbl_phone=Label(upper_frame,font=("arial",11,"bold"),text="Phone No:",bg="white")
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_phone.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        # Designation =========

        lbl_designation=Label(upper_frame,font=("arial",11,"bold"),text="Designation:",bg="white")
        lbl_designation.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        txt_designation=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_designation.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Email =============

        lbl_email=Label(upper_frame,font=("arial",11,"bold"),text="Email:",bg="white")
        lbl_email.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        txt_email=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_email.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Country ============

        lbl_country=Label(upper_frame,font=("arial",11,"bold"),text="Country:",bg="white")
        lbl_country.grid(row=1,column=4,padx=2,pady=10,sticky=W)

        txt_country=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_country.grid(row=1,column=5,padx=2,pady=10,sticky=W)

        # Address ============

        lbl_address=Label(upper_frame,font=("arial",11,"bold"),text="Address:",bg="white")
        lbl_address.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        txt_address=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_address.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # Married Status =====

        lbl_married=Label(upper_frame,font=("arial",11,"bold"),text="Married Status:",bg="white")
        lbl_married.grid(row=2,column=2,padx=2,pady=10,sticky=W)

        combo_marrried = ttk.Combobox(upper_frame, font=('arial', 12, 'bold'), width=20, state='readonly')
        combo_marrried['value'] = ( 'Married', 'UnMarried', 'Engage')
        combo_marrried.current(0)
        combo_marrried.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # Salary ==============

        lbl_salary=Label(upper_frame,font=("arial",11,"bold"),text="Salary(CTC):",bg="white")
        lbl_salary.grid(row=2,column=4,padx=2,pady=10,sticky=W)
        
        txt_salary=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_salary.grid(row=2,column=5,padx=2,pady=10,sticky=W)

        # DOB =================

        lbl_BOD=Label(upper_frame,font=("arial",11,"bold"),text="Date Of Birth:",bg="white")
        lbl_BOD.grid(row=3,column=0,padx=2,pady=10,sticky=W)

        txt_BOD=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_BOD.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        # DOJ =================

        lbl_DOJ=Label(upper_frame,font=("arial",11,"bold"),text="Date Of Join:",bg="white")
        lbl_DOJ.grid(row=3,column=2,padx=2,pady=10,sticky=W)

        txt_DOJ=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_DOJ.grid(row=3,column=3,padx=2,pady=10,sticky=W)
        # Id Proof ======================

        com_txt_proof=ttk.Combobox(upper_frame,state="readonly",font=("arial",12,"bold"),width=20)
        com_txt_proof['value']=("Select ID Prood:","PAN CARD","ADHAR CARD","DRIVING LICENCE")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_proof=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_proof.grid(row=4,column=1,padx=2,pady=10,sticky=W)

        # Gender ========================

        lbl_gender=Label(upper_frame,font=("arial",11,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(upper_frame,state="readonly",font=("arial",12,"bold"),width=20)
        com_txt_gender['value']=("Male","Female")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        # mask image ========================

        img4=Image.open(r"C:\Users\Isuru Dilshan\Documents\python\EmployeeMS\Empimg\mask.jpg")
        img4=img4.resize((250,220),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img4)

        self.img4=Label(upper_frame,image=self.photo4)
        self.img4.place(x=1055,y=0,width=225,height=220)

        # Button Frame =======================
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1290,y=30,width=170,height=170)

        # buttons ============================

        btn_add=Button(button_frame,text="Save",font=("arial",15,"bold"),width=13,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=0)

        btn_update=Button(button_frame,text="Update",font=("arial",15,"bold"),width=13,bg='green',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=0)

        btn_delete=Button(button_frame,text="Delete",font=("arial",15,"bold"),width=13,bg='red',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=0)

        btn_clear=Button(button_frame,text="Clear",font=("arial",15,"bold"),width=13,bg='#c9b414',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=0)

        # down Frame ====================================================================================

        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',12,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)

        # Search Frame ===================================================================================

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text=' Search Employee Information',font=('times new roman',12,'bold'),fg='blue')
        search_frame.place(x=0,y=0,width=1470,height=60)

        # search ===========================

        com_txt_gender = ttk.Combobox(search_frame, state="readonly", font=("arial", 12, "bold"), width=20)
        com_txt_gender['value'] = ("Select Option", "Phone","Id_proof")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=0, column=1, sticky=W, padx=5,)

        txt_search = ttk.Entry(search_frame, width=22, font=("arial", 12, "bold"))
        txt_search.grid(row=0, column=2, padx=5)

        btn_search = Button(search_frame, text="Search", font=("arial", 12, "bold"), width=14, bg='red', fg='white')
        btn_search.grid(row=0, column=3, padx=5)

        btn_showall = Button(search_frame, text="Show All", font=("arial", 12, "bold"), width=14, bg='blue', fg='white')
        btn_showall.grid(row=0, column=4, padx=5)

        company_logo=Label(search_frame,text="iCrown SoftCompany (PVT)",font=("time new roman",20,"bold"),bg="white",fg="blue")
        company_logo.place(x=780,y=0,width=600,height=30)

        logo=Image.open(r"C:\Users\Isuru Dilshan\Documents\python\EmployeeMS\Empimg\download.png")
        logo=logo.resize((60,50),Image.ANTIALIAS)
        self.photo5=ImageTk.PhotoImage(logo)

        self.logo=Label(search_frame,image=self.photo5)
        self.logo.place(x=830,y=0,width=60,height=30)

        # =================== Employee Table =====================================
        # Table Frame =============

        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","degi","email","address","married","dob","doj","idproofcomb","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Designation')
        self.employee_table.heading('email',text="Email")
        self.employee_table.heading('address',text="Address")
        self.employee_table.heading('married',text="Married Status")
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text="DOJ")
        self.employee_table.heading('idproofcomb',text="ID Type")
        self.employee_table.heading('idproof',text="ID Proof")
        self.employee_table.heading('gender',text="Gender")
        self.employee_table.heading('phone',text="Phone")
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show']='headings'
        self.employee_table.column("dep",width=100)
        self.employee_table.pack(fill=BOTH,expand=1)

        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('degi',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('married',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idproofcomb',width=100)
        self.employee_table.column('idproof',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)



if __name__ =="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()

