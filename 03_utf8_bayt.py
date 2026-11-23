for h in ["I","İ","g","ğ","c","ç"]:
    b=h.encode("utf-8")
    print(h, len(b),"bayt" ,b.hex(" "))
