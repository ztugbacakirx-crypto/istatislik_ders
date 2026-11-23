import math
for ad, p in [("kesin olay",1),("yazı-tura",1/2),("zar",1/6)]:
    print(ad,abs(round(-math.log2(p),2)),"bit")
    
