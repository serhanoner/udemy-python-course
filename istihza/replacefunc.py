kardiz = "memleket"
kardiz2 = kardiz.replace("e", "E")
print(kardiz2)

iller = "ADIYAMAN, ISPARTA, DİYARBAKIR, BURSA, İSTANBUL"
iller2 = iller.replace("I","ı").replace("İ","i").lower()
print(iller2)

d1 = "python.ogg"
d2 = "tkinter.mp3"
d3 = "pygtk.ogg"
d4 = "movie.avi"
d5 = "sarki.mp3"
d6 = "filanca.ogg"
d7 = "falanca.mp3"
d8 = "dosya.avi"
d9 = "perl.ogg"
d10 = "c.avi"
d11 = "c++.mp3"
for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
    if i.endswith(".mp3"):
        print(i)