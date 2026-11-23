def hex_coz(kod):
    kod = kod.lstrip("#")
    rgb=[int(kod[i:i+2],16) for i in (0,2,4)]
    return rgb,[format(x,"08b") for x in rgb]
print(hex_coz("#F05923"))
