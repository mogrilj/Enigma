import lib


abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
reflector = [["a","y"],["b","r"],["d","h"],["f","s"],["g","l"],["i","p"],["j","x"],["k","n"],["m","o"],["e","q"],["t","z"],["v","w"],["c","u"],]
global rotor1
global rotor2
global rotor3



lll = []
nums = [1,2,3]
yn = input("Wollen sie die positionen der Rotoren selbst bestimmen?(j/n)")
if yn == "j":
    rotorLayout1 = input("Bestimme die Position des ersten Rotoren:")
    rotorLayout2 = input("Bestimme die Position des zweiten Rotoren:")
    rotorLayout3 = input("Bestimme die Position des dritten Rotoren:")

    rotorLayout1 = int(rotorLayout1)
    rotorLayout2 = int(rotorLayout2)
    rotorLayout3 = int(rotorLayout3)
    if rotorLayout1 in nums:
        if rotorLayout1 == 1:  
            rotor1 = lib.getRotor1()
            if rotorLayout2 == 2:
                rotor2 = lib.getRotor2()
                rotor3 = lib.getRotor3()
            else:
                rotor2 = lib.getRotor3()
                rotor3 = lib.getRotor2()
        if rotorLayout2 == 1:
            rotor1 = lib.getRotor2()
            if rotorLayout1 == 2:
                rotor2 = lib.getRotor1()
                rotor3 = lib.getRotor3()
            else:
                rotor2 = lib.getRotor3()
                rotor3 = lib.getRotor1()
        if rotorLayout3 == 1:
            rotor1 = lib.getRotor3()
            if rotorLayout2 == 2:
                rotor2 = lib.getRotor2()
                rotor3 = lib.getRotor1()
            else:
                rotor2 = lib.getRotor1()
                rotor3 = lib.getRotor2()
    else:
        rotor1 = lib.getRotor1()
        rotor2 = lib.getRotor2()
        rotor3 = lib.getRotor3()
else:
    rotor1 = lib.getRotor1()
    rotor2 = lib.getRotor2()
    rotor3 = lib.getRotor3()

yn = input("Willst du die Rotor Startposition bestimmen?(j/n)")

if yn == "ja" or yn == "j":
    rotorsetting1 = input("Einstellung des ersten Rotors:")
    rotorsetting2 = input("Einstellung des zweiten Rotors:")
    rotorsetting3 = input("Einstellung des dritten Rotors:")

    if rotorsetting1 == None or rotorsetting1 == "":
        rotorsetting1 = 0
    if rotorsetting2 == None or rotorsetting2 == "":
        rotorsetting2 = 0
    if rotorsetting3 == None or rotorsetting3 == "":
        rotorsetting3 = 0

    rotorsetting1 = abc.index(rotorsetting1)
    rotorsetting2 = abc.index(rotorsetting2)
    rotorsetting3 = abc.index(rotorsetting3)
else:
    rotorsetting1 = 0
    rotorsetting2 = 0
    rotorsetting3 = 0

yn = input("Willst du das Steckbrett verwenden?(j/n):")

if yn == "ja" or yn == "j":
    pairs = input("Gib die gewünschten Buchstabenpaare an:")
    if pairs == "" or pairs == None:
        pass
    else:
        l = []
        ll = []
        lll = []
        for prs in pairs.split(" "):
            
            l.append(prs)
        for items in l:
             
            for letters in items:
                
                
                ll.append(letters)
                
                

            lll.append(ll)
           
            ll = []    
        
        
        
else:
    pass
    
def crypt(sr1,sr2,sr3,pairs):
    b = False
    bb = False
    bbb = False
    C = ""
    Chiffre = ""
    for i in range(sr3,sr3 + 26):
        if i > 25 and b == False:
            b = True
            ii = 0
        if b:
            ii = ii + 1
        else:
            ii = i
        
        l = rotor3[ii]
        for idx in range(sr2,sr2 + 26):
            if idx > 25 and bb == False:
                bb = True
                idxx = 0
            if bb:
                idxx = idxx + 1
            else:
                idxx = idx
            lst = rotor2[idxx]
            
            for index in range(sr1,sr1 + 26):
                if index > 25 and bbb == False:
                    bbb = True
                    indexx = 0
                if bbb:
                    indexx = indexx + 1
                else:
                    indexx = index
                liste = rotor1[indexx]
                
                
                Letter = input("Gib einen Buchstaben ein:")
                for paar in pairs:
                    
                    if Letter in paar:
                        
                        if paar.index(Letter) == 0:
                            Letter = paar[1]
                            
                        else:
                            Letter = paar[0]
               
                C = liste[abc.index(Letter)]
                
                C = lst[abc.index(C)]
                
                C = l[abc.index(C)]
                
                for ref in reflector:
                    if C in ref:
                        
                        if ref.index(C) == 0:
                            tausch = 1
                        else:
                            tausch = 0
                        tausch = ref[tausch]
                        
                        C = abc[l.index(tausch)]
                        
                        C = abc[lst.index(C)]
                       
                        C = abc[liste.index(C)]
                        
                        for paar in pairs:
                            
                            if C in paar:
                        
                                if paar.index(C) == 0:
                                    C = paar[1]
                                    
                                else:
                                    C = paar[0]
                        
                        
                        break
                        
                    
                        
                
                Chiffre = Chiffre + C
                print(Chiffre.upper())

crypt(rotorsetting1 + 1,rotorsetting2,rotorsetting3,lll)
