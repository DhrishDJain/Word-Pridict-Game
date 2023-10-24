import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import sleep
class gui(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.title('HANGMAN GAME')
        self.maxsize(width=1000,height=600)
        self.minsize(width=1000,height=600)
        self.config(background="#DE9E46")
         
    def clr(self,i):
        try:
            canvas.delete(i)    
        except:
            pass

    def CANVAS(self,chances,w,letter):
        global canvas
        global inco
        global t
        canvas=Canvas(background="#DE9E46",height=900)
        l=[]
        index_loc=[]
        p=0
        d=int(len(w)/2)
        #logic to keep word in middle of window
        para=len(w)/2
        sub=para*64
        st=540-sub
        for i in range(len(w)):
            l.append("_")
            xcord=st+p
            underscore=canvas.create_text(xcord,100+10,text=l[i],fill="#1c404c",font=('typewriter 50 bold'))
            index_loc.append(xcord)
            p+=64
        def blank_filling(i,user):
            l[i]=str(user)
            try:
                underscore=canvas.create_text(index_loc[i],100+10,text=l[i].upper(),fill="#1c404c",font=('typewriter 40 bold'))
                print(i,index_loc)
                index_loc.remove(index_loc[i])
            except:
                pass
        canvas.create_text(510,50,text="HANGMAN GAME",fill="#1c404c",font="gabriola 40 bold")
        t=canvas.create_text(972,20,text=f"{chances}",fill="#1c404c",font="typewriter 27 bold")
        canvas.create_text(830,20,text="CHANCES LEFT : ",fill="#1c404c",font="gabriola 33")
        canvas.create_text(510,185+100,text="ENTER YOUR PRIDICTION ",fill="#1c404c",font="gabriola 40 bold")
        inco=Entry(canvas,width=25,highlightcolor="#1c404c",font=("gabriola",17),highlightthickness=4,background="#DE9E46",highlightbackground="#1c404c",relief=RAISED)
        inco.place(x=390,y=221+100)
    
        def take(event):
            global z
            
            user=inco.get()
            inco.delete(0,END)
            for i in range(len(letter)):
                if user=="".join(letter) or l==[]:
                    ll=list(user)
                    for x in range(len(ll)):
                        if len(index_loc)!=0:
                            blank_filling(i,ll[x])
                    try:
                        self.clr(z)
                    except:
                        pass
                    blank_filling(i,user)
                    z=canvas.create_text(510,180+15,text="YOU WON",fill=f"#1c404c",font=f"gabriola 30 bold")
                    letter.clear()
                    sleep(1.2)
                    decision=messagebox.askyesno("CONGRATULATION","WANNA PLAY MORE!!")
                    if decision==True:
                        self.destroy()
                        reset()
                    else:
                        self.destroy()
                    break

                elif user==letter[i]:
                    letter.remove(letter[i])
                    try:
                        self.clr(z)
                    except:
                        pass
                    z=canvas.create_text(510,180+15,text="YOU PRIDICTED A LETTER",fill=f"#1c404c",font=f"gabriola 30 bold")
                    print(letter)
                    blank_filling(i,user)
                    break
                else:
                    try:
                         self.clr(z)
                    except:
                        pass
                    z=canvas.create_text(510,180+15,text="You pridicted letter/word not match",fill=f"#1c404c",font=f"gabriola 30 bold")
                    continue
        butt=Button(canvas,text="PRIDICT",relief=RAISED,width=16,height=0,bg="#1c404c",font="gabriola 24 bold",foreground="#DE9E46",activebackground="#1c404c",justify=CENTER)
        butt.bind("<Button-1>",take)   
        butt.place(x=391,y=274+100)
        canvas.pack(fill=BOTH)
    
    def wordchosing(self):
        global fru
        global chances
        global letter
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