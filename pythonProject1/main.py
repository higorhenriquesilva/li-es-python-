nota_1 = int(input("Digite a primeira nota."))
nota_2 = int(input("Digite a segunda nota."))
nota_3 = int(input("Digite a terceira nota."))

media = (nota_1 + nota_2 + nota_3) / 3

if(media < 60):
    print("sua nota é " , media , " infelizmente você reprovou!")
elif(media >= 60):
    print("sua nota é " , media , " voce atingiu a media e passou de ano ")

