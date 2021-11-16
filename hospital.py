from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NoofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()


        lbltitle = Label(self.root, bd=20, relief=RIDGE, text = "HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # Dataframe
        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(X=0,Y=130,width=1530,height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(X=0,Y=5,width=980,height=350)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")
        DataFrameRight.place(X=990,Y=5,width=460,height=350)


        # Buttonframe
        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(X=0,Y=530,width=1530,height=70)


        # Detailsframe
        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailsFrame.place(X=0,Y=600,width=1530,height=190)


        # DataframeLeft
        lblNameTablet = Label(DataFrameLeft, text="Name of Tablet", font=("times new roman", 12, "bold"), padX=2, padY=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet = ttk.Combobox(DataFrameLeft,textvarible=self.Nameoftablets, state="readonly",font=("times new roman", 12, "bold"), width=33)
        comNametablet["values"] = ("Nice","Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No:", padX=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1,column=1)

        lblDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dose:", padX=2,padY=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2,column=1)

        lblNoOfTablets = Label(DataFrameLeft, font=("arial", 12, "bold"), text="No. of Tablets:", padX=2,padY=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtNoOfTablets.grid(row=3,column=1)

        lblLot = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot:", padX=2,padY=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padX=2,padY=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padX=2,padY=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Daily Dose:", padX=2,padY=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padX=2,padY=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Further Information:", padX=2)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padX=2, padY=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Storage Advice:", padX=2, padY=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medication:", padX=2, padY=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtMedicine.grid(row=3,column=3,sticky=W)

        lblPatientID = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient ID:", padX=2, padY=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        txtPatientID = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtPatientID.grid(row=4,column=3)

        lblNhsNumber = Label(DataFrameLeft, font=("arial", 12, "bold"), text="NHS Number:", padX=2, padY=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name:", padX=2, padY=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date of Birth:", padX=2, padY=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address:", padX=2, padY=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtPatientAddress.grid(row=8,column=3)


        #DataFrameRight
        self.txtPrescription = Text(DataFrameRight, font=("arial", 12, "bold"), width=45, height=16,padY=6)
        self.txtPrescription.grid(row=0,column=0)


        #Buttons
        btnPrescription = Button(ButtonFrame,text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=23, height=16,padY=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(ButtonFrame,text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=23, height=16,padY=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate = Button(ButtonFrame,text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=23, height=16,padY=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete = Button(ButtonFrame,text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=23, height=16,padY=6)
        btnDelete.grid(row=0,column=3)

        btnClear = Button(ButtonFrame,text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=23, height=16,padY=6)
        btnClear.grid(row=0,column=4)

        btnExit = Button(ButtonFrame,text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=23, height=16,padY=6)
        btnExit.grid(row=0,column=5)


        #Table
            #Scrollbar
        scroll_x = ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
        self.hospital_table = ttk.TreeView(DetailsFrame,column=("nameoftablet", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)    
        scroll_x.pack = (side=BOTTOM, fill=X)
        scroll_y.pack = (side=RIGHT, fill=Y)
        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No. Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="DNS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("addtess",text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)

        
# Functionality Declaration



root = Tk()
ob = Hospital(root)
root.mainloop()
