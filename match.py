from tkinter import *
import random
from tkinter import messagebox
from csv import *
from playsound import playsound
import winsound

#สร้าง Tkinker
root = Tk ()
root.title('เกมจับคู่ภาพใครใคร่เล่นก็เล่นไม่เล่นก็ออกไป๊')
root.geometry("900x900")

global winner
winner = 0

#create out matches
img_bg = PhotoImage(file = r"C:\Users\Roong\Downloads\project\png\Block.png")
img1 = PhotoImage(file = r"C:\Users\Roong\Downloads\project\png\pika.png")
img2 = PhotoImage(file = r"C:\Users\Roong\Downloads\project\png\2.png")
img3 = PhotoImage(file = r"C:\Users\Roong\Downloads\project\png\3.png")
img4 = PhotoImage(file = r"C:\Users\Roong\Downloads\project\png\4.png")
img5 = PhotoImage(file = r"C:\Users\Roong\Downloads\project\png\5.png")
img6 = PhotoImage(file = r"C:\Users\Roong\Downloads\project\png\6.png")

matches = [img1,img1,img2,img2,img3,img3,img4,img4,img5,img5,img6,img6]

#shuffle our matches
random.shuffle(matches)

#create button frame
my_frame = Frame(root)
my_frame.pack(pady=10)
but1 = Button(root,text='ไม่ลงไม่เล่นมันละออก ^^',command=root.destroy).pack()

#define some variables
count = 0
answer_list = []
answer_dict = {}

x1 = StringVar()
score=[]
with open('jiab.csv','r',encoding='utf-8-sig') as f:
    for i in f:
        score.append(int(i))
low_score = min(score)
x1.set(low_score)

#winner function
time = 0
def win():
    global time
    my_label.config(text="ยินดีด้วยคุณชนะแล้ว! เก่งมากเยี่ยมมากดีเลิศ")
    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    #loop tru buttons and change colors
    for button in button_list:
        button.config(bg="yellow")
    root.destroy()
    with open('jiab.csv','a',encoding='utf-8-sig') as f:
        f.write(str(time) + '\n')
    
#sound
def sound():
##    playsound("japan.wav")
        winsound.PlaySound('japan.wav',winsound.SND_ASYNC)
btn_sound = Button(root, text='song',bg='yellow',width=3,font=('Helvetica','20'),command=sound)
btn_sound.place(x=800, y=800)            

#funtion for clicking buttons
def button_click(b,number):
    global count,answer_list,answer_dict,winner
    global a1,a2
    global time
    
    if count < 2:
        b.configure(image = matches[number])
        #add number to answer list
        answer_list.append(number)
        #add button and number to answer dictionary
        answer_dict[b] = matches[number]
        #Increment out counter
        count += 1
        time = time + 1
        label1.configure(text="time press"+ str(time))
        if(count == 1):
            a1 =b
        else:
            a2 =b

    #เช็คว่าถูกหรือผิด
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            my_label.config(text="เก่งมากทำได้ยังไงกันเนี้ย โอโห้ว!")
            for key in answer_dict: #key =index ใน answer_dict  
                key["state"] = "disable" #ถ้าถูกให้เปลี่ยนปุ่มเป็น disable ใช้ state
#ใช้ state ในการกำหนดค่าให้ answer_dict ให้กดซ้ำไม่ได้
            count = 0
            answer_list = []
            answer_dict = {}
            #Increment our winner counter
            winner += 1
            if winner ==6:
                win()
        else:
            my_label.config(text="ผิดนะจ๊ะ เอาใหม่นะจ๊ะ!")
            count = 0
            answer_list = []
            #pop up box
            messagebox.showinfo("Incorrect!", "Incorrect")
            a1.configure(image=img_bg)
            a2.configure(image=img_bg)
            #reset the buttons
            for key in answer_dict:
                key["text"] = " " #set กลับไปเป็นปุ่มที่สามารถกดได้เหมือนเดิม " " = text =' ' 
                
            answer_dict = {}
            
#สร้างปุ่ม           
#define our buttons ใช้ lambda เพราะโค้ดจะได้สั้นลงและเรียกใช้ได้ง่าย ประกาศแค่ button_click ตัวเดียวและเรียกใช้หลาย ๆ ที
b0 = Button(my_frame, text=' ',height=200,width=200,image = img_bg,command=lambda: button_click(b0, 0))
b1 = Button(my_frame, text=' ',height=200,width=200,image = img_bg,command=lambda: button_click(b1, 1))
b2 = Button(my_frame, text=' ',height=200,width=200,image = img_bg,command=lambda: button_click(b2, 2))
b3 = Button(my_frame, text=' ',height=200,width=200,image = img_bg,command=lambda: button_click(b3, 3))
b4 = Button(my_frame, text=' ',height=200,width=200,image = img_bg,command=lambda: button_click(b4, 4))
b5 = Button(my_frame, text=' ',height=200,width=200,image = img_bg,command=lambda: button_click(b5, 5))
b6 = Button(my_frame, text=' ',height=200,width=200,image = img_bg,command=lambda: button_click(b6, 6))
b7 = Button(my_frame, text=' ',height=200,width=200,image = img_bg,command=lambda: button_click(b7, 7))
b8 = Button(my_frame, text=' ',height=200,width=200,image = img_bg,command=lambda: button_click(b8, 8))
b9 = Button(my_frame, text=' ',height=200,width=200,image = img_bg,command=lambda: button_click(b9, 9))
b10 = Button(my_frame, text=' ',height=200,width=200,image = img_bg,command=lambda: button_click(b10, 10))
b11 = Button(my_frame, text=' ',height=200,width=200,image = img_bg,command=lambda: button_click(b11, 11))

#Grid our Buttons Grid = กำหนดตำแหน่ง
b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)

b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)

my_label = Label(root, text="")
my_label.pack(pady=20)

label1 = Label(root,text = "time press",font="30")
label1.place(x=20,y=700)

label2 = Label(root,text = "High Score C:")
label2.place(x=200,y=700)

label2 = Label(root,textvariable = x1)
label2.place(x=280,y=700)

root.title
