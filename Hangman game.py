import random
from tkinter import *
from tkinter import ttk

class gui(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.maxsize(width=1000,height=600)
        self.minsize(width=1000,height=600)
        self.config(background="#DE9E46")

    def CANVAS(self,X_cord,Y_cord,text,s):
        global w
        global canvas
        canvas=Canvas(background="#DE9E46",height=900)
        l=[]
        p=0
        d=int(len(w)/2)
        #logic to keep word in middle of window
        para=len(w)/2
        sub=para*64
        print(para)
        st=540-sub
        for i in range(len(w)):
            l.append("_")
            canvas.create_text(st+p,100,text=l[i],fill="#1c404c",font=('typewriter 50 bold'))
            p+=64
        content=canvas.create_text(510,50,text="HANGMAN GAME",fill="#1c404c",font="gabriola 40 bold")
        content=canvas.create_text(830,20,text="CHANCES LEFT : ",fill="#1c404c",font="gabriola 33")
        content=canvas.create_text(510,185,text="ENTER YOUR PRIDICTION ",fill="#1c404c",font="gabriola 33 bold")
        canvas.create_text(X_cord,Y_cord,text=text,fill=f"#1c404c",font=f"typewriter {s} bold")
        canvas.pack(fill=BOTH)
        

    
    def wordchosing(self):
        global fru
        global w
        global chances
        fru=["apple","mango","cherry","peach","kiwi","grape",'orange','strawberry']
        w=random.choice(fru)
        chances=len(w)+4
        print(w,chances)
        self.CANVAS(972,20,f"{chances}",27)

    def logic(self):
        global user
        inco=Entry(canvas,width=25,highlightcolor="#1c404c",font=("gabriola",15),highlightthickness=4,background="#DE9E46",highlightbackground="#1c404c",relief=RAISED)
        inco.place(x=346,y=221)
        def take(self):
            user=inco.get()
            print(user,chances)
            inco.delete(0,END)
            
        butt=Button(canvas,text="PRIDICT",relief=RAISED,width=17,height=0,bg="#1c404c",font="gabriola 11 bold",foreground="#DE9E46",activebackground="#1c404c",justify=CENTER)

        # canvas.create_rectangle(458,260,555,333,outline="#1c404c",width=8)
        butt.bind("<Button-1>",take)   
        butt.place(x=558,y=220)
        #limiting input to one letter
        # while True:
        #     if len(user)==1 :
        #         break
        #     else:
        #         print("Please enter a single letter")
        #         break
        
        #matching letter
        # for i in range(len(w)):
        #     if user==frul[i]:
        #         frul.remove(frul[i])
        #         print(f"""YOU PREDICTED A RIGHT LETTER
        #         chances left:- {left}""")
                
        #         return i
        
        # return f"""You pridicted letter not match
        #         chances  left:- {left}"""

if __name__=="__main__":
    root=gui()
#creating words that to be pridicted
root.wordchosing()
root.logic()
root.mainloop()




# backup_frul=w
# number_of_letter=len(frul)

# #no. of chances
# chances=len(frul)
# print(f"You can pridict {chances} letter")

# #display
# dis=[]
# for i in range(len(frul)):
#     dis.append("_")

# repeated_index=[]
# def counter():
#     global repeated_letter
#     for i in range(len(frul)):
        
#         v=frul.count(frul[i])
#         if v>1:
#             for u in range(len(frul)):
#                 if frul[i]==frul[u]:
#                     repeated_index.append(u)
#             print(f"list of index repeated {repeated_index}")
#             # index=[]
#             # index.append(i)
#             # # print(index)
#             print(f"no. of time {frul[i]} repeated {v}")
#             return frul[i]
#             # return frul[i]

            
# repeated_letter=counter()
# print (repeated_letter)



# #logic to match input and letter of th word

# #loop to take input no. of time as that of no. of letter or to check for win or lose
# for i in range(chances):
#     # chances left counter
#     left=(chances-1)-i
#     p=match(left)
    
#     for i in range(len(backup_frul)):
#         # dis[i]=user
        
#         if backup_frul[i]==user:
#            dis[i]=user
#            x="".join(dis)
#            print(x)
#            break
#         if user==repeated_letter:
#             for index in repeated_index:
#                 dis[index]=user
#                 # dis.pop(index)
#                 repeated_index.remove(repeated_index[0])
#                 break

    
#     #checking win or lose
#     if frul==[]:
#             print("CONGRATULATION!! you won")
#             break
#     elif chances==0:
#             print(f"SORRY!! Better luck next time")
#             break
#     elif user=='quit':
#         break

#     #display
            
    
