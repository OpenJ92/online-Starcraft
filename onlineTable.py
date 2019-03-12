# this class will take in a query of the database and construct a pd.DataFrame
# or numpy.ndarray fo the queried informationself.

# Note: Be sure to start pulling in replays from previous project. ie ~/Personal_Project/Starcraft_2/sc2reader/SCReplays
from onlineModels import db
from onlineModels import Participant, User, Game, PlayerStatsEvent, UnitBornEvent, \
                         UnitTypeChangeEvent, UpgradeCompleteEvent, UnitDoneEvent, \
                         BasicCommandEvent, TargetPointCommandEvent, UnitDiedEvent, UnitInitEvent


class Table():
    def __init__(self):
        pass

    # look to add unit died event measure to these tables.
    def event_Dictionary(self):
        UBE_t = ['Banshee', 'Cyclone', 'Marine', 'Medivac', 'Raven', 'Reaper',
                'SiegeTank', 'VikingFighter', 'Hellion', 'Liberator', 'Thor',
                'Marauder', 'WidowMine', 'HellionTank', 'Battlecruiser', 'Ghost', 'SCV']
        UBE_z = ['Roach', 'Baneling', 'Mutalisk', 'Queen', 'Zergling', 'Corruptor',
                'Hydralisk', 'Viper', 'Ultralisk', 'Drone', 'Overlord']
        UBE_p = ['Stalker', 'Colossus', 'Disruptor', 'Immortal', 'WarpPrism',
                 'Observer', 'Adept', 'Phoenix', 'Oracle', 'Zealot', 'Sentry',
                 'Tempest', 'Carrier', 'VoidRay', 'Archon', 'Mothership', 'HighTemplar', 'Probe']

        PSE_coldrop = ['name', 'player', '_sa_instance_state']

        TPE_t = ['BuildArmory', 'BuildBarracks', 'BuildBarracksReactor', 'BuildBarracksTechLab',
                 'BuildCommandCenter', 'BuildEngineeringBay', 'BuildFactory', 'BuildFactoryTechLab',
                 'BuildMissileTurret', 'BuildSensorTower', 'BuildStarport', 'BuildStarportReactor',
                 'BuildStarportTechLab', 'BuildSupplyDepot', 'BuildFactoryReactor', 'BuildBunker',
                 'BuildFusionCore', 'BuildGhostAcademy']
        TPE_z = ['BuildHatchery', 'BuildRoachWarren', 'BuildSpawningPool', 'BuildBanelingNest',
                 'BuildCreepTumor', 'BuildEvolutionChamber', 'BuildSpire', 'BuildSporeCrawler',
                 'BuildHydraliskDen', 'BuildInfestationPit', 'BuildSpineCrawler',
                 'BuildUltraliskCavern', 'BuildNydusNetwork', 'BuildLurkerDenMP']
        TPE_p = ['BuildCyberneticsCore', 'BuildDarkShrine', 'BuildForge', 'BuildGateway',
                 'BuildNexus', 'BuildPylon', 'BuildShieldBattery', 'BuildTemplarArchive',
                 'BuildTwilightCouncil', 'BuildRoboticsBay', 'BuildRoboticsFacility',
                 'BuildStargate', 'BuildPhotonCannon', 'BuildFleetBeacon']

        UDE_t = ['Armory', 'Barracks', 'BarracksReactor', 'EngineeringBay', 'Factory',
                 'FactoryTechLab', 'MissileTurret', 'OrbitalCommand', 'PlanetaryFortress',
                 'Refinery', 'SensorTower', 'Starport', 'StarportReactor', 'StarportTechLab',
                 'BarracksTechLab', 'CommandCenter', 'FactoryReactor', 'Bunker', 'FusionCore', 'GhostAcademy']
        UDE_z = ['Hatchery', 'RoachWarren', 'SpawningPool', 'BanelingNest', 'EvolutionChamber',
                 'Spire', 'GreaterSpire', 'HydraliskDen', 'InfestationPit', 'SpineCrawler',
                 'SporeCrawler', 'UltraliskCavern', 'Lair', 'NydusNetwork', 'Hive', 'CreepTumorQueen',
                 'CreepTumor', 'LurkerDen']
        UDE_p = ['CyberneticsCore', 'DarkShrine', 'Forge', 'Nexus', 'ShieldBattery', 'TemplarArchive',
                 'TwilightCouncil', 'WarpGate', 'RoboticsBay', 'RoboticsFacility', 'Stargate',
                 'PhotonCannon', 'FleetBeacon', 'Gateway']

        BCE_t = ['BuildSiegeTank', 'TrainBanshee', 'TrainCyclone', 'TrainLiberator', 'TrainMarine',
                 'TrainMedivac', 'TrainRaven', 'TrainReaper', 'TrainViking', 'BuildHellion', 'BuildThor',
                 'TrainMarauder', 'BuildWidowMine', 'TrainBattlecruiser', 'TrainGhost', 'BuildBattleHellion',
                 'TrainNuke', 'TrainSCV']
        BCE_z = ['MorphRoach', 'MorphToRavager', 'MorphMutalisk', 'MorphToOverseer', 'MorphZergling',
                 'TrainBaneling', 'TrainQueen', 'MorphCorruptor', 'MorphHydralisk', 'MorphInfestor',
                 'MorphSwarmHost', 'MorphToBroodLord', 'MorphViper', 'MorphUltralisk', 'TrainDrone']
        BCE_p = ['TrainStalker', 'TrainColossus', 'TrainDisruptor', 'TrainImmortal', 'TrainObserver',
                 'TrainWarpPrism', 'TrainAdept', 'TrainZealot', 'TrainOracle', 'TrainPhoenix',
                 'TrainSentry', 'TrainTempest', 'TrainCarrier', 'TrainVoidRay', 'TrainMothership',
                 'TrainInterceptor', 'TrainProbe']

        return {'UBE': {'Terran': UBE_t,'Zerg': UBE_z,'Protoss': UBE_p, 'event_column': 'unit_type_name'},
                'TPE': {'Terran': TPE_t,'Zerg': TPE_z,'Protoss': TPE_p, 'event_column': 'ability_name'},
            'UDE': {'Terran': UDE_t,'Zerg': UDE_z,'Protoss': UDE_p, 'event_column': 'unit'},
            'BCE': {'Terran': BCE_t,'Zerg': BCE_z,'Protoss': BCE_p, 'event_column': 'ability_name'},
            'drop_add': ['participant_id', 'second']}

    def unique_event_names(self):
        event_dictionary_ = self.event_Dictionary()
        return {'UBE': event_dictionary_['UBE']['Terran'] + event_dictionary_['UBE']['Zerg'] + event_dictionary_['UBE']['Protoss'],
                'TPE': event_dictionary_['TPE']['Terran'] + event_dictionary_['TPE']['Zerg'] + event_dictionary_['TPE']['Protoss'],
                'UDE': event_dictionary_['UDE']['Terran'] + event_dictionary_['UDE']['Zerg'] + event_dictionary_['UDE']['Protoss'],
                'BCE': event_dictionary_['BCE']['Terran'] + event_dictionary_['BCE']['Zerg'] + event_dictionary_['BCE']['Protoss']}



    def query(self):
        pass

    def create_table(self):
        pass

if __name__ == '__main__':
    pass
