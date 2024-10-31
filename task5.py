#!python3

def main():
    invatory = {}
    action = ''
    while '\'end' not in action:
        action = "\'" + input("get iteam or drop iteam: ")
        if '\'end' in action:
            break
        elif '\'get' in action:
            action = action.replace("\'get ", "")
            action = action.split(" ")
            iteam = ''
            a = 1
            for i in action:
                if i.isdigit():
                    a = int(i)
                else:
                    iteam = iteam + f' {i}'
            if iteam[0] == ' ':
                iteam = iteam.replace(' ','',1)
            if iteam in invatory:
                invatory[iteam] = invatory[iteam] + a
            else:
                invatory[iteam] = a
        elif '\'drop' in action:
            action = action.replace("\'drop ", "")
            action = action.split(" ")
            iteam = ''
            a = 1
            for i in action:
                if i.isdigit():
                    a = int(i)
                else:
                    iteam = iteam + f' {i}'
            if iteam[0] == ' ':
                iteam = iteam.replace(' ','',1)
            if iteam in invatory:
                if invatory[iteam] == a:
                    invatory.pop(iteam)
                elif invatory[iteam] < a:
                    print(f"You only have {invatory[iteam]} in your invatory, cant remove {a} {iteam}.")
                else:
                    invatory[iteam] = invatory[iteam] - a
            else:
                print(f"{iteam} not in your invatory")            
        elif '\'show invatory' in action:
            print(invatory)
            for i in invatory:
                tableLingth = 7 + len(i) + len(str(invatory[i]))
                print(tableLingth)
        else:
            print("Not valid acction")
            if input("End code? ") == 'yes':
                action = '\'end'
                break
        print(invatory)

if __name__ == '__main__':
    main()