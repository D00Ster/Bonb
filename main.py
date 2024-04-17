import keyboard

# sketch of winconditions
solution_1 = ['s', 'down', 'space', 'down', 's', 'space'] #ladder
solution_2 = ['right', 'left', 'right', 'up', 'red'] #svetofor

made = 0

# gameplay loop

g1 = -1
g2 = -1
buff = []
wbuff = 0
gbuff = 0
cur = 0
curgame = -1
last = 0
lenn = 0
outputs = []

while True:
    a = keyboard.read_key()
    #print(a)
    if made != 2 and a == 'w':
        print("YOU BLEW UP!!!")
        exit(0)
    elif a == 'w':
        wbuff += 1
        if wbuff > 20:
            print("YOU BLEW UP!!!")
            exit(0)
        continue
    elif a == 'g':
        gbuff += 1
        if gbuff > 3 and wbuff != 0 and made == 2:
            print("SUCCSESS!")
        continue
    #print(a)
    buff.append(a)
    lenn += 1
    #while len(buff) > 2:
    #    buff.pop(0)
    if cur == 0 and 's' in buff and curgame == -1 and g1 == -1:
        curgame = 1
        cur += 1
        print("BIP")
        buff.clear()
        continue
    elif 'right' in buff and curgame == -1 and g2 == -1:
        curgame = 2
        cur += 1
        print("BIP")
        buff.clear()
        #print("!!")
        continue
    else:
        outputs.append("BIP BIP")
    if cur > 0:
        for i in buff:
            if i == solution_1[cur] and curgame == 1:
                print("BIP")
                outputs.clear()
                cur += 1
                buff.clear()
            elif curgame == 2 and i == solution_2[cur]:
                print("BIP")
                outputs.clear()
                cur += 1
                buff.clear()
                #print("!!")
            else:
                outputs.append("BIP BIP")
    #print(cur)
    if curgame == 1 and cur == 6:
        print("BIP BIP BIP")
        made += 1
        g1 = 1
        cur = 0
        curgame = -1
        outputs.clear()
    elif curgame == 2 and cur == 4:
        print("BIP BIP BIP")
        made += 1
        g2 = 1
        cur = 0
        curgame = -1
        outputs.clear()
    elif made != 2 and lenn >= 7:
        print("BIP BIP")
        outputs.clear()

    #print("last = ", last)


# make two counters and say gg if players win

print("GG")

# add counter with graphics next time