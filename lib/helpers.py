import sys
import time
from prettycli import red, green, yellow
from simple_term_menu import TerminalMenu


def app_start_termical():
    options = ["Sign Up", "Login", "Exit"]
    terminal_menu = TerminalMenu(options)
    selection = terminal_menu.show()

    # if selection == 0:
    #     sign_up()
    # elif selection == 1:
    #     handle_login()
    # else:
    #     exit_app()


def clear_screen(lines):
    print("\n" * lines)


def exit_app():
    print("Exiting from app. Thanks for using Contact Storage App. ")
    print(
        yellow(
            """

    ____                  ____                  _  _  _ 
   | __ )  _   _   ___   | __ )  _   _   ___   | || || |
   |  _ \ | | | | / _ \  |  _ \ | | | | / _ \  | || || |
   | |_) || |_| ||  __/  | |_) || |_| ||  __/  |_||_||_|
   |____/  \__, | \___|  |____/  \__, | \___|  (_)(_)(_)
           |___/                 |___/                  

"""
        )
    )
    time.sleep(2)
    sys.exit()


def welcome_banner():
    print(
        green(
            """

   __        __     _                                                                                              
   \ \      / /___ | |  ___  ___   _ __ ___    ___                                                                 
    \ \ /\ / // _ \| | / __|/ _ \ | '_ ` _ \  / _ \                                                                
     \ V  V /|  __/| || (__| (_) || | | | | ||  __/                                                                
    _ \_/\_/  \___||_| \___|\___/ |_| |_| |_| \___|                                                                
   | |_  ___                                                                                                       
   | __|/ _ \                                                                                                      
   | |_| (_) |                                                                                                     
    \__|\___/                                                                                                      
     ____               _                _      ____   _                                        _                  
    / ___| ___   _ __  | |_  __ _   ___ | |_   / ___| | |_  ___   _ __  __ _   __ _   ___      / \    _ __   _ __  
   | |    / _ \ | '_ \ | __|/ _` | / __|| __|  \___ \ | __|/ _ \ | '__|/ _` | / _` | / _ \    / _ \  | '_ \ | '_ \ 
   | |___| (_) || | | || |_| (_| || (__ | |_    ___) || |_| (_) || |  | (_| || (_| ||  __/   / ___ \ | |_) || |_) |
    \____|\___/ |_| |_| \__|\__,_| \___| \__|  |____/  \__|\___/ |_|   \__,_| \__, | \___|  /_/   \_\| .__/ | .__/ 
                                                                              |___/                  |_|    |_|    

"""
        )
    )
