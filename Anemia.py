HGB = float(input("гемоглобин = "))
HCT = float(input("гематокрит = "))
MCHC = float(input("средняя концентрация гемоглобина в эритроците = "))  
MCH = float(input("среднее содержание гемоглобина в эритроците = "))
MCV = float(input("средний объем эритроцита = "))
RBC = float(input("количество эритроцитов = "))

mHGB = (125 - HGB) / (125 - 115)
mHCT = (0.38 - HCT) / (0.38 - 0.30)
mMCHC = (80 - MCHC) / (80 - 64)
mMCH = (MCH - 34) / (36.4 - 34)
mMCV = (80 - MCV) / (80 - 64)
mRBC = (4 - RBC) / (4 - 3.5)

def calculate_mMCHMicro(MCH):
    return (27-MCH)/(27-18.5)
    
def calculate_mMCVMicro(MCV):
    return (80-MCV)/(80-64)

def calculate_mMCHMacro(MCH):
    return (MCH-34)/(36.4-34)

def calculate_mMCVMacro(MCV):
    return (MCV-95)/(129-95)

def calculate_mMCHNormo(MCH):
    if 18.5 <= MCH <= 27:
        return (MCH - 18.5) / (27 - 18.5)
    elif 34 <= MCH <= 38:
        return (36.4 - MCH) / (36.4 - 34)
    else:
        return 0.0

def calculate_mMCVNormo(MCV):
    if 90 <= MCV <= 80:
        return (MCV -80) / (90-80)
    elif 95 <= MCV <= 100:
        return (100 - MCV) / (100 - 95)
    else:
        return 0.0
    
    
mMCHMicro = float(calculate_mMCHMicro(MCH))
mMCVMicro = float(calculate_mMCVMicro(MCV))                                         
mMCHMacro = float(calculate_mMCHMacro(MCH))
mMCVMacro = float(calculate_mMCVMacro(MCV))
mMCHNormo = float(calculate_mMCHNormo(MCH))
mMCVNormo = float(calculate_mMCVNormo(MCV))

M = (mHGB * 0.5) + (mHCT * 0.1) + (mMCHC * 0.1) + (mMCH * 0.1) + (mMCV * 0.1) + (mRBC * 0.1)
print("Значение M =", M)

if M >= 0.5:
    print("Соответствие результатов анализа состоянию анемии")
elif 0.2 <= M < 0.5:
    print("Подозрение на анемию")
elif 0 <= M < 0.2:
    print("Соответствие результатов анализа норме")


MMicro = float(mMCHMicro*0.5 + mMCVMicro*0.5)
if MMicro >= 0.5:
    print("Анемия может быть отнесена к микроцитарной.", "Значение M микро=", MMicro)
    Fer_ZDA = float(input("Значение ферритина = "))
    
    def calculate_Fer_ZDA(Fer_ZDA):
        return (40-Fer_ZDA)/(40-20)
    print("Для железодефицитной анемии принадлежность к патологии равна = ", calculate_Fer_ZDA(Fer_ZDA))


    
MMacro = float(mMCHMacro*0.5 + mMCVMacro*0.5)
if MMacro >= 0.5:
    print("Анемия может быть отнесена к макроцитарной.", "Значение M макро=", MMacro)
    B12 = float(input("Значение витамина B12 = "))
    
    def calculate_B12(B12):
         return (400-B12)/(400-100)
    print("Для В12-дефицитных анемий принадлежность к патологии равна = ", calculate_B12(B12))


MNormo = float(mMCHNormo*0.5 + mMCVNormo*0.5)
if MNormo >= 0.5:
    print("Анемия может быть отнесена к нормоцитарной.", "Значение M нормо=", MNormo)
    Fer_AXZ = float(input("Значение ферритина = "))
    Fer_ZDA = Fer_AXZ
    
    def calculate_Fer_AXZ(Fer_AXZ):
        return (Fer_AXZ-40)/(60-40)
    print("Для анемии при хронических заболеваниях принадлежность к патологии равна = ", calculate_Fer_AXZ)(Fer_AXZ)
        
    def calculate_Fer_ZDA(Fer_ZDA):
        return (40-Fer_ZDA)/(40-20)
    print("Для железодефицитной анемии принадлежность к патологии равна = ", calculate_Fer_ZDA(Fer_ZDA))

    
