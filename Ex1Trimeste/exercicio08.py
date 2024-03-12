print("nivel de glicose")

glicose = int(input("digite o numero da sua glicose"))

if(glicose <= 100):
    print("sua glicose esta normal")
elif(100 < glicose <= 140):
    print("sua glicose esta elevada (high)")
elif(glicose > 140):
    print("voce tem diabete")