unidade = ["zero","um","dois","três","quatro","cinco","seis", "sete","oito","nove"]
umadezena = ["dez","onze","doze","treze","quatorze","quinze","dezeseis", "dezesete","dezoito","dezenove"]
dezena = ["vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"]
umacentena = ["cem","cento"]
centena = ["duzentos","trezentos","quatrocentos","quinhentos","seiscentos","setecentos","oitocentos","novecentos"]




def unitarios(num):
        for i in range(len(unidade)):
                if i == int(num):
                        return unidade[i]

        
def dec(num):
        if int(num[0]) == 0:
                if int(num[1:]) != 0:
                        return unitarios(num[1:])
                else:
                        return ""
        if int(num[0]) == 1:
                for i in range(len(umadezena)):
                        if int(num[1]) == i:
                                return umadezena[i]

        for i in range(len(dezena)):
                if i+2 == int(num[0]):
                        if int(num[1]) == 0:
                                return dezena[i]
                        else:
                                
                                return dezena[i] + " e " + unitarios(num[1])
                                

        
        
def cent(num):
        if int(num[0]) == 0:
                return dec(num[1:])
        if int(num[0]) == 1:
                if int(num[1]) == 0 and int(num[2]) == 0:
                        return umacentena[0] #cem

                if int(num[1]) != 0: #cem e dezena
                        
                        return umacentena[1] + " e " + dec(num[1]+num[2])
                        
                if int(num[2]) != 0 and int(num[1]) == 0:#cem e unidade
                        return umacentena[1] + " e " + unitarios(num[2])


        for i in range(len(centena)):
                if int(num[0]) == i+2:
                        if int(num[1]) == 0 and int(num[2]) == 0:
                                return centena[i]
                        else:
                                if int(num[2]) != 0 and int(num[1]) == 0:      
                                        return centena[i] + " e " + unitarios(num[2])
                                else:
                                      return centena[i] + " e " + dec(num[1]+num[2])  
def mil(num):

        if int(num[0]) == 0:
                return  cent(num[1:])

        
        if cent(num[1:]) != "":      
                if int(num[0]) != 1: 
                        return unitarios(num[0]) +" mil e "+ cent(num[1:])
                else:
                        return "mil e " + cent(num[1:])
        else:
                if int(num[0]) != 1:
                        return unitarios(num[0]) +" mil"
                else:
                        return "mil"
                        

def dezmil(num):
        if int(num[0]) == 0:
                return  mil(num[1:])
        
        
        if cent(num[2:]) != "":            
                return dec(num[0]+num[1])+ " mil e " + cent(num[2:])      
        else:
                return dec(num[0]+num[1])+ " mil"
                
              

def cem_mil(num):
        if int(num[0]) == 0:
                return dezmil(num[1:])

        if cent(num[3:]) != "":            
                return cent(num[0]+num[1]+num[2])+ " mil e " + cent(num[3:])
                      
        else:
                return cent(num[0]+num[1]+num[2])+ " mil"
              
def milhao(num):   
        if int(num[0]) == 0:
                return cem_mil(num[1:])
        return umbiumi(num,cem_mil,"milhão","milhões",16,1)
        
                        

def dezmilhoes(num):
        if int(num[0]) == 0:
                return milhao(num[1:])

        doisdig = num[0]+num[1]
        return cembicemi(num,cem_mil,dec,"milhões",doisdig,16,2)


def cem_milhoes(num):
        if int(num[0]) == 0:
                return dezmilhoes(num[1:])
        tresdig = num[0]+num[1]+num[2]
        return cembicemi(num,cem_mil,cent,"milhões",tresdig,16,3)

def bilhao(num):
        if int(num[0]) == 0:
                return cem_milhoes(num[1:])

        return umbiumi(num,cem_milhoes,"bilhão","bilhões",20,1)

def dezbilhoes(num):
        if int(num[0]) == 0:
                return bilhao(num[1:])

        doisdig = num[0]+num[1]
        return cembicemi(num,cem_milhoes,dec,"bilhões",doisdig,20,2)
      
def cem_bilhoes(num):
        if int(num[0]) == 0:
                return dezbilhoes(num[1:])
        tresdig = num[0]+num[1]+num[2]

        return cembicemi(num,cem_milhoes,cent,"bilhões",tresdig,20,3)


def cembicemi(num,func,func2,string,string2,lstr,numcut):
        
        if func(num[numcut:]) != "":
                if len(func(num[numcut:])) <= lstr:

                        return func2(string2) +" " + string + " e "+  func(num[numcut:]) 
                else:
                        return func2(string2)+  " " + string +" "+  func(num[numcut:])

        else:
                return func2(string2) + " " + string + " "+ func(num[numcut:])

def umbiumi(num,func,string,string2,lstr,numcut):
        if func(num[numcut:]) != "":
                if int(num[0]) != 1:

                        if len(func(num[numcut:])) <= lstr:
                               
                                return unitarios(num[0]) + " " + string2 + " e " + func(num[numcut:])
                                
                        else:
                                
                                return unitarios(num[0]) + " " + string2 +" " + func(num[numcut:])
                if int(num[0]) == 1:
                                if len(func(num[1:])) <= lstr:
                                        return unitarios(num[0]) + " " + string2 + " e "+ func(num[numcut:])
                                        
                                else:
                                        return unitarios(num[0]) + " " + string2 +" "+ func(num[numcut:])
        else:
                if int(num[0]) != 1:
                        return unitarios(num[0]) +  " " + string2 +" "
                else:
                        return unitarios(num[0]) + " " + string


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
                                print(dec(num))
                        if len(num) == 3:
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
