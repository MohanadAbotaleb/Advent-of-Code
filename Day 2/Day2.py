count = 0
with open("input.txt") as f:    
    ranges = [] 
    for line in f:
        ranges = line.split(",")
    for prod_range in ranges:
        start, end = prod_range.split("-")
        for item in range(int(start), int(end)):
            # part 1 uses array s1 = [] 
            i, pref = 1, 0
            item = str(item)
            l = len(item)
            lps = [0 for i in range(l)]
            while i < l:
                if item[i] == item[pref]:
                    i += 1
                    pref += 1
                    lps[i-1] = pref
                else:
                    if pref > 0:
                        pref = lps[pref - 1]
                    elif pref == 0:
                        lps[i] = 0
                        i += 1
            k = lps[l - 1]
            p = l - k
            if k > 0 and l % p == 0:
                count += int(item)
            #l = len(item)//2
            #s1 = item[:l]
            #s2 = item[l:]
            #print(s1)
            #print(dic_vals)
            #print(len(dic_vals))
            #if len(dic_vals) == 1:
                #count += int(item)
            #if s1 == s2:
               # count += int(item)
    print(count)

