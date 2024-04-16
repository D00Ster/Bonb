import keyboard

# sketch of winconditions
solution_1 = ['w', 'a', 's', 'd']
solution_2 = ['space']
temp = 1

# gameplay loop


while True:
    a = keyboard.read_key()
    print(a)
    if a == solution_1[temp] and temp < len(solution_1) - 1:
        temp += 1
        print(str(temp) + " is correct")
        # make sure to fix, no wincondition if as of now
    if a == solution_2[0]:
        print("wp")
        # else:
        pass

# make two counters and say gg if players win

print("GG")

# add counter with graphics next time
