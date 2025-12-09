count = 0
with open("input.txt") as f:
    #f = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
    for line in f:
        # fDig, sDig = 0, 0
        numDig = []
        line = line.strip()
        stackPops = len(line) - 12
        isLargest = -1

        for d in line:
            while numDig and stackPops > 0 and numDig[-1] < d:
                numDig.pop()
                stackPops -= 1
            numDig.append(d)
        #     if int(line[i]) > int(fDig) and i != len(line) - 1:
        #         fDig = line[i]
        #         isLargest = i
        # if isLargest != -1:
        #     for i in range(isLargest + 1, len(line)):
        #         if int(line[i]) > int(sDig):
        #             sDig = line[i]
        # fDig, sDig = str(fDig), str(sDig)
        # num = int(fDig + sDig)
        # print(num)
        print(numDig)
        num = int("".join(numDig[:12]))
        print(num)
        count += num
print(count)
