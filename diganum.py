unidade = ["zero","um","dois","três","quatro","cinco","seis", "sete","oito","nove"]
umadezena = ["dez","onze","doze","treze","quatorze","quinze","dezeseis", "dezesete","dezoito","dezenove"]
dezena = ["vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"]
umacentena = ["cem","cento"]
centena = ["duzentos","trezentos","quatrocentos","quinhentos","seiscentos","setecentos","oitocentos","novecentos"]




def unitarios(num):
        for i in range(len(unidade)):
                if i == int(num):
                        return unidade[i]
def umdec(num): 
        if int(num[0]) == 0:
                if int(num[1:]) != 0:
                        return  unitarios(num[1:]) 
                else:
                        return ""  
        for i in range(len(umadezena)):
                if int(num[1]) == i:
                        return umadezena[i]

def dec(num):
        if int(num[0]) == 0:
                if int(num[1:]) != 0:
                        return unitarios(num[1:])
                else:
                        return ""
        if int(num[0]) == 1:
                return  umdec(num)

        for i in range(len(dezena)):
                if i+2 == int(num[0]):
                        if int(num[1]) == 0:
                                return dezena[i]
                        else:
                                
                                return dezena[i] + " e " + unitarios(num[1])
                                
def umcent(num):
        if int(num[0]) == 0:
                return  dec(num[1:])
        
        if int(num[1]) == 0 and int(num[2]) == 0:
                return umacentena[0]
        else:
                if int(num[1]) != 0:
                        if int(num[1]) != 1:
                                return umacentena[1] + " e " + dec(num[1]+num[2])
                        else:
                                return umacentena[1] + " e " + umdec(num[1]+num[2])

                if int(num[2]) != 0 and int(num[1]) == 0:
                        return umacentena[1] + " e " + unitarios(num[2])
def cent(num):
        if int(num[0]) == 0:
                return dec(num[1:])
        if int(num[0]) == 1:
                return  umcent(num)

        for i in range(len(centena)):
                if int(num[0]) == i+2:
                        if int(num[1]) == 0 and int(num[2]) == 0:
                                return centena[i]
                        else:
                                if int(num[2]) != 0 and int(num[1]) == 0:      
                                        return centena[i] + " e " + unitarios(num[2])
                                if int(num[1]) != 1:
                                        return centena[i] + " e " + dec(num[1]+num[2])
                                else:
                                        return centena[i] + " e " + umdec(num[1]+num[2])
                                
def mil(num):

        if int(num[0]) == 0:
                return  cent(num[1:])

        if int(num[1]) == 0 and  int(num[2]) == 0 and int(num[3]) == 0 and int(num[0]) == 1:
                return "mil"

        if int(num[1]) == 0 and int(num[2]) == 0 and int(num[3]) == 0 and int(num[0]) != 1:
                return unitarios(num[0]) +" mil"
   
        for i in range(4):               
     
                
                                        
                if int(num[i]) != 0 and i == 1: #SE SEGUNDO DIGITO DIFERENTE DE ZERO
                        if int(num[i]) != 1:
                                return unitarios(num[0]) +" mil e "+ cent(num[i:])
                                break
                        else:
                                return unitarios(num[0]) +" mil e "+ umcent(num[i:])
                                break

                if int(num[i]) != 0 and i == 2: #= TERCEIRO =  =  = =
                        if int(num[i]) != 1:
                                return unitarios(num[0]) +" mil e "+ dec(num[i:])
                                break
                        else:
                                return unitarios(num[0]) +" mil e "+ umdec(num[i:])
                                break

                if int(num[i]) != 0 and i == 3:#= QUARTO
                        
                        return unitarios(num[0]) +" mil e "+ unitarios(num[i:])
                        break
                        


    


def dezmil(num):
        if int(num[0]) == 0:
                return  mil(num[1:])
        if int(num[0]) == 1: # 10 mil

                centeninha = num[2:]
                if centeninha == "000":
                        return umdec(num[0]+num[1])+ " mil"
                for i in range (3):
                        if int(centeninha[i]) != 0 and i == 0:
                                if int(centeninha[i]) == 1:
                                        return umdec(num[0]+num[1])+ " mil e " + umcent(centeninha)
                                        break
                                else:
                                        return umdec(num[0]+num[1])+ " mil e " + cent(centeninha)
                                        break

                        if int(centeninha[i]) != 0 and i == 1:
                                if int(centeninha[i]) == 1:
                                        return umdec(num[0]+num[1])+ " mil e " + umdec(centeninha[i:])
                                        break
                                else:
                                        return umdec(num[0]+num[1])+ " mil e " + dec(centeninha[i:])
                                        break
                        if int(centeninha[i]) != 0 and i == 2:     
                                return umdec(num[0]+num[1])+ " mil e " + unitarios(centeninha[i:])
                                break
                                
              
        else:
                centeninha = num[2:]
                if centeninha == "000":
                        return dec(num[0]+num[1])+ " mil"

                for i in range (3):
                        if int(centeninha[i]) != 0 and i == 0:
                                if int(centeninha[i]) == 1:
                                        return dec(num[0]+num[1])+ " mil e " + umcent(centeninha)
                                        break
                                else:
                                        return dec(num[0]+num[1])+ " mil e " + cent(centeninha)
                                        break

                        if int(centeninha[i]) != 0 and i == 1:
                                if int(centeninha[i]) == 1:
                                        return dec(num[0]+num[1])+ " mil e " + umdec(centeninha[i:])
                                        break
                                else:
                                        return dec(num[0]+num[1])+ " mil e " + dec(centeninha[i:])
                                        break
                        if int(centeninha[i]) != 0 and i == 2:     
                                return dec(num[0]+num[1])+ " mil e " + unitarios(centeninha[i:])
                                break
              

def cem_mil(num):
        if int(num[0]) == 0:
                return dezmil(num[1:])
        if int(num[0]) == 1:
                centeninha = num[3:]
                if centeninha == "000":
                        return umcent(num[0]+num[1]+num[2])+ " mil"

                for i in range (3):
                        if int(centeninha[i]) != 0 and i == 0:
                                if int(centeninha[i]) == 1:
                                        return umcent(num[0]+num[1]+num[2])+ " mil " + umcent(centeninha)
                                        break
                                else:
                                        return umcent(num[0]+num[1]+num[2])+ " mil " + cent(centeninha)
                                        break

                        if int(centeninha[i]) != 0 and i == 1:
                                if int(centeninha[i]) == 1:
                                        return umcent(num[0]+num[1]+num[2])+ " mil e " + umdec(centeninha[i:])
                                        break
                                else:
                                        return umcent(num[0]+num[1]+num[2])+ " mil e " + dec(centeninha[i:])
                                        break
                        if int(centeninha[i]) != 0 and i == 2:     
                                return umcent(num[0]+num[1]+num[2])+ " mil e " + unitarios(centeninha[i:])
                                break        

          
        else:
                centeninha = num[3:]
                if centeninha == "000":
                        return cent(num[0]+num[1]+num[2])+ " mil"

                for i in range (3):
                        if int(centeninha[i]) != 0 and i == 0:
                                if int(centeninha[i]) == 1:
                                        return cent(num[0]+num[1]+num[2])+ " mil e " + umcent(centeninha)
                                        break
                                else:
                                        return cent(num[0]+num[1]+num[2])+ " mil e " + cent(centeninha)
                                        break

                        if int(centeninha[i]) != 0 and i == 1:
                                if int(centeninha[i]) == 1:
                                        return cent(num[0]+num[1]+num[2])+ " mil e " + umdec(centeninha[i:])
                                        break
                                else:
                                        return cent(num[0]+num[1]+num[2])+ " mil e " + dec(centeninha[i:])
                                        break
                        if int(centeninha[i]) != 0 and i == 2:     
                                return cent(num[0]+num[1]+num[2])+ " mil e " + unitarios(centeninha[i:])
                                break        




def milhao(num):
        if int(num[0]) == 1 and int(num[1]) == 0 and int(num[2]) == 0 and int(num[3]) == 0 and int(num[4]) == 0 and int(num[5]) == 0 and int(num[6]) == 0:
                return "Um milhão"
        if int(num[0]) != 1 and int(num[0]) != 0 and int(num[1]) == 0 and int(num[2]) == 0 and int(num[3]) == 0 and int(num[4]) == 0 and int(num[5]) == 0 and int(num[6]) == 0:
                return unitarios(num[0]) +  " milhões"
        if int(num[0]) == 0:
                return cem_mil(num[1:])

        if cem_mil(num[1:]) != "":

                if int(num[0]) != 1:
                        if len(cem_mil(num[1:])) <= 16:
                                return unitarios(num[0]) + " milhões e " + cem_mil(num[1:])
                                
                        else:
                                return unitarios(num[0]) + " milhões " + cem_mil(num[1:])
                if int(num[0]) == 1:
                                if len(cem_mil(num[1:])) <= 16:
                                        return unitarios(num[0]) + " milhão e "+ cem_mil(num[1:])
                                        
                                else:
                                        return unitarios(num[0]) + " milhão "+ cem_mil(num[1:])
                                        

       
def dezmilhoes(num):
        if int(num[0]) == 0:
                return milhao(num[1:])

        if int(num[0]) == 1:
                if cem_mil(num[2:]) != "":
                        if len(cem_mil(num[2:])) <= 16:
                                return umdec(num[0]+num[1])+ " milhões e " +  cem_mil(num[2:]) 
                        else:
                                return umdec(num[0]+num[1])+ " milhões " +  cem_mil(num[2:]) 
                else:
                        return umdec(num[0]+num[1])+ " milhões"
        else:
                if cem_mil(num[2:]) != "":
                        if len(cem_mil(num[2:])) <= 16:
                                return dec(num[0]+num[1]) +" milhões e "+ cem_mil(num[2:])
                        else:
                                return dec(num[0]+num[1])+ " milhões " +  cem_mil(num[2:])
                else:
                        return dec(num[0]+num[1]) +" milhões"

def cem_milhoes(num):
        if int(num[0]) == 0:
                return dezmilhoes(num[1:])

        if int(num[0]) == 1:
                if cem_mil(num[3:]) != "":
                        
                        if len(cem_mil(num[3:])) <= 16:
                                return umcent(num[0]+num[1]+num[2])+ " milhões e " +  cem_mil(num[3:]) 
                        else:
                                
                                return umcent(num[0]+num[1]+num[2])+ " milhões " +  cem_mil(num[3:]) 
                else:
                        return umcent(num[0]+num[1]+num[2])+ " milhões"
        else:
                if cem_mil(num[3:]) != "":
                        if len(cem_mil(num[3:])) <= 16:

                                return cent(num[0]+num[1]+num[2]) +" milhões e "+ cem_mil(num[3:])
                        else:
                                return cent(num[0]+num[1]+num[2])+ " milhões " +  cem_mil(num[3:])

                else:
                        return cent(num[0]+num[1]+num[2]) +" milhões"
def bilhao(num):
        if int(num[0]) == 0:
                return cem_milhoes(num[1:])

        if int(num[0]) == 1 and int(num[1]) == 0 and int(num[2]) == 0 and int(num[3]) == 0 and int(num[4]) == 0 and int(num[5]) == 0 and int(num[6]) == 0:
                return "Um bilhão"
        if int(num[0]) != 1 and int(num[0]) != 0 and int(num[1]) == 0 and int(num[2]) == 0 and int(num[3]) == 0 and int(num[4]) == 0 and int(num[5]) == 0 and int(num[6]) == 0:
                return unitarios(num[0]) +  " bilhões"
        

        if cem_mil(num[1:]) != "":

                if int(num[0]) != 1:
                        if len(cem_milhoes(num[1:])) <= 20:
                               
                                return unitarios(num[0]) + " bilhões e " + cem_milhoes(num[1:])
                                
                        else:
                                
                                return unitarios(num[0]) + " bilhões " + cem_milhoes(num[1:])
                if int(num[0]) == 1:
                                if len(cem_milhoes(num[1:])) <= 20:
                                        return unitarios(num[0]) + " bilhão e "+ cem_milhoes(num[1:])
                                        
                                else:
                                        return unitarios(num[0]) + " bilhão "+ cem_milhoes(num[1:])
def dezbilhoes(num):
        if int(num[0]) == 0:
                return bilhao(num[1:])

        if int(num[0]) == 1:
                if cem_milhoes(num[2:]) != "":
                        if len(cem_milhoes(num[2:])) <= 20:
                                return umdec(num[0]+num[1])+ " bilhões e " +  cem_milhoes(num[2:]) 
                        else:
                                return umdec(num[0]+num[1])+ " bilhões " +  cem_milhoes(num[2:]) 
                else:
                        return umdec(num[0]+num[1])+ " bilhões"
        else:
                if cem_milhoes(num[2:]) != "":
                        if len(cem_milhoes(num[2:])) <= 20:
                                return dec(num[0]+num[1]) +" bilhões e "+ cem_milhoes(num[2:])
                        else:
                                return dec(num[0]+num[1])+ " bilhões " +  cem_milhoes(num[2:])
                else:
                        return dec(num[0]+num[1]) +" bilhões"

def cem_bilhoes(num):
        if int(num[0]) == 0:
                return dezbilhoes(num[1:])

        if int(num[0]) == 1:
                if cem_milhoes(num[3:]) != "":
                        
                        if len(cem_milhoes(num[3:])) <= 20:
                                return umcent(num[0]+num[1]+num[2])+ " bilhões e " +  cem_milhoes(num[3:]) 
                        else:
                                
                                return umcent(num[0]+num[1]+num[2])+ " bilhões " +  cem_milhoes(num[3:]) 
                else:
                        return umcent(num[0]+num[1]+num[2])+ " bilhões"
        else:
                if cem_milhoes(num[3:]) != "":
                        if len(cem_milhoes(num[3:])) <= 20:

                                return cent(num[0]+num[1]+num[2]) +" bilhões e "+ cem_milhoes(num[3:])
                        else:
                                return cent(num[0]+num[1]+num[2])+ " bilhões " +  cem_milhoes(num[3:])

                else:
                        return cent(num[0]+num[1]+num[2]) +" bilhões"




def __main__():
        run= True
        while(run):
                num = input("digite um numero: ")
                
                if len(num) >= 2 and num[0] == "0":
                        run= False
                else:

                        if len(num) == 1:
                                
                                print(unitarios(num))
                                
                                        

                        if len(num) == 2:
                                
                                if int(num[0]) == 1:
                                        print(umdec(num))

                                else:

                                        print(dec(num))


                        if len(num) == 3:

                                if int(num[0]) == 1:
                                        print(umcent(num))
                                else:
                                        print(cent(num))
                        if len(num) == 4:
                                print(mil(num))

                        if len(num) == 5:
                                print(dezmil(num))
                                
                        if len(num) == 6:
                                print(cem_mil(num))
                        
                        if len(num) == 7:
                                print(milhao(num))
                        if len(num) == 8:
                                print(dezmilhoes(num))
                        if len(num) == 9:
                                print(cem_milhoes(num))
                        if len(num) == 10:
                                print(bilhao(num))
                        if len(num) == 11:
                                print(dezbilhoes(num))
                        if len(num) == 12:
                                print(cem_bilhoes(num))



__main__()