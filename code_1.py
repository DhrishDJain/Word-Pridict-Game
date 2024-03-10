import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from time import sleep
class gui(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.title('HANGMAN GAME')
        self.iconbitmap("E:\GitHub\Word Pridict Game\icon.ico")
        self.maxsize(width=1000,height=600)
        self.minsize(width=1000,height=600)
        self.config(background="#DE9E46")

    #function to clear previous canvas text
    def clr(self,i):
        try:
            canvas.delete(i)    
        except:
            pass

    #function to update and decrease(if matched condition) chances left canvas text 
    def change(self,chances):
            global tkf
            global canvas
            self.clr(tkf)
            tkf=canvas.create_text(972,20,text=f"{chances}",fill="#1c404c",font="typewriter 27 bold")

    
    def hint(self,e):
        global canvas
        global w    
        print(w)
        dic={"apple":"red","mango":"yellow","cherry":"red","peach":"peach","kiwi":"brown","grape":"green",'orange':"orange",'strawberry':"red"}
        dic_keys=list(dic.keys())
        dic_values=list(dic.values())
        for i in range(len(dic_keys)):
            if w==dic_keys[i]:
                hint=canvas.create_text(350+30,560,text=f"the colour of the fruit is {dic_values[i]}".upper(),fill="#1c404c",font="gabriola 40 bold")
                break
        hint_butt.destroy()
    


    #var to stop one extra calling of change function from inside of take funtion (declared ahead)
    global counter
    counter=0
    global canvas
    #function to create canvas
    def CANVAS(self,chances,w,letter):
        global canvas
        global inco
        global tkf
        global hint_butt
       
        canvas=Canvas(background="#DE9E46",height=900)
        l=[]
        index_loc=[] #list holding cordinate of _
        #logic to keep word in middle of window
        p=0
        d=int(len(w)/2)
        para=len(w)/2
        sub=para*64
        st=540-sub

        #loop for printing intial _
        for i in range(len(w)):
            l.append("_")
            xcord=st+p
            underscore=canvas.create_text(xcord,100+10,text=l[i],fill="#1c404c",font=('typewriter 50 bold'))
            index_loc.append(xcord)
            p+=64

        #function placing correct pridicted letter to its correct postion in word
        def blank_filling(i,user):
            l[i]=str(user)
            try:
                underscore=canvas.create_text(index_loc[i],100+10,text=l[i].upper(),fill="#1c404c",font=('typewriter 40 bold'))
                print(i,index_loc)
                index_loc.remove(index_loc[i])
            except:
                pass

        #creating and placeing stationary canvas text 
        canvas.create_text(510,50,text="HANGMAN GAME",fill="#1c404c",font="gabriola 40 bold")
        tkf=canvas.create_text(972,20,text=f"{chances}",fill="#1c404c",font="typewriter 27 bold")
        canvas.create_text(830,20,text="CHANCES LEFT : ",fill="#1c404c",font="gabriola 33")
        canvas.create_text(510,185+100,text="ENTER YOUR PRIDICTION ",fill="#1c404c",font="gabriola 40 bold")
        canvas.create_text(70,510,text="hint:".upper(),fill="#1c404c",font="gabriola 40 bold")
       

        inco=Entry(canvas,width=25,highlightcolor="#1c404c",font=("gabriola",17),highlightthickness=4,background="#DE9E46",highlightbackground="#1c404c",relief=RAISED)
        inco.place(x=390,y=221+100)

        def take_input(e):
            global z
            global chances
            global canvas
            global counter
        
            
            user=inco.get()
            inco.delete(0,END)#calling inbuilt function that clear entries in entry width when called
            chances-=1
            #loop for checking weather the pridicted letter is in word of not and also showing its result
            for i in range(len(letter)):
                try:
                    self.clr(z)
                except:
                    pass
                if str(user)=="" :
                    z=canvas.create_text(510,180+15,text="ENTER ATLEAST ONE LETTER",fill=f"#1c404c",font=f"gabriola 30 bold")
                    chances+=1
                elif user.isalpha()==False:
                    z=canvas.create_text(510,180+15,text="ENTER A LETTER",fill=f"#1c404c",font=f"gabriola 30 bold")
                    chances+=1
                elif user=="".join(letter) or l==[] or chances==0:
                    counter+=1
                    ll=list(user)
                    for x in range(len(ll)):
                        if len(index_loc)!=0:
                            blank_filling(i,ll[x])
                    blank_filling(i,user)
                    if chances==0:
                         z=canvas.create_text(510,180+15,text="try better in next round".upper(),fill=f"#1c404c",font=f"gabriola 30 bold")
                    else:
                         z=canvas.create_text(510,180+15,text="YOU WON",fill=f"#1c404c",font=f"gabriola 30 bold")
                    letter.clear()
                    chances=0
                    counter+=1
                    print(counter)
                    
                    decision=messagebox.askyesno("CONGRATULATION","WANNA PLAY MORE!!")
                    if decision==True:
                        self.destroy()
                        reset()
                    else:
                        self.destroy()
                    break

                elif user==letter[i]:
                    letter.remove(letter[i])
                    z=canvas.create_text(510,180+15,text="YOU PRIDICTED A LETTER",fill=f"#1c404c",font=f"gabriola 30 bold")
                    print(letter)
                    blank_filling(i,user)
                else:
                    z=canvas.create_text(510,180+15,text="You pridicted letter/word not match".upper(),fill=f"#1c404c",font=f"gabriola 30 bold")
                    continue
                break

            if counter==0:
                self.change(chances)
        butt=Button(canvas,text="PRIDICT",relief=RAISED,width=16,height=0,bg="#1c404c",font="gabriola 24 bold",foreground="#DE9E46",activebackground="#1c404c",justify=CENTER)
        butt.bind("<Button-1>",take_input)
        self.bind('<Return>',take_input)  
        butt.place(x=391,y=274+100)
            
        hint_butt=Button(canvas,text="HINT",relief=RAISED,width=10,height=0,bg="#1c404c",font="gabriola 24 bold",foreground="#DE9E46",activebackground="#1c404c",justify=CENTER)
        hint_butt.bind("<Button-1>",self.hint)  
        hint_butt.place(x=800,y=500)       
        canvas.pack(fill=BOTH)
    
    
    
    #function for chosing word 
    def wordchosing(self):
        global fru
        global chances
        global letter
        global w
        fru=["apple","mango","cherry","peach","kiwi","grape",'orange','strawberry']
        w=random.choice(fru)
        chances=len(w)+4
        letter=list(w)
        print(w,chances,letter)
        self.CANVAS(chances,w,letter)


def reset():
    if __name__=="__main__":
        root=gui()
    root.wordchosing()
    root.mainloop()
reset()