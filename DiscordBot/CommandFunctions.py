import sys
import random

def PrintLog(text):
    print(text)

#コマンドから指定された範囲でランダムな数字を返します。
#構文: !dice
#構文: !dice [min-max]
def c_dice(command):
    command = str(command)
    command = command.replace("!dice","")
    command = command.replace(" ","")
    if len(command) == 0:
        return str(random.randint(0,100))

    elif command.count(":") == 1:
        command = command.replace(":"," ")
        min = ""
        max = ""
        frag = False
        for s in command:
            if frag:
                max += s

            elif s == " ":
                frag = True

            else:
                min += s

        try:
            min = int(min)
            max = int(max)
            return str(random.randint(min,max))
            
        except ValueError:
            print("Error:ValueError_At c_dice")
            return None

        return str(random.randint(min,max))

