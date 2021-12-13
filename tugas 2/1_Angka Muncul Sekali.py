def angka_muncul_sekali(s):
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    res = []
    for k in d:
        if d[k] == 1:
            res.append(int(k))
    return res

s = input("Masukkan string : ")
print(angka_muncul_sekali(s))