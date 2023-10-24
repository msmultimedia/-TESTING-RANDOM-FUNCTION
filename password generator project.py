from tkinter import*
import random
root=Tk()
root.title("password generator")
root.geometry("500x500")
label=Label(root)
entry=Entry(root)
entry.place(relx=0.5,rely=0.3,anchor=CENTER)
label2=Label(root)
label2.place(relx=0.5,rely=0.4,anchor=CENTER)

array_3d=[[["&","#","@","!"],["king","queen"],["a","b","c","d"]]]
print(array_3d[0][2][3])
def new_password():
    random_no_1=random.randint(0,3)
    random_no_2=random.randint(0,1)
    random_no_3=random.randint(0,3)
    letter1=str(array_3d[0][0][random_no_1])
    letter2=(array_3d[0][1][random_no_2])
    letter3=(array_3d[0][2][random_no_3])
    label["text"]=letter1 + ""  +   letter2 + ""  + letter3 +  ""  
    label2["text"]="guessed password:"+ entry.get()
    
    

btn=Button(root,text="new password",command=new_password)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()