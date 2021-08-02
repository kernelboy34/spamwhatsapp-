import pyautogui
import webbrowser as web
import time

print("""        ___====-_  _-====___
           _--^^^#####//      \\#####^^^--_
        _-^##########// (    ) \\##########^-_
       -############//  |\^^/|  \\############-
     _/############//   (@::@)   \\############\_
    /#############((     \\//     ))#############\
   -###############\\    (oo)    //###############-
  -#################\\  / VV \  //#################-
 -###################\\/      \//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)                             """)
print("un programa secillo de spam para whatsapp  hecho por kernelboy34")

like=input("escribe el numero:   ")
ees=input("escribe el mensaje que quiere enviar:  ")
web.open('https://web.whatsapp.com/send?phone='+like)
time.sleep(8)

for i in range(150):
    pyautogui.write(ees)
    pyautogui.press('enter')
    print((ees)+str(i+1)+' enviado')
    pass
pyautogui.alert('Bomba de mensajes finalizada')