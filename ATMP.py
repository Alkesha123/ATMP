from cgitb import text
from  tkinter import *


root= Tk()
root.geometry('1000x800')
root.resizable(0,0)
root.config(bg="#780d4f")


def frame1():
    balance2 = 5000
    
    def mainframe():
        submit.destroy()
        label.destroy()
        enter_pin.destroy()
        pin_input.destroy()


        def withdraw():
            label2.destroy()
            withdraw_btn.destroy()
            diposite_btn.destroy()
            balance_btn.destroy()
            exit_btn.destroy()
            enter_amount = Label(root, text="Enter Withdrawl Amount", font=("vardana", 25), bg="#000000",fg='white')
            enter_amount.place(x=330, y=200)
            amount = Entry(width=20,border=3,font=("vardana", 25))
            amount.place(x=310, y=280,height=30)
            

            def msg_withdraw():
                global acct
                amt =float (amount.get())
                acct = balance2-amt

                enter_amount.destroy()
                amount.destroy()
                sub.destroy()

                msg = Label(root, text=f"Money debited from your account successfully  {amt}", font=("vardana", 15),bg="#780d4f")
                msg.place(x=220, y=200)

                def exit():
                    msg.destroy()
                    exit.destroy()
                    main.destroy()
                    thank = Label(root, text="Thank You", font=("vardana", 35, 'bold'), bg="#000000",fg='white')
                    thank.place(x=400, y=300)

                exit = Button(root, text='Exit', font=("vardana", 15),border=10,command=exit)
                exit.place(x=580, y=350)

                def again_mainframe():
                    msg.destroy()
                    exit.destroy()
                    main.destroy()
                    mainframe()
                main = Button(root, text='Main Menu', font=("vardana", 15),border=10,command=again_mainframe)
                main.place(x=280, y=350)

            sub = Button(root, text='OK', font=("vardana", 15),border=10, activebackground='red',command=msg_withdraw)
            sub.place(x=450, y=350)


        def deposite():
            label2.destroy()
            withdraw_btn.destroy()
            diposite_btn.destroy()
            balance_btn.destroy()
            exit_btn.destroy()
            enter = Label(root, text="Enter Deposite Amount", font=("vardana", 25), bg="#000000",fg='white')
            enter.place(x=330, y=200)
            amount = Entry(width=20,border=3,font=("vardana", 25))
            amount.place(x=310, y=280,height=30)
            
            def msg_deposite():
                global acct
                b = float(amount.get())
                acct = balance2 + b

                enter.destroy()
                amount.destroy()
                ok.destroy()


                msg2 = Label(root, text=f"Money credited to your account successfully {b}", font=("vardana", 20), bg="#780d4f")
                msg2.place(x=220, y=200)

                def exit2():
                    msg2.destroy()
                    exit2.destroy()
                    main2.destroy()

                    thank = Label(root, text="Thank You", font=("vardana", 35, 'bold'), bg="#000000",fg='white')
                    thank.place(x=400, y=300)



                exit2 = Button(root, text='Exit', font=("vardana", 15),border=10,command=exit2)
                exit2.place(x=580, y=350)

                def again_mainframe2():
                    msg2.destroy()
                    exit2.destroy()
                    main2.destroy()
                    mainframe()
                main2 = Button(root, text='Main Menu', font=("vardana", 15),border=10, command=again_mainframe2)
                main2.place(x=280, y=350)

            ok = Button(root, text='OK', font=("vardana", 15),border=10, activebackground='red',command=msg_deposite)
            ok.place(x=450, y=350)

    
        def balance():
            acct = balance2
            label2.destroy()
            withdraw_btn.destroy()
            diposite_btn.destroy()
            balance_btn.destroy()
            exit_btn.destroy()
            balance = Label(root, text=f"Your current balance is  {acct}", font=("vardana", 25), bg="#780d4f")
            balance.place(x=250, y=200)

            def exit3():
                balance.destroy()
                exit.destroy()
                menu.destroy()
                thank = Label(root, text="Thank You", font=("vardana", 35, 'bold'), bg="#000000",fg='white')
                thank.place(x=400, y=300)

            exit = Button(root, text='Exit', font=("vardana", 15),border=10,command=exit3)
            exit.place(x=550, y=350)

            def agin_mainframe3():
                balance.destroy()
                exit.destroy()
                menu.destroy()
                mainframe()

            menu = Button(root, text='Main Menu', font=("vardana", 15),border=10,command=agin_mainframe3)
            menu.place(x=250, y=350)

        def exit():
            label2.destroy()
            withdraw_btn.destroy()
            diposite_btn.destroy()
            balance_btn.destroy()
            exit_btn.destroy()
            thank=Label(root,text="Thank You",font=("vardana", 35,'bold'),bg="#000000",fg='white')
            thank.place(x=400,y=300)



        label2 = Label(root, text="Welcome to ATM", font=("vardana", 30), bg="#000000",fg="white")
        label2.place(x=320, y=100)
        withdraw_btn = Button(root, text="Withdral", font=("vardana", 25),border=10, activebackground="red",command=withdraw)
        withdraw_btn.place(x=180, y=230)
        diposite_btn = Button(root, text="Deposite", font=("vardana", 25),border=10, activebackground="red",command=deposite)
        diposite_btn.place(x=550, y=230)
        balance_btn = Button(root, text="Balance", font=("vardana", 25),border=10, activebackground="red",command=balance)
        balance_btn.place(x=180, y=410)
        exit_btn = Button(root, text="Exit", font=("vardana", 25),border=10, activebackground="red",command=exit)
        exit_btn.place(x=550, y=410)

    def main():
        label.destroy()
        enter_pin.destroy()
        pin_input.destroy()
        submit.destroy()
        l = Label(root,text='Enter valid pin',bg="#000000",fg='white',font=("vardana", 30))
        l.place(x=400,y=300)
    def pin_submit():
        a = str(pin_input.get())
        if a == '2558':
            mainframe()
        else:
            main()
    label = Label(root, text="Welcome to ATM", font=("vardana", 25))
    label.place(x=350, y=200)
    enter_pin = Label(root, text="Enter Your Pin", font=("vardana", 20,))
    enter_pin.place(x=370, y=270)
    
    pin_input = Entry(width=15,show='*',border=5,font=("vardana", 25,))
    pin_input.place(x=340, y=350,height=30)

    submit = Button(root, text='Submit', font=("vardana", 15),border=10, command=pin_submit, activebackground='green')
    submit.place(x=430, y=450)


frame1()

root.mainloop()