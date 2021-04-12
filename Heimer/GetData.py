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

itemList = ['1001','1004','1006','1011','1018','1026','1027','1028','1029','1031',
'1033','1035','1036','1037','1038','1039','1042','1043','1052','1053','1054','1055',
'1056','1057','1058','1082','1083','2003','2010','2015','2031','2033','2047','2051',
'2052','2055','2065','2138','2139','2140','2403','2420','2421','2422','2423','3001',
'3003','3004','3006','3009','3011','3020','3024','3026','3031','3033','3035','3036',
'3040','3041','3042','3043','3044','3046','3047','3048','3050','3051','3053','3057',
'3065','3066','3067','3068','3070','3071','3072','3074','3075','3076','3077','3078',
'3082','3083','3085','3086','3089','3091','3094','3095','3100','3102','3105','3107',
'3108','3109','3110','3111','3112','3113','3114','3115','3116','3117','3123','3124',
'3133','3134','3135','3139','3140','3142','3143','3145','3152','3153','3155','3156',
'3157','3158','3165','3177','3179','3181','3184','3190','3191','3193','3211','3222',
'3340','3363','3364','3400','3504','3508','3513','3514','3599','3600','3742','3748',
'3801','3802','3814','3850','3851','3853','3854','3855','3857','3858','3859','3860',
'3862','3863','3864','3916','4005','4401','4403','4628','4629','4630','4632','4633',
'4635','4636','4637','4638','4641','4642','4643','6029','6035','6333','6609','6616',
'6617','6630','6631','6632','6653','6655','6656','6660','6662','6664','6670','6671',
'6672','6673','6675','6676','6677','6691','6692','6693','6694','6695']

itemNames = ['Boots', 'Faerie Charm', 'Rejuvenation Bead', "Giant's Belt", 'Cloak of Agility', 'Blasting Wand', 
'Sapphire Crystal', 'Ruby Crystal', 'Cloth Armor', 'Chain Vest', 'Null-Magic Mantle', 'Emberknife', 'Long Sword',
'Pickaxe', 'B. F. Sword', 'Hailblade', 'Dagger', 'Recurve Bow', 'Amplifying Tome', 'Vampiric Scepter', "Doran's Shield",
"Doran's Blade", "Doran's Ring", 'Negatron Cloak', 'Needlessly Large Rod', 'Dark Seal', 'Cull', 'Health Potion', 
'Total Biscuit of Everlasting Will', 'Kircheis Shard', 'Refillable Potion', 'Corrupting Potion', "Oracle's Extract", 
"Guardian's Horn", 'Poro-Snax', 'Control Ward', "Shurelya's Battlesong", 'Elixir of Iron', 'Elixir of Sorcery', 
'Elixir of Wrath', 'Minion Dematerializer', 'Stopwatch', 'Broken Stopwatch', 'Slightly Magical Footware', 'StopwatchURF', 
'Abyssal Mask', "Archangel's Staff", 'Manamune', "Berserker's Greaves", 'Boots of Swiftness', 'Chemtech Putrifier', 
"Sorcerer's Shoes", 'Glacial Buckler', 'Guardian Angel', 'Infinity Edge', 'Mortal Reminder', 'Last Whisper',
"Lord Dominik's Regards", "Seraph's Embrace", "Mejai's Soulstealer", 'Muramana', 'MuramanaURF', 'Phage', 'Phantom Dancer', 
'Plated Steelcaps', "Seraph's EmbraceURF", "Zeke's Convergence", 'Hearthbound Axe', "Sterak's Gage", 'Sheen', 'Spirit Visage',
'Winged Moonplate', 'Kindlegem', 'Sunfire Aegis', 'Tear of the Goddess','Black Cleaver', 'Bloodthirster', 'Ravenous Hydra', 
'Thornmail', 'Bramble Vest', 'Tiamat', 'Trinity Force', "Warden's Mail", "Warmog's Armor", "Runaan's Hurricane", 'Zeal',
"Rabadon's Deathcap", "Wit's End", 'Rapid Firecannon', 'Stormrazor', 'Lich Bane', "Banshee's Veil", 'Aegis of the Legion', 
'Redemption', 'Fiendish Codex', "Knight's Vow", 'Frozen Heart', "Mercury's Treads", "Guardian's Orb", 'Aether Wisp',
'Forbidden Idol', "Nashor's Tooth", "Rylai's Crystal Scepter", 'Mobility Boots', "Executioner's Calling", "Guinsoo's Rageblade", 
"Caulfield's Warhammer", 'Serrated Dirk', 'Void Staff', 'Mercurial Scimitar', 'Quicksilver Sash', "Youmuu's Ghostblade", 
"Randuin's Omen", 'Hextech Alternator', 'Hextech Rocketbelt', 'Blade of The Ruined King', 'Hexdrinker', 'Maw of Malmortius', 
"Zhonya's Hourglass", 'Ionian Boots of Lucidity', 'Morellonomicon', "Guardian's Blade", 'Umbral Glaive', 'Sanguine Blade', 
"Guardian's Hammer", 'Locket of the Iron Solari', "Seeker's Armguard", 'Gargoyle Stoneplate', "Spectre's Cowl", 
"Mikael's Blessing", 'Stealth Ward', 'Farsight Alteration', 'Oracle Lens', 'Your Cut', 'Ardent Censer', 'Essence Reaver', 
'Eye of the Herald', 'Eye of the Herald After', "Kalista's Black Spear", "Kalista's Black Spear After", "Dead Man's Plate", 'Titanic Hydra', 
'Crystalline Bracer', 'Lost Chapter', 'Edge of Night', "Spellthief's Edge", 'Frostfang', 'Shard of True Ice', 
'Steel Shoulderguards', 'Runesteel Spaulders', 'Pauldrons of Whiterock', 'Relic Shield', "Targon's Buckler", 
'Bulwark of the Mountain', 'Spectral Sickle', 'Harrowing Crescent', 'Black Mist Scythe', 'Oblivion Orb', 'Imperial Mandate', 
'Force of Nature', 'The Golden Spatula', 'Horizon Focus', 'Cosmic Drive', 'Blighting Jewel', 'Verdant Barrier', 'Riftmaker', 
'Leeching Leer', 'Night Harvester', 'Demonic Embrace', 'Watchful Wardstone', 'Stirring Wardstone', 'Bandleglass Mirror', 
'Vigilant Wardstone', 'Ironspike Whip', 'Silvermere Dawn', "Death's Dance", 'Chempunk Chainsword', 'Staff of Flowing Water', 
'Moonstone Renewer', 'Goredrinker', 'Stridebreaker', 'Divine Sunderer', "Liandry's Anguish", "Luden's Tempest", 'Everfrost', 
"Bami's Cinder", 'Frostfire Gauntlet', 'Turbo Chemtank', 'Noonquiver', 'Galeforce', 'Kraken Slayer', 'Immortal Shieldbow', 
'Navori Quickblades', 'The Collector', 'Rageknife', 'Duskblade of Draktharr', 'Eclipse', "Prowler's Claw", "Serylda's Grudge", 
"Serpent's Fang"]

itemDf = pd.DataFrame(itemList, index = itemNames)

def getItems():
# Then do this section
    for item in itemList:
        with request.urlopen('http://cdn.merakianalytics.com/riot/lol/resources/latest/en-US/items/'+item+'.json') as response:
            source = response.read()
            data = json.loads(source)

        with open('ItemDataFiles/'+item+'.json', 'w') as f:
            json.dump(data, f, indent = 2, sort_keys = True)

#getItems()

