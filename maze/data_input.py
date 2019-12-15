from .models import Character, NPCharacter, Monster, Spell, \
    Appearance, Getsup, BodyFeatures, Personality, \
    Background, Habit, Belongings, Features, Weapon, FirstName, LastName, \
    NPCJob, Misfortune, Mission, NPCAim, Weakness, Asset, Method, Secret, \
    Fame, Hobby, Relationship, Divinity, Result, \
    MonsterType, MonsterBodyFeature, MonsterFeature, MonsterAbility, \
    MonsterTactics, MonsterWeakness, MaterialEffect, MaterialElement, \
    MaterialForm, SpiritualEffect, SpiritualElement, SpiritualForm, Mutation, \
    Madness, MagicalDisaster, Book, Potion, MagicMaterial, \
    TreasureFeature, PreciousMaterial, Stuff, CityTopic, CityEvent, \
    AreaTopic, HighClassBuilding, DownstreamBuilding, CityAction, \
    BuildingRoom, StreetTactic, BuildingTactic, Faction, FactionFeature, \
    FactionAim, WildArea, WildTerrain, WildArtifact, WildAreaFeature, \
    WildDiscovery, WildAction, WildThreat, Herb, ToxicPlant, \
    MotelNamePrefix, MotelNameSuffix, MotelUniqueness, \
    DungeonEntrance, DungeonForm, DungeonPlacement, WhyDungeonWasAbandoned, \
    DungeonReward, DungeonAction, DungeonRoom, DungeonRoomDetail, \
    DungeonMechanism, DungeonThreat, TrapEffect, TrapActuation              
import os


def bulk_save():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    f = open(BASE_DIR + "/maze/static/data.txt", 'r')
    while True:
        line = f.readline()
        if not line: 
            break
        obj = TrapActuation() ### data.txt 파일 먼저 변경 하고 실행
        obj.word = line.strip()
        obj.save()
    f.close()
    
