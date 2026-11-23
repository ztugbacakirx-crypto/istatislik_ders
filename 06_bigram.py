from collections import defaultdict,Counter
derlem="veri verilendir veri sayıdır sayı mantıktır veri verilendir".split()
sonraki=defaultdict(Counter)
for k1,k2 in zip(derlem,derlem[1:]):
                 sonraki[k1][k2] += 1
toplam=sum(sonraki["veri"].values())
for kelime, n in sonraki["veri"].most_common():
    print(f"veri -> {kelime}: %{100*n/toplam:.0f}")
