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
                return umadezena[int(num[1])]

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
            if dec(num[1:]) != "":
                return umacentena[1] + " e " + dec(num[1]+num[2])
                
            else:
                return umacentena[0]

        for i in range(len(centena)):
                if int(num[0]) == i+2:
                    if dec(num[1:]) != "":
                        return centena[i] + " e " + dec(num[1]+num[2])
                    else:
                        return centena[i]


def mil(num):
    return milhares(num,1,cent,unitarios,cent,num[0])
                        

def dezmil(num):
    doisdig = num[0]+num[1]
    return milhares(num,2,mil,dec,cent,doisdig) 

                
def cem_mil(num):      
    tresdig = num[0]+num[1]+num[2]
    return milhares(num,3,dezmil,cent,cent,tresdig)              


def milhares(num,numcut,func,func2,func3,string):
    if int(num[0]) == 0:
                return func(num[1:])

    if cent(num[numcut:]) != "":  
        if len(str(num)) != 4:
                if len(str(func2(num[numcut:])))  <= 12 or num[numcut:][0]=="0": 
                    return func2(string)+ " mil e " + func3(num[numcut:])
                    
                else: 
                    return func2(string)+ " mil " + func3(num[numcut:]) 
        else:
            if int(num[0]) != 1: 
                    if len(str(func(num[numcut:]))) <= 12 or num[numcut:][0]=="0" :
                        return func2(string) +" mil e " + func3(num[numcut:])

                    else:
                        return func2(string) +" mil "+ func3(num[numcut:])
            else:
                if len(str(func(num[numcut:]))) <= 12 or num[numcut:][0]=="0":
                    return "mil e " + func3(num[numcut:])
                else:
                    return "mil " + func3(num[numcut:])
                                                
    else:
        if len(str(num)) == 4:  
            if int(num[0]) != 1:
                return func2(string) +" mil"
            else:
                return "mil"  
        else:
            return func2(string)+ " mil"   
        



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

        return umbiumi(num,cem_milhoes,"bilhão","bilhões",21,1)

def dezbilhoes(num):
        if int(num[0]) == 0:
                return bilhao(num[1:])

        doisdig = num[0]+num[1]
        return cembicemi(num,cem_milhoes,dec,"bilhões",doisdig,21,2)
      
def cem_bilhoes(num):
        if int(num[0]) == 0:
                return dezbilhoes(num[1:])
        tresdig = num[0]+num[1]+num[2]

        return cembicemi(num,cem_milhoes,cent,"bilhões",tresdig,21,3)

def trilhao(num):
        if int(num[0]) == 0:
                return cem_bilhoes(num[1:])

        return umbiumi(num,cem_bilhoes,"trilhão","trilhões",21,1)
def deztri(num):
    if int(num[0]) == 0:
                return trilhao(num[1:])
    doisdig = num[0]+num[1]
    return cembicemi(num,cem_bilhoes,dec,"trilhões",doisdig,21,2)

def cemtri(num):
    if int(num[0]) == 0:
                return deztri(num[1:])
    tresdig = num[0]+num[1]+num[2]
    return cembicemi(num,cem_bilhoes,cent,"trilhões",tresdig,21,3)


def cembicemi(num,func,func2,string,string2,lstr,numcut):#centena e dezena de multiplos numeros
        
        if func(num[numcut:]) != "":
                if len(func(num[numcut:])) <= lstr:

                        return func2(string2) +" " + string + " e "+  func(num[numcut:]) 
                else:
                        return func2(string2)+  " " + string +" "+  func(num[numcut:])

        else:
                return func2(string2) + " " + string + " "+ func(num[numcut:])

def umbiumi(num,func,string,string2,lstr,numcut):#unidade de multiplos numeros
        if func(num[numcut:]) != "":
                if int(num[0]) != 1:

                        if len(func(num[numcut:])) <= lstr:
                               
                                return unitarios(num[0]) + " " + string2 + " e " + func(num[numcut:])
                                
                        else:
                                
                                return unitarios(num[0]) + " " + string2 +" " + func(num[numcut:])
                if int(num[0]) == 1:
                                if len(func(num[1:])) <= lstr:
                                        return unitarios(num[0]) + " " + string + " e "+ func(num[numcut:])
                                        
                                else:
                                        return unitarios(num[0]) + " " + string +" "+ func(num[numcut:])
        else:
                if int(num[0]) != 1:
                        return unitarios(num[0]) +  " " + string2 +" "
                else:
                        return unitarios(num[0]) + " " + string
def comandoselec(num):
        for i in range(len(comandos)):
                if len(num) == i+1:
                        return comandos[i](num)

comandos = [unitarios,dec,cent,mil,dezmil,cem_mil,milhao,dezmilhoes,cem_milhoes,bilhao,dezbilhoes,cem_bilhoes,trilhao,deztri,cemtri]

def __main__():
        run= True
        while(run):
                num = input("digite um numero (00 pra sair): ")
                
                if len(num) >= 2 and num[0] == "0":
                        run= False
                else:
                        if num[0] != "-":
                            print(comandoselec(num))
                        else:
                            if num == "-0":
                                pass
                            else:
                                print("menos " + comandoselec(num[1:]))



__main__()
