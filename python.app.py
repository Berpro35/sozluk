sozluk = {
        "LOL" : "komik bir şeye verilen cevap",
        "CRINGE" : "garip ya da utandırıcı bir şey",
        "ROFL" : "bir şakaya karşılık cevap",
        "SHEESH" : "onaylamamak",
        "CREEPY" : "korkunç",
        "AGGRO" : "agresifleşmek/sinirlenmek"
}

kelime = input("Burada olupta bilmediğiniz kelimeleri yazınız(hepsini büyük harflerle yazın!): ")

if kelime in sozluk:
    print(sozluk[kelime])
else:
    print("aradığınız kelime bulunmuyor")
