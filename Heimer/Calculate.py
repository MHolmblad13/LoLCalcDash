# This file is where all the general functions for the calculator will be stored
def autoAttackDamage(ad, ap, arm, mr, mixedAuto):
    if(arm < 0):
        adDamage = ad * (2 - (100/(100+arm)))
    if(arm == 0):
        adDamage = ad - 1
    if(arm > 0):
        adDamage = ad * (100/(100+arm))
    if(mixedAuto):
        if(mr < 0):
            magDamage = ap * (2 - (100/(100+mr)))
        if(mr == 0):
            magDamage = ap - 1
        if(mr > 0):
            magDamage = ap * (100/(100+mr))
    
    return magDamage + adDamage

def basicAutoAttack(ad, arm):
    if(arm < 0):
        adDamage = ad * (2 - (100/(100+arm)))
    if(arm == 0):
        adDamage = ad - 1
    if(arm > 0):
        adDamage = ad * (100/(100+arm))
    return adDamage

#In cases like Corki Gatling Gun, this function will be called twice
def abilityDamage(abilityBaseDamage, arm, mr, type):
    if(type == 'physical'):
        if(arm < 0):
            damage = abilityBaseDamage * (2 - (100/(100+arm)))
        if(arm == 0):
            damage = abilityBaseDamage - 1
        if(arm > 0):
            damage = abilityBaseDamage * (100/(100+arm))
    if(type == 'magic'):
        if(mr < 0):
            damage = abilityBaseDamage * (2 - (100/(100+mr)))
        if(mr == 0):
            damage = abilityBaseDamage - 1
        if(mr > 0):
            damage = abilityBaseDamage * (100/(100+mr))
    return damage

def armorReduction(arm, armRedFlat, armRedPer, armPenPer, leth):
    remaining = arm
    if(remaining >= 0):
        remaining = remaining - armRedFlat
    if(remaining >= 0):   
        remaining = remaining - remaining * armRedPer
    if(remaining >= 0):    
        remaining = remaining - remaining * armPenPer
    if(remaining >= 0):    
        remaining = remaining - leth
    return remaining

def mrReduction(mr, mrRedFlat, mrRedPer, magPenPer, magPenFlat):
    remaining = mr
    if(remaining >= 0):
        remaining = remaining - mrRedFlat
    if(remaining >= 0):    
        remaining = remaining - remaining * mrRedPer
    if(remaining >= 0):    
        remaining = remaining - remaining * magPenPer
    if(remaining >= 0):    
        remaining = remaining - magPenFlat
    return remaining