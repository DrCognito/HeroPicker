import json

heroNicks = [
    {"id": "#abaddon", "nicks": []},
    {"id": "#alchemist", "nicks": []},
    {"id": "#ancient_apparition", "nicks": ["aa", "ancient apparition"]},
    {"id": "#antimage", "nicks": ["anti-mage", "anti mage", "am"]},
    {"id": "#arc_warden", "nicks": ["arc warden"]},
    {"id": "#axe", "nicks": []},
    {"id": "#bane", "nicks": []},
    {"id": "#batrider", "nicks": []},
    {"id": "#beastmaster", "nicks": []},
    {"id": "#bloodseeker", "nicks": []},
    {"id": "#bounty_hunter", "nicks": ["bounty hunter"]},
    {"id": "#brewmaster", "nicks": ["brew", "brew master", "bm"]},
    {"id": "#bristleback", "nicks": ["bb", "bristle"]},
    {"id": "#broodmother", "nicks": ["brood", "brood mother"]},
    {"id": "#centaur", "nicks": ["centaur"]},
    {"id": "#chaos_knight", "nicks": ["chaos knight"]},
    {"id": "#chen", "nicks": ["chen"]},
    {"id": "#clinkz", "nicks": ["clinkz"]},
    {"id": "#clockwerk", "nicks": ["clock"]},
    {"id": "#crystal_maiden", "nicks": ["cm", "crystal maiden"]},
    {"id": "#dark_willow", "nicks": ["dark willow", "dw"]},
    {"id": "#dark_seer", "nicks": ["dark seer", "ds"]},
    {"id": "#dazzle", "nicks": ["dazzle"]},
    {"id": "#death_prophet", "nicks": ["death prophet", "dp"]},
    {"id": "#disruptor", "nicks": []},
    {"id": "#doom", "nicks": []},
    {"id": "#dragon_knight", "nicks": ["dk", "dargon knight"]},
    {"id": "#drow_ranger", "nicks": ["drow ranger"]},
    {"id": "#earth_spirit", "nicks": ["earth spirit"]},
    {"id": "#earthshaker", "nicks": ["earth shaker"]},
    {"id": "#elder_titan", "nicks": ["et", "elder titan"]},
    {"id": "#ember_spirit", "nicks": ["ember"]},
    {"id": "#enchantress", "nicks": ["ench"]},
    {"id": "#enigma", "nicks": []},
    {"id": "#faceless_void", "nicks": ["faceless void", "void"]},
    {"id": "#gyrocopter", "nicks": []},
    {"id": "#huskar", "nicks": []},
    {"id": "#invoker", "nicks": []},
    {"id": "#wisp", "nicks": ["io"]},
    {"id": "#jakiro", "nicks": []},
    {"id": "#juggernaut", "nicks": ["jugger"]},
    {"id": "#keeper_of_the_light", "nicks": ["kotl", "keeper of the light"]},
    {"id": "#kunkka", "nicks": ["kunka"]},
    {"id": "#legion_commander", "nicks": ["lc"]},
    {"id": "#leshrac", "nicks": []},
    {"id": "#lich", "nicks": []},
    {"id": "#lifestealer", "nicks": []},
    {"id": "#lina", "nicks": []},
    {"id": "#lion", "nicks": []},
    {"id": "#lone_druid", "nicks": ["lone druid"]},
    {"id": "#luna", "nicks": []},
    {"id": "#lycan", "nicks": []},
    {"id": "#magnus", "nicks": []},
    {"id": "#medusa", "nicks": []},
    {"id": "#meepo", "nicks": []},
    {"id": "#mirana", "nicks": []},
    {"id": "#monkey_king", "nicks": ["mk"]},
    {"id": "#morphling", "nicks": []},
    {"id": "#naga_siren", "nicks": ["naga siren"]},
    {"id": "#natures_prophet", "nicks": ["furion", "natures prophet"]},
    {"id": "#necrophos", "nicks": []},
    {"id": "#night_stalker", "nicks": ["ns", "night stalker"]},
    {"id": "#nyx_assassin", "nicks": ["nyx assassin"]},
    {"id": "#ogre_magi", "nicks": ["ogre magi"]},
    {"id": "#omniknight", "nicks": []},
    {"id": "#oracle", "nicks": []},
    {"id": "#outworld_devourer", "nicks": ["od", "outworld devourer"]},
    {"id": "#pangolier", "nicks": []},
    {"id": "#phantom_assassin", "nicks": ["pa", "phantom assassin"]},
    {"id": "#phantom_lancer", "nicks": ["phantom lancer", "pl"]},
    {"id": "#phoenix", "nicks": []},
    {"id": "#puck", "nicks": []},
    {"id": "#pudge", "nicks": []},
    {"id": "#pugna", "nicks": []},
    {"id": "#queenofpain", "nicks": ["qop", "qwop"]},
    {"id": "#razor", "nicks": []},
    {"id": "#riki", "nicks": []},
    {"id": "#rubick", "nicks": []},
    {"id": "#sand_king", "nicks": ["sand king", "sk"]},
    {"id": "#shadow_demon", "nicks": ["shadow demon", "sd"]},
    {"id": "#shadow_fiend", "nicks": ["shadow fiend", "shadowfiend", "sf"]},
    {"id": "#shadow_shaman", "nicks": ["shadow shaman", "rasta"]},
    {"id": "#silencer", "nicks": []},
    {"id": "#skywrath_mage", "nicks": ["skywrath mage"]},
    {"id": "#slardar", "nicks": []},
    {"id": "#slark", "nicks": []},
    {"id": "#sniper", "nicks": []},
    {"id": "#spectre", "nicks": []},
    {"id": "#spirit_breaker", "nicks": ["spirit breaker"]},
    {"id": "#storm_spirit", "nicks": ["storm spirit"]},
    {"id": "#sven", "nicks": []},
    {"id": "#techies", "nicks": []},
    {"id": "#templar_assassin", "nicks": ["templar assassin"]},
    {"id": "#terrorblade", "nicks": []},
    {"id": "#tidehunter", "nicks": ["tide", "tidehunter", "th"]},
    {"id": "#timbersaw", "nicks": []},
    {"id": "#tinker", "nicks": []},
    {"id": "#tiny", "nicks": []},
    {"id": "#treant", "nicks": []},
    {"id": "#troll_warlord", "nicks": ["troll warlord"]},
    {"id": "#tusk", "nicks": []},
    {"id": "#underlord", "nicks": []},
    {"id": "#undying", "nicks": []},
    {"id": "#ursa", "nicks": []},
    {"id": "#vengefulspirit", "nicks": ["vengeful spirit"]},
    {"id": "#venomancer", "nicks": []},
    {"id": "#viper", "nicks": []},
    {"id": "#visage", "nicks": []},
    {"id": "#warlock", "nicks": []},
    {"id": "#weaver", "nicks": []},
    {"id": "#windrunner", "nicks": ["wind runner"]},
    {"id": "#winter_wyvern", "nicks": ["winter wyvern"]},
    {"id": "#witch_doctor", "nicks": ["witch doctor"]},
    {"id": "#wraith_king", "nicks": ["wraith king", "skeleton king"]},
    {"id": "#zeus", "nicks": []},
]

jsonOut = heroNicks
with open('heroSearch.json', 'w') as outfile:
    json.dump(jsonOut, outfile)


