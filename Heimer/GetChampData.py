# can be rewritten in a similar style as the items can be, rewrite by scraping ids
import json
import urllib.request as request
import pandas as pd
import requests

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
'Renekton','Rengar','Riven','Rumble','Ryze', 'Samira','Sejuani','Senna','Seraphine','Sett','Shaco',
'Shen','Shyvana','Singed','Sion','Sivir','Skarner','Sona','Soraka','Swain','Sylas','Syndra','TahmKench',
'Taliyah','Talon','Taric','Teemo','Thresh','Tristana','Trundle','Tryndamere','TwistedFate','Twitch',
'Udyr','Urgot','Varus','Vayne','Veigar','Velkoz','Vi','Viego','Viktor','Vladimir','Volibear','Warwick','MonkeyKing','Xayah','Xerath','XinZhao','Yasuo','Yone','Yorick','Yuumi','Zac','Zed',
'Ziggs','Zilean','Zoe','Zyra']

def getCurrentChampData(champList):
    for champ in champList:
        url = 'http://cdn.merakianalytics.com/riot/lol/resources/latest/en-US/champions/'+champ+'.json'
        with request.urlopen(request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})) as response:
            source = response.read().decode('utf8')
            data = json.loads(source)

        champ = champ.capitalize()
        with open('ChampionDataFiles/' + champ + '.json', 'w') as f:
            json.dump(data, f, indent = 2)

# getCurrentChampData(champList)