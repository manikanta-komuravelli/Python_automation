from tkinter import *
from tkinter import messagebox
import os
import shutil



top = Tk()  
  
top.title('File Copier')  

def inforamtion():
    messagebox.showinfo("Info", "This tool is used to copy the below formatted files from the input directory provided. Incase of multiple directories, separate them by a comma ','",)

Button(top, text="INFO", command=inforamtion).grid()

checkvar1 = IntVar()  
  
checkvar2 = IntVar()  
  
checkvar3 = IntVar()  

checkvar4 = IntVar()  
  
checkvar5 = IntVar()  
  
checkvar6 = IntVar() 

checkvar7 = IntVar() 

checkvar8 = IntVar() 

checkvar9 = IntVar() 

inputvar= StringVar()

outputvar= StringVar()

inputlist=list()
inputfolderlist=list()
outputfolderlist=list()
    

def input_types():
    message= messagebox.askquestion("Confirm","Are you sure?")  
    if message == "yes":
        var1= checkvar1.get()
        var2= checkvar2.get()
        var3= checkvar3.get()
        var4= checkvar4.get()
        var5= checkvar5.get()
        var6= checkvar6.get()
        var7= checkvar7.get()
        var8= checkvar8.get()
        var9= checkvar9.get()
        inputvar1= inputvar.get()
        outputvar1= outputvar.get()
        if var1 == 1:
            inputlist.append('csv')
        if var2 == 1:
            inputlist.append('docx')
        if var3 == 1:
            inputlist.append('pptx')
        if var4 == 1:
            inputlist.append('txt')
        if var5 == 1:
            inputlist.append('xls')
        if var6 == 1:
            inputlist.append('zip')
        if var7 == 1:
            inputlist.append('pdf')
        if var8 == 1:
            inputlist.append('jpg')
        inputfolderlist.append(inputvar1)
        outputfolderlist.append(outputvar1)
        top.destroy()  
    


Label(top, text="Inputfolders").grid(row=1,column=0)

Label(top, text= "Destinationfolder").grid(row=2,column=0)

Entry(top, textvariable=inputvar).grid(row=1,column=1)

Entry(top, textvariable=outputvar).grid(row=2,column=1)

Checkbutton(top, text = "CSV", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10).grid(row=3,column=0) 
  
Checkbutton(top, text = "DOCX", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10).grid(row=3,column=1) 
  
Checkbutton(top, text = "PPTX", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10).grid(row=3,column=2) 

Checkbutton(top, text = "TXT", variable = checkvar4, onvalue = 1, offvalue = 0, height = 2, width = 10).grid(row=4,column=0) 
  
Checkbutton(top, text = "XLS", variable = checkvar5, onvalue = 1, offvalue = 0, height = 2, width = 10).grid(row=4,column=1) 
  
Checkbutton(top, text = "ZIP", variable = checkvar6, onvalue = 1, offvalue = 0, height = 2, width = 10).grid(row=4,column=2) 

Checkbutton(top, text = "PDF", variable = checkvar7, onvalue = 1, offvalue = 0, height = 2, width = 10).grid(row=5,column=0) 
  
Checkbutton(top, text = "JPG", variable = checkvar8, onvalue = 1, offvalue = 0, height = 2, width = 10).grid(row=5,column=1) 

#Button(top, text="OK", command=input_types).grid(row=6,column=1)

Button(top, text="Confirm", command=input_types).grid(row=7,column=1)


top.mainloop()  

#print(inputlist,inputfolderlist,outputfolderlist)

for i in outputfolderlist:
    destpath= i
    
for i in inputlist:
    if i == "csv":
        csv_path= destpath+"\\csv_files"
        if os.path.exists(csv_path):
            continue
        else:
            os.mkdir(csv_path)
    elif i == "docx":
        docx_path= destpath+"\\docx_files"
        if os.path.exists(docx_path):
            continue
        else:
            os.mkdir(docx_path)
    elif i == "pptx":
        pptx_path= destpath+"\\pptx_files"
        if os.path.exists(pptx_path):
            continue
        else:
            os.mkdir(pptx_path)
    elif i == "txt":
        txt_path= destpath+"\\txt_files"
        if os.path.exists(txt_path):
            continue
        else:
            os.mkdir(txt_path)
    elif i == "xls":
        xlsx_path= destpath+"\\xlsx_files"
        if os.path.exists(xlsx_path):
            continue
        else:
            os.mkdir(xlsx_path)
    elif i == "zip":
        zip_path= destpath+"\\zip_files"
        if os.path.exists(zip_path):
            continue
        else:
            os.mkdir(zip_path)
    elif i == "pdf":
        pdf_path= destpath+"\\pdf_files"
        if os.path.exists(pdf_path):
            continue
        else:
            os.mkdir(pdf_path)
    elif i == "jpg":
        jpg_path= destpath+"\\jpg_files"
        if os.path.exists(jpg_path):
            continue
        else:
            os.mkdir(jpg_path)
            

input_folders=list()

for i in inputfolderlist:
   input_folders.extend(i.split(',')) 

for inputs in input_folders:
    for root, dirs, files in os.walk(inputs):
        for file_ in files:
            if file_[-3:] == "csv" and file_[-3:] in inputlist:
                full_path=os.path.join(root,file_) 
                shutil.copy(full_path,csv_path)
            elif file_[-4:] == "docx" and file_[-4:] in inputlist:
                full_path=os.path.join(root,file_) 
                shutil.copy(full_path,docx_path)
            elif file_[-4:] == "pptx" and file_[-4:] in inputlist:
                full_path=os.path.join(root,file_) 
                shutil.copy(full_path,pptx_path)
            elif file_[-3:] == "txt" and file_[-3:] in inputlist:
                full_path=os.path.join(root,file_) 
                shutil.copy(full_path,txt_path)
            elif file_[-4:-1] == "xls" and file_[-4:-1] in inputlist:
                full_path=os.path.join(root,file_) 
                shutil.copy(full_path,xlsx_path)
            elif file_[-3:] == "zip" and file_[-3:] in inputlist:
                full_path=os.path.join(root,file_) 
                shutil.copy(full_path,zip_path)
            elif file_[-3:] == "pdf" and file_[-3:] in inputlist:
                full_path=os.path.join(root,file_) 
                shutil.copy(full_path,pdf_path)
            elif file_[-3:] == "jpg" and file_[-3:] in inputlist:
                full_path=os.path.join(root,file_) 
                shutil.copy(full_path,jpg_path)
                