import json
import pandas as pd

champList = ['Aatrox','Ahri','Akali','Alistar','Amumu','Anivia','Annie','Aphelios','Ashe',
'AurelionSol','Azir','Bard','Blitzcrank','Brand','Braum', 'Caitlyn', 'Camille', 'Cassiopeia', 'Chogath', 'Corki','Darius','Diana',
'Draven', 'DrMundo', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora',
'Fizz', 'Galio', 'Gangplank','Garen','Gnar','Gragas', 'Graves', 'Hecarim', 'Heimerdinger',
'Illaoi', 'Irelia', 'Ivern', 'Janna', 'JarvanIV', 'Jax', 'Jayce', 'Jhin', 'Jinx', 'Kaisa', 'Kalista',
'Karma', 'Karthus', 'Kassadin','Katarina','Kayle','Kayn','Kennen','Khazix', 'Kindred',
'Kled','KogMaw','Leblanc','LeeSin','Leona','Lillia','Lissandra','Lucian',
'Lulu','Lux','Malphite','Malzahar','Maokai','MasterYi','MissFortune','Mordekaiser',
'Morgana','Nami','Nasus','Nautilus','Neeko','Nidalee','Nocturne','Nunu','Olaf',
'Orianna','Ornn','Pantheon','Poppy','Pyke','Qiyana','Quinn','Rakan','Rammus','RekSai',
'Renekton','Rengar','Riven','Rumble','Ryze', 'Samira','Sejuani','Senna', 'Seraphine', 'Sett','Shaco',
'Shen','Shyvana','Singed','Sion','Sivir','Skarner','Sona','Soraka','Swain','Sylas','Syndra','TahmKench',
'Taliyah','Talon','Taric','Teemo','Thresh','Tristana','Trundle','Tryndamere','TwistedFate','Twitch',
'Udyr','Urgot','Varus','Vayne','Veigar','Velkoz','Vi','Viktor','Vladimir','Volibear','Warwick','MonkeyKing','Xayah','Xerath','XinZhao','Yasuo','Yone','Yorick','Yuumi','Zac','Zed',
'Ziggs','Zilean','Zoe','Zyra']

def getChampionStatsInfo(champName):
    j = json.load(open('Heimer/ChampionDataFiles/'+champName+'.json'))
    champStatList = []
    attackDamage = j["stats"]["attackDamage"]
    champStatList.append(attackDamage)
    armor = j["stats"]["armor"]
    champStatList.append(armor)
    attackSpeed = j["stats"]["attackSpeed"]
    champStatList.append(attackSpeed)
    attackSpeedRatio = j["stats"]["attackSpeedRatio"]
    champStatList.append(attackSpeedRatio)
    criticalStrikeDamage = j["stats"]["criticalStrikeDamage"]
    champStatList.append(criticalStrikeDamage)
    criticalStrikeDamageModifier = j["stats"]["criticalStrikeDamageModifier"]
    champStatList.append(criticalStrikeDamageModifier)
    health = j["stats"]["health"]
    champStatList.append(health)
    healthRegen = j["stats"]["healthRegen"]
    champStatList.append(healthRegen)
    magicResistance = j["stats"]["magicResistance"]
    champStatList.append(magicResistance)
    mana = j["stats"]["mana"]
    champStatList.append(mana)
    manaRegen = j["stats"]["manaRegen"]
    champStatList.append(manaRegen)
    movespeed = j["stats"]["movespeed"]
    champStatList.append(movespeed)
    champStatDf = pd.DataFrame(champStatList, index = ['attackDamage','armor','attackSpeed',
    'attackSpeedRatio', 'criticalStrikeDamage','criticalStrikeDamageModifier','health','healthRegen',
    'magicResistance','mana','manaRegen','movespeed'])
    return champStatDf

def getFlatBaseStats(baseStatList):
    flatList = []
    flatList.append(baseStatList['flat'])
    return flatList

def getPerLevelBaseStats(baseStatList):
    perLevelList = []
    perLevelList.append(baseStatList['perLevel'])
    return perLevelList

def GetChampionInfo(champName, level):
    overallStatList = []
    baseStatList = getChampionStatsInfo(champName)
    flatStatList = getFlatBaseStats(baseStatList)[0]
    perLevelStatList = getPerLevelBaseStats(baseStatList)[0]
    level = float(level)
    ad = flatStatList['attackDamage'] + perLevelStatList['attackDamage'] * level
    armor = flatStatList['armor'] + perLevelStatList['armor'] * level
    attackSpeed = flatStatList['attackSpeed'] + perLevelStatList['attackSpeed'] * level
    attackSpeedRatio = flatStatList['attackSpeedRatio'] + perLevelStatList['attackSpeedRatio'] * level
    #criticalStrikeDamage = flatStatList['criticalStrikeDamage'] + perLevelStatList['criticialStrikeDamage'] * level
    #criticalStrikeDamageModifier = flatStatList['criticalStrikeDamageModifier'] + perLevelStatList['criticalStrikeDamageModifier'] * level
    health = flatStatList['health'] + perLevelStatList['health'] * level
    healthRegen = flatStatList['healthRegen'] + perLevelStatList['healthRegen'] * level
    magicResistance = flatStatList['magicResistance'] + perLevelStatList['magicResistance'] * level
    mana = flatStatList['mana'] + perLevelStatList['mana'] * level
    manaRegen = flatStatList['manaRegen'] + perLevelStatList['manaRegen'] * level
    movespeed = flatStatList['movespeed'] + perLevelStatList['movespeed'] * level
    ap = 0
    overallStatList = {
        "Ability Power": ap,
        "Attack Damage": ad,
        "Armor": armor,
        "Attack Speed": attackSpeed,
        "Attack Speed Ratio": attackSpeedRatio,
        "Health": health,
        "Health Regen": healthRegen,
        "Magic Resistance": magicResistance,
        "Mana": mana,
        "Mana Regen": manaRegen,
        "Move Speed": movespeed,
    }
    return overallStatList
