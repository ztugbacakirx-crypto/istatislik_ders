from collections import Counter
metin= "veri sayısallaştırılmış özelliklerdir verilenden üretilene"
sayim= Counter(h for h in metin.lower() if h.isalpha())
print(sayim.most_common(5))
