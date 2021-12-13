def penjumlahan_angka(mylist,target):
    mydict = {}
    for i in range(len(mylist)):
        mydict[mylist[i]] = i
    for k in mydict:
        if (target - k) in mydict:
            return [mydict[k], mydict[target-k]]

mylist = list(map(int, input("Masukkan list : ").split())) # input list dengan spasi sebagai pemisah antar items
target = int(input("Target : "))
print(penjumlahan_angka(mylist,target))