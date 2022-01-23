import tkinter as r
import tkinter.font as tkfont
def pro():
    page=r.Tk()
    page.title("EGG CATCHER GAME")
    page.configure(bg='deep sky blue')
    page.geometry('800x400')

    labelsty=tkfont.Font(family="Lucida Grande",size=10)
    labelsty.configure(size=50)

    l=r.Label(page,text="EGG CATCHER GAME",font=labelsty)
    l.pack(side='top')
    l.place()
    l.configure(bg='sea green')

    buttonsty=tkfont.Font(family="Lucida Grande",size=2)
    buttonsty.configure(size=20)

    def start():
        page.destroy()
        import narsa
          
    def inst():
        pass
        import instructions
    f=open("Score.txt","r")
    score=f.read()
    f.close()
    def reset():
        f= open("Score.txt","r+")
        f.truncate(0)
        f.write("0")
        f.close()
        page.destroy()
        pro()
    
    
    l1=r.Label(page,text="Highest score : "+score,font=buttonsty)
    l1.place(x=260,y=180)
    l1.configure(bg='deep sky blue')
    b1=r.Button(page,text="Start the game",command=start,font=buttonsty)
    b1.place(x=275,y=220)
    b1.configure(bg='light pink')
    b2=r.Button(page,text="Instructions",command=inst,font=buttonsty)
    b2.place(x=293,y=280)
    b2.configure(bg='light pink')
    b3=r.Button(page,text="RESET",command=reset,font=buttonsty)
    b3.place(x=350,y=350)
    b3.configure(bg='light pink')

    page.mainloop()
pro()
