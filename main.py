import getpass
import pyautogui, time, threading, ctypes, schedule

shutdown_event = threading.Event()
ctypes.windll.kernel32.SetConsoleTitleW("SpaceCrypto-BotV1 by.firstngub")
print("============================================")
print("Not allowed to use for sale and redistribution from owner.")
print("Donate: 087-389088-6 Kbank | Thank you. :)")
print("============================================")
print("1. Please enter your Metamask password.!")
User_Password = getpass.getpass("Password: ")
print("2. Please enter your Return to Lobby time (minutes)!!")
Return_times = int(input("Return Time: "))
print("============================================")

for i in range(3, 0, -1):
    print("=> [INFO]Bot-Starting: ", i)
    time.sleep(1)
print("=> [INFO]Complete Loading!")
print("============================================")
time.sleep(3)



def Lobby_ReturnFunc():
        Lobby_Return = pyautogui.locateOnScreen('images/Lobby_return.png')
        if Lobby_Return == None:
            return
        elif Lobby_Return != None:
            pyautogui.moveTo(Lobby_Return)
            pyautogui.leftClick()
            print("=> [SC][INFO] : Return to Lobby")
            print("============================================")
            time.sleep(5)
            
        else:
            return

schedule.every(Return_times).minutes.do(Lobby_ReturnFunc)


def is_onready():

    #BOMB CONNECT
    def Bomb_connectFunc():
        Bomb_connect = pyautogui.locateOnScreen('images/Bomb_connect.png')

        if Bomb_connect == None:
            return
        elif Bomb_connect != None:
            pyautogui.moveTo(Bomb_connect)
            pyautogui.leftClick()
            print("=> [BC][INFO]BombCrypto Connecting..!")
            time.sleep(2)
        else:
            return

    
    def Metamask_Password_Unlock():
        Password_Unlock = pyautogui.locateOnScreen('images/Password_Unlock.png')
        Password_Unlock_TH = pyautogui.locateOnScreen('images/Password_Unlock_TH.png')
        print("=> [INFO]Entering Password...")
        pyautogui.write(User_Password, interval= 0.15)

        if Password_Unlock != None:
            time.sleep(0.5)
            pyautogui.moveTo(Password_Unlock)
            pyautogui.leftClick()

        elif Password_Unlock == None:
            return

        elif Password_Unlock_TH != None:
            time.sleep(0.5)
            pyautogui.moveTo(Password_Unlock_TH)
            pyautogui.leftClick() 

        elif Password_Unlock_TH == None:
            return
        
        else:
            return

    def Metamask_Password_Check():
        Password_1_Check = pyautogui.locateOnScreen('images/Password.png')
        Password_Unlock_Check = pyautogui.locateOnScreen('images/Password_Unlock.png')
        Password_Unlock_TH_Check = pyautogui.locateOnScreen('images/Password_Unlock_TH.png')

        if Password_1_Check == None:
            if Password_Unlock_Check != None:
                pyautogui.moveTo(Password_Unlock_Check)
                pyautogui.leftClick()
            elif Password_Unlock_Check == None:
                return
            elif Password_Unlock_TH_Check != None:
                pyautogui.moveTo(Password_Unlock_TH_Check)
                pyautogui.leftClick()
            elif Password_Unlock_TH_Check == None:
                return
            else:
                return
        elif Password_1_Check != None:
            pyautogui.moveTo(Password_1_Check)
            pyautogui.leftClick()

            Metamask_Password_Unlock()
        else:
            return

    def Metamask():
        Connect_Wallet = pyautogui.locateOnScreen('images/Connect_wallet.png')
        if Connect_Wallet != None:
            time.sleep(0.5)
            pyautogui.moveTo(Connect_Wallet)
            pyautogui.leftClick()
            print("=> [SC]Starting Connect (Metamask) !!")
        elif Connect_Wallet == None:
            return
        else:
            return

    def Metamask_Check():
        Connect_Wallet_Check = pyautogui.locateOnScreen('images/Connect_wallet.png')
        if Connect_Wallet_Check != None:
            
            Metamask() #callback

        elif Connect_Wallet_Check == None:
            return
        else:
            return

    def Metamask_Notification():
        Sign_eng_button = pyautogui.locateOnScreen('images/Sign_eng.png')
        Sign_th_button = pyautogui.locateOnScreen('images/Sign_th.png')
        if Sign_eng_button != None:
            time.sleep(0.5)
            pyautogui.moveTo(Sign_eng_button)
            pyautogui.leftClick()
            print("=> [INFO]Metamask Logged in !!")
        elif Sign_eng_button == None:
            return
        elif Sign_th_button != None:
            time.sleep(0.5)
            pyautogui.moveTo(Sign_th_button)
            pyautogui.leftClick()
            print("=> [INFO]Metamask Logged in !!")
        elif Sign_th_button == None:
            return
        else:
            return

    def _Play_SpaceCryptoFunc():
        Play_SpaceCrypto = pyautogui.locateOnScreen('images/Play_SpaceCrypto.png', confidence=0.6)
        if Play_SpaceCrypto != None:
            print("=> [SC]Starting SpaceCrypto...")
            time.sleep(0.5)
            pyautogui.moveTo(Play_SpaceCrypto)
            pyautogui.leftClick()
        elif Play_SpaceCrypto == None:
            return
        else:
            return

    def Spaceship_fightbossFunc():
        Fight_Boss_Button = pyautogui.locateOnScreen('images/Fight_Boss_Button.png')

        if Fight_Boss_Button != None:
            pyautogui.moveTo(Fight_Boss_Button)
            pyautogui.leftClick()
            print("=> [SC][INFO] : Fighting Boss...")

        elif Fight_Boss_Button == None:
            return
        else:
            return

    def Spaceship_sendFunc():
        Red_fight_Button = pyautogui.locateOnScreen('images/Red_fight_Button.png')
        
        while True:
            if Red_fight_Button == None:
                return
            elif Red_fight_Button != None:
                print("=> [SC][INFO] : Sending Spaceship..")
                pyautogui.moveTo(Red_fight_Button)
                pyautogui.leftClick()
                return Spaceship_sendFunc()
            else:
                return

    def Spaceship_Check():
        Full_team = pyautogui.locateOnScreen('images/Full_team.png')

        if Full_team == None:
            
            Spaceship_sendFunc()

        elif Full_team != None:
            
            Spaceship_fightbossFunc()

        else:
            return

    def is_VictoryFunc():
        Victory_popup = pyautogui.locateOnScreen('images/Victory_popup.png')
        Victory_Confirm = pyautogui.locateOnScreen('images/Victory_confirm.png')

        if Victory_popup == None:
            return
        elif Victory_popup != None:
            
            if Victory_Confirm != None:

                pyautogui.moveTo(Victory_Confirm)
                pyautogui.leftClick()
                print("=> [SC][INFO] : Victory")
                time.sleep(2)

            elif Victory_Confirm == None:
                return
            else:
                return
        else:
            return

    def is_DefeatFunc():
        Defeat_popup = pyautogui.locateOnScreen('images/Defeat_popup.png')
        Defeat_Confirm = pyautogui.locateOnScreen('images/Defeat_confirm.png')

        if Defeat_popup == None:
            return
        elif Defeat_popup != None:
            
            if Defeat_Confirm != None:

                pyautogui.moveTo(Defeat_Confirm)
                pyautogui.leftClick()
                print("=> [SC][INFO] : Defeat")
                time.sleep(2)

            elif Defeat_Confirm == None:
                return
            else:
                return
        else:
            return
    
    def LoginFailed_Func():
        Login_Failed_popup = pyautogui.locateOnScreen('images/Login_Failed_popup.png', confidence=0.7)
        OK_Button = pyautogui.locateOnScreen('images/OK_Button.png', confidence=0.7)

        if Login_Failed_popup == None:
            return

        elif Login_Failed_popup != None:
            time.sleep(0.5)
            print("=> [SC][WARNING]: Login Failed")

            if OK_Button != None:
                pyautogui.moveTo(OK_Button)
                pyautogui.leftClick()
            
            elif OK_Button == None:
                return
            else:
                return
        else:
            return
    
    def Error_ExceptionFunc():
        Error_popup = pyautogui.locateOnScreen('images/Error_popup.png', confidence=0.7)
        Close_Button = pyautogui.locateOnScreen('images/Close_Button.png', confidence= 0.7)

        if Error_popup == None:
            return

        elif Error_popup != None:
            time.sleep(0.5)
            print("=> [SC][WARNING]: Error Exception")

            if Close_Button != None:
                pyautogui.moveTo(Close_Button)
                pyautogui.leftClick()
                time.sleep(5)
                pyautogui.keyDown('ctrl')
                pyautogui.press('f5')
                pyautogui.keyUp('ctrl')
                print("=> [SC][INFO] : Refreshing...")

                return
            elif Close_Button == None:
                return
            else:
                return
        else:
            return


    def main():
        #============= 
        #Start Func
        #=============

        #special func
        Bomb_connectFunc()
        #/////////#

        Metamask_Check() #1
        
        Metamask_Password_Check() #2

        Metamask_Notification() #3
        
        _Play_SpaceCryptoFunc() #4 Start
        
        Spaceship_Check() #5 Spaceship check for sending and fight boss
        
        is_VictoryFunc() #Victory Check
        
        is_DefeatFunc() #Defeat Check

        LoginFailed_Func() # Check Login Failed
        
        Error_ExceptionFunc() # Error Exception Check
        
        schedule.run_pending()


    if __name__ == "__main__":
        main()

def updateTimeFunc():
    while not shutdown_event.is_set():
        statustrade = 1
        if statustrade == 1:
            is_onready()

#---- timer
updateTime = threading.Timer(0.5,updateTimeFunc)
updateTime.start() # t.cancel()
#-------------