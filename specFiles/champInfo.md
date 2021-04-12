# Champion Data

## Summary
This file is meant to be a key for all the different variables in a champion's json file.


Every variable will be listed below. Variables will either have an example or more bullet points that are sub-variables within the variable. An example is that the stats variable has sub-variables, and those variables have sub-variables that have the actual value.

## Variables
* id: this is the id assigned to a champion by the Riot API
* key: how you find the champ in the API
* name: champion's name
* title: every champion has something they're known as
    * Ex: Ezreal is "the Prodigal Explorer" and Lux is "the Lady of Luminosity"
* fullname: some champions have a first and last name and some do not
    * Ex: Lux is "Luxanna Crownguard" and Ezreal is just ""
* icon: url for the champion's icon in the Riot API data dragon
* resource: what the champion spends to cast spells or secondary thing
    * Ex: Rumble has heat, Akali has energy, Garen has nothing, and most champs have mana
* attackType: this is usually melee or ranged for how a champion attacks other champions
* adaptiveType: this is physical or magic damage
* stats: Every stat has a flat number, percent, perlevel, and percentPerLevel
    * health: total health that a champion has and how much they gain per level
    * healthRegen: amount the champion gains back in health per second
    * mana: this is the resource management stat
    * manaRegen: also works with resource management
    * armor
    * magicResistance
    * attackDamage
    * movespeed
    * Radius stats: their are 4 radius stats that deal with movement
    * Critical: their are 2 stats that deal with how much a crit does
    * attackSpeed: how fast a champion attacks
    * attackSpeedRatio: this deals with attack speed growth
    * Attack Time: their are 3 stats that deal with casting an auto attack
    * Every champion also has a spot for other game mode modifiers like aram and urf
* roles: The type of role that a champion is supposed to fulfill
    * Example: Akali is a Battlemage, Fighter, and mage
* attributeRatings: there are the numbers assigned in the overview for the graphics
* Abilities: Every champion has a passive, q, w, e, and r ability that are their own sub-variable that contains the following data
    * name
    * icon
    * effects: this is even more broken down to have the following
        * description: what the ability does
        * leveling: this deals with all the different ways an ability changes as it gets points put into it
            * attribute: everything an ability does has an attribute. The more different stuff an ability does, then the more attributes it has. Evey attribute has the following
            * modifiers: this is coupled with the attribute and is broken down further by values and units.
    * targeting: how the ability gets targeted at champions
    * affects: does the ability affect allies or enemies or other?
    * spellshieldable: can a spell shield block it
    * resource: what the ability uses
    * spellEffects
    * projectile: the kind of projectile it is
    * onHitEffects: does it have these
    * occurrence
    * notes: things that Riot has noted about the ability
    * blurb: this is the description in the client on the abilities page
    * missileSpeed
    * rechargeRate
    * collisionRadius
    * tetherRadius
    * onTargetCdStatic
    * innerRadius
    * speed
    * width
    * angle
    * castTime
    * effectRadius
    * targetRange
* releaseDate: when the champion was released, year-month-day
* releasePatch: season.something.something.something
* patchLastChanged: last time the champ had buffs, nerfs, or vfx
* price: this has a blueEssence and rp sub-variable
* lore: story about the character  