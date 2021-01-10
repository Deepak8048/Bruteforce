import string
import pyautogui
import random

strings = string.ascii_letters + string.digits
strings = list(strings)

password = pyautogui.password(str('Enter a password to be bruteforced: '))

def Bruteforce(password):
    bruteforced_pass=''
    while(bruteforced_pass!=password):
        bruteforced_pass = random.choices(strings, k=len(password))
        print('<{=========='+str(bruteforced_pass)+'==========}>')
        if (bruteforced_pass==list(password)):
            print('Your password is: ', ''.join(l for l in bruteforced_pass))
            break

Bruteforce(password=password)
