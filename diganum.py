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
                    if len(cent(num[1:])) <= 12 or num[1:][0]=="0" :
                        return unitarios(num[0]) +" mil e " + cent(num[1:])

                    else:
                        
                        return unitarios(num[0]) +" mil "+ cent(num[1:])

                else:
                    if len(cent(num[1:])) <= 12 or num[1:][0]=="0":
                        return "mil e " + cent(num[1:])
                    else:
                        return "mil " + cent(num[1:])
        else:
                if int(num[0]) != 1:
                        return unitarios(num[0]) +" mil"
                else:
                        return "mil"
                        

def dezmil(num):
        if int(num[0]) == 0:
                return  mil(num[1:])
        
        
        if cent(num[2:]) != "":        
                if len(cent(num[2:]))  <= 12 or num[2:][0]=="0":  
                    return dec(num[0]+num[1])+ " mil e " + cent(num[2:])
                else:
                    return dec(num[0]+num[1])+ " mil " + cent(num[2:])

        else:
                return dec(num[0]+num[1])+ " mil"
                
              

def cem_mil(num):
        if int(num[0]) == 0:
                return dezmil(num[1:])

        if cent(num[3:]) != "":  
                if len(cent(num[3:]))  <= 12 or num[3:][0]=="0":         
                    return cent(num[0]+num[1]+num[2])+ " mil e " + cent(num[3:])
                else:
                    return cent(num[0]+num[1]+num[2])+ " mil " + cent(num[3:])

                      
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

comandos = [unitarios,dec,cent,mil,dezmil,cem_mil,milhao,dezmilhoes,cem_milhoes,bilhao,dezbilhoes,cem_bilhoes,trilhao]

def __main__():
        run= True
        while(run):
                num = input("digite um numero: ")
                
                if len(num) >= 2 and num[0] == "0":
                        run= False
                else:

                        print(comandoselec(num))



__main__()
