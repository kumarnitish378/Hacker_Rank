from time import sleep

def crypto():
    for i in range(5):
        print(".",end="")
        sleep(0.1)
    print("\nwelcome!")
    first_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', '.', ',', ' ']
    second_lower = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '//', ' ']
    first_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', '/', '.']
    second_upper = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '', '.']
    lower_spacial_char = ['←', '↑', '→', '↓', '™', '♦', '♥', '♣', '‰', '‡', '†', '§', '¢', '¤', '¥', '©', '«', '®', '¶',
                          '¼', '¾', '½', 'Æ', 'Ð', '¿', 'µ', '±', ' ', '.']
    upper_spacial_char = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '>', '+', '=', '{', '}', ']', '[',
                          '|', '`', ',', '.', '/', '?', '<', ' ', 'Ê']
    lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', ' ', '/', '.']
    upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '/']

    def encryption_first(new):
        output = ""
        try:
            for i in new:
                if i in second_lower or i in second_upper:
                    if i in second_lower:
                        output = output + first_lower[second_lower.index(i)]
                    else:
                        output = output + first_upper[second_upper.index(i)]

                else:
                    if i in first_lower:
                        output = output + second_lower[first_lower.index(i)]

                    else:
                        output = output + second_upper[first_upper.index(i)]
            fed = output
            output1 = ""
            for j in fed:
                if j in lower_case:
                    output1 = output1 + lower_spacial_char[lower_case.index(j)]
                else:
                    output1 = output1 + upper_spacial_char[upper_case.index(j)]
            return output1
        except:
            print("not in list\n"
                  "please enter only alphabates\n"
                  "do not enter any spacial character")

    def encryption_second(new):
        output = ""
        try:
            for i in new:
                if i in second_lower or i in second_upper:
                    if i in second_lower:
                        output = output + first_lower[second_lower.index(i)]
                    else:
                        output = output + first_upper[second_upper.index(i)]

                else:
                    if i in first_lower:
                        output = output + second_lower[first_lower.index(i)]

                    else:
                        output = output + second_upper[first_upper.index(i)]
            return output
        except:
            print("not in list\n"
                  "please enter only alphabates\n"
                  "do not enter any spacial character")

    def decryption(new):
        try:
            output = ""
            for i in new:
                if i in lower_spacial_char:
                    output = output + lower_case[lower_spacial_char.index(i)]
                else:
                    output = output + upper_case[upper_spacial_char.index(i)]
            return encryption_second(output)
        except:
            print("not in list")

    def banner():
        print('''
                   _*OOOOOO*_
                   OO      OO
                   OO      OO
                   OO      OO
                _*||||||||||||*_
                ||||||||||||||||
                ||||||||||||||||
                ||||||/  \||||||
                ||||||\__/||||||
                |||||||  |||||||
                |||||||  |||||||
                \||||||||||||||/''')

    while (True):
        banner()
        choise = input(''' Data Encryption and Decryption: 
        [1]. Encryption 
        [2]. Decryption
        chose any one >> ''')
        if choise == '1':
            Input = input("enter plain text >>> ")
            new = Input[::-1]
            print("Encrypted Data")
            print("======================================================================================")
            print(encryption_first(new))
            print("================================== THANKS ============================================")
            Next = input("You want to continue(Y/N)= ")
            if Next == "N" or Next == "n":
                exit("thank for using!")
            else:
                pass
        elif choise == '2':
            Input = input("enter Chipher text >>> ")
            new = Input[::-1]
            print("Decrypted Data")
            print("=====================================================================================")
            print(decryption(new))
            print("================================= THANKS ============================================")
            Next = input("Do You want to continue?(Y/N)= ")
            if Next == "N" or Next == "n":
                exit("Thank for using!"
                     " Have a nice day")
            else:
                pass
        elif choise == "banner":
            banner()
        else:
            print("Please chose correct option ")
            pass
password = input("enter password: ")
if password == "hello":
    crypto()
else:
    print("try again!")