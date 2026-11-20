#1D

product = "computer"

product_computer =["montor","mouse","keyboard"]

#1d


   
#2D

product_car =[
    ["honda","toyota", "nissan"], 
    ["NMW", "BENZ", "worswagen"],
    ["FORD", "Chevy","ram"]
]

#loop1


#3D
 
product_car = [
    [ ["ประเทศญี่ปุ่น"], ["honda", "toyota", "nissan"] ],
    [ ["ประเทศเยอรมัน"], ["NMW", "BENZ", "worswagen"] ],
    [ ["ประเทศอเมริกา"], ["FORD", "Chevy", "ram"] ]
]

for i in range(len(product_car)):
    for j in range(len(product_car[i])):
        for k in range(len(product_car[i][j])):
            print(product_car[i][j][k], end=" ")
    print()
 
 
