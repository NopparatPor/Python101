#เวลา save file name ห้ามใช้ชื่อเดียวกับ library (ห้าม save ว่า tkinter)
from tkinter import *
from tkinter import ttk #theme ของ tk
from tkinter import messagebox

GUI = Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดของโปรแกรม


B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท') #นี่คือปุ่มกด แบบสวยๆ(มีสีฟ้าๆ)
B1.pack(ipadx=20,ipady=20) #ทำให้เห็นปุ่มขึ้นมา ตำแหน่งปุ่มจะอยู่บนกลางหน้าจอ

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
###################################################คั่น

#def คือฟังก์ชันที่เอาไว้เก็บคำสั่งหลายๆคำสั่ง
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text) #สามารถเขียน show ได้หลายแบบ คือ showwarning, showinfo , showerror เสียงก็จะขึ้นมาต่างกันด้วยแต่ละอัน

FB1 = LabelFrame(GUI,text='Money') #เหมือนกระดาน
FB1.place(x=100,y=50)

B2 = Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2) #ปุ่มแบบไม่สวย นูนๆ
B2.pack(ipadx=20,ipady=20,padx=30,pady=30)
#B2.place(x=50,y=200)

################################################คั่น

GUI.mainloop()
