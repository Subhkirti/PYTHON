file=open("bank(saral3).txt","w")
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(banks_list):
    file.write(banks_list[i])
    file.write("\n")
    i+=1
file.close()


