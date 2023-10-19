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
        global inco
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
        def blanks(i,user):
            l[i]=str(user)
            underscore=canvas.create_text(index_loc[i],100+10,text=l[i].upper(),fill="#1c404c",font=('typewriter 40 bold'))
            index_loc.remove(index_loc[i])
            # underscore.itemconfig(text=l[i])

        canvas.create_text(X_cord,Y_cord,text=text,fill=f"#1c404c",font=f"typewriter {s} bold")
        canvas.create_text(510,50,text="HANGMAN GAME",fill="#1c404c",font="gabriola 40 bold")
        canvas.create_text(830,20,text="CHANCES LEFT : ",fill="#1c404c",font="gabriola 33")
        canvas.create_text(510,185+100,text="ENTER YOUR PRIDICTION ",fill="#1c404c",font="gabriola 40 bold")
        inco=Entry(canvas,width=25,highlightcolor="#1c404c",font=("gabriola",17),highlightthickness=4,background="#DE9E46",highlightbackground="#1c404c",relief=RAISED)
        inco.place(x=390,y=221+100)
        def take(event):
            global z
            
            user=inco.get()
            # user.lower()
            inco.delete(0,END) 
            def clr(i):
                # global z
                try:
                    canvas.delete(i)    
                except:
                    pass
            for i in range(len(letter)):
                if user==letter[i]:
                    letter.remove(letter[i])
                    try:
                        clr(z)
                    except:
                        pass
                    z=canvas.create_text(510,180+15,text="YOU PRIDICTED A LETTER",fill=f"#1c404c",font=f"gabriola 30 bold")
                    print(letter)
                    blanks(i,user)
                    break
                elif user==w:
                    letter.clear()
                    try:
                        clr(z)
                    except:
                        pass
                    z=canvas.create_text(510,180+15,text="YOU PRIDICTED ENTIRE WORD",fill=f"#1c404c",font=f"gabriola 30 bold")
                    print(letter)
                    break

                else:
                    try:
                         clr(z)
                    except:
                        pass
                    z=canvas.create_text(510,180+15,text="You pridicted letter/word not match",fill=f"#1c404c",font=f"gabriola 30 bold")
                    # break
                    continue
        
            # self.CANVAS(user)
        butt=Button(canvas,text="PRIDICT",relief=RAISED,width=16,height=0,bg="#1c404c",font="gabriola 24 bold",foreground="#DE9E46",activebackground="#1c404c",justify=CENTER)
        butt.bind("<Button-1>",take)   
        butt.place(x=391,y=274+100)
        canvas.pack(fill=BOTH)
        

    
    def wordchosing(self):
        global fru
        global w
        global chances
        global letter
        fru=["apple","mango","cherry","peach","kiwi","grape",'orange','strawberry']
        w=random.choice(fru)
        chances=len(w)+4
        print(w,chances)
        letter=list(w)
        self.CANVAS(972,20,f"{chances}",27)




    def input(self):

        global inco
        global user
        #     if len(user)==1 :
        #         break
        #     else:
        #         print("Please enter a single letter")
        #         break
        
        #matching letter
        
        # return f
if __name__=="__main__":
    root=gui()
#creating words that to be pridicted
root.wordchosing()
# print(root.take())
root.input()
# def logic(user):
    # fting input to one
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



# #input to match input and letter of th word

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
            
    
