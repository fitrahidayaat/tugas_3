def total_kemunculan(mylist):
    data = {}
    for i in mylist:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    return dict(sorted(data.items(), key=lambda item: item[1]))

mylist = input("Masukkan list : ").split() # input list dengan spasi sebagai pemisah antar items
mydict = total_kemunculan(mylist)
for k,v in mydict.items():
    print(f"{k} : {v}")