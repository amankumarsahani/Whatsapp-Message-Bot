import pyautogui as ag
import time
lst=[]

def data(t_msg=1):
    msg_no=int(input("TOTAL NUMBER OF YOU WANT TO SEND MESSAGE (eg:1,2,3...) : "))
    
    for i in range(t_msg):
        msg=input("ENTER MESSAGE YOU WANT TO SEND : \n")
        lst.append(msg)
    return msg_no,msg

def show_Loading_time():
    print("PLEASE WAIT DATA IS LOADING...")
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)
    print("PROCESSING...")

def message(Msg_no,Msg,lst,t_msg=1):
    n=0
    strt=time.time()
    while n<Msg_no:
        for j in range(t_msg):
            for txt in lst:
                time.sleep(0)
                ag.typewrite(txt)
                time.sleep(0.1)
                ag.press('enter')
                n+=1
    end=time.time()
    print("\nMESSAGE SENT....TASK COMPLETED!")
    print("\nTOTAL TIME TAKEN TO COMPLETE YOUR TASK : ",end-strt)

opt=int(input('''
        CHOOSE OPTION TO PERFORM TASK:
            1.WANT TO SEND SINGLE MESSAGE
            2.WANT TO SEND MULTIPLE MESSAGE
            3.EXIT
        '''))

if opt==1:
    msg_no,msg=data()
    print('\nNOTE - KINDLE OPEN WHATSAPP TO WHOME YOPU WANT TO SEND MESSAGE!!!\n')
    show_Loading_time()
    tm=message(msg_no,msg,lst)
    
     
elif opt==2:
    t_msg=int(input("ENTER TOTAL TYPES OF MESSAGES(eg:1,2,3...) : "))
    msg_no,msg=data(t_msg)
    print('\nNOTE - KINDLE OPEN WHATSAPP TO WHOM YOU WANT TO SEND MESSAGE!!!\n')
    show_Loading_time()
    tm=message(msg_no,msg,lst)

else:
    print(" THANKS FOR VISITING OUR PROGRAM....HAVE A GOOD DAY ")
