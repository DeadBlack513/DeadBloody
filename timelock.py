while True: 
    # -*- coding:utf -8 -*-
    from colorama import init
    import colorama
    from colorama import Fore, Back
    from termcolor import colored
    import socket
    import random
    import stun
    import threading
    import requests
    import urllib.request
    import re

    res = urllib.request.urlopen('https://2ip.ru').read()

    pas = random.randint(11111111, 99999999)

    xfx = ["[+] -- Osx_Os", "[+] -- Hacked_Blood", "[+] -- Black_Die", "[+] -- Dark_Inside", "[+] -- Dead_Boy", "[+] -- Vnuchock228", "[+] -- Haera_Galak", "[+] -- Ip_Up", "[+] -- Angelok", "[+] -- Dinospike", "[+] -- Low_priority", "Faraon_Ega", "Week_of_year", "[+] -- LadoBill"]


    def fanc1():
        color_a = colored("[+] ", 'green')
        print("~"*50)
        host = input(wat + "Host --> " + start)
        port = int(input(wat + "Port --> "))
        print("~"*50)

        scan = socket.socket()

        color_b = colored("[!] ", 'red')
        color_c = colored("[!] ", 'green')

        try:
            scan.connect((host, port))
        except socket.error:
            print(color_b + wat + "Port -- ", port, " -- [CLOSED]" + start + "|")
        else:
            print(color_c + wat + "Port -- ", port, " -- [OPENED]" + color_c + "|")

    def fanc2():
        color_a = colored("[+] ", 'yellow')
        color_b = colored("[!] ", 'red')
        color_c = colored("[!] ", 'green')

        host = input(color_b + wat + "[Host --> " + start)
        print("\n")
        port = [0, 1, 2, 3, 5, 7, 9, 11, 13, 17, 18, 19, 20, 21, 22, 23, 24,25, 26, 27, 29, 31, 33, 35, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 280, 282, 283, 284, 285, 286, 287, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 330, 333, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420]

        for i in port:
            try:
                scan = socket.socket()
                scan.settimeout(0.5)
                scan.connect((host, i))
            except socket.error:
                print(color_b + wat + "Port -- ", i, " -- [CLOSED]" + start + "|")
            else:
                print(color_c + wat + "Port -- ", i, " -- [OPENED]" + color_c + "|")
    wat = "\033[1;37m"
    start = "\033[1;31m"
    print(start + "_"*60, "\n")
    print(" ███████████████████████████████████████████████████████")
    print(" █▄─▄▄▀█▄─▄▄─██▀▄─██▄─▄▄▀███▄─▄─▀█▄─▄███─▄▄─█─▄▄─█▄─▄▄▀█")
    print(" ██─██─██─▄█▀██─▀─███─██─████─▄─▀██─██▀█─██─█─██─██─██─█")
    print(" ▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀")
    print("_"*60, "\n")

    print(wat + "----Author: Magomed Urdashev -------------------------------\n----Created In: Python -------------------------------------")
    print(start + "_"*60)
    print("\n")
    print(wat + "----[1] --- Scan A Single Port")
    print(wat + "----[2] --- Scan The List Of Ports")

    print(start + "_"*60, "\n", '-'*59, "\n")
    text_a = input(wat + "[CHOICE]--> ")

    if text_a == "1":
        fanc1()
    elif text_a == "2":
        fanc2()