# this class will take in a query of the database and construct a pd.DataFrame # or numpy.ndarray fo the queried informationself.

# Note: Be sure to start pulling in replays from previous project. ie ~/Personal_Project/Starcraft_2/sc2reader/SCReplays
from onlineDB.Database.replays.onlineModels import db
from onlineDB.Database.replays.onlineModels import Participant, User, Game, PlayerStatsEvent, UnitBornEvent, \
                         UnitTypeChangeEvent, UpgradeCompleteEvent, UnitDoneEvent, \
                         BasicCommandEvent, TargetPointCommandEvent, UnitDiedEvent, UnitInitEvent
import pandas as pd
import numpy as np

class Table():
    def __init__(self, participant, event):
        self.participant = participant
        self.event = event
        self.table = self.create_table()

    def __getitem__(self, idx):
        pass

    def event_Dictionary(self):
        UBE_t = ['Banshee', 'Cyclone', 'Marine', 'Medivac', 'Raven', 'Reaper',
                'SiegeTank', 'VikingFighter', 'Hellion', 'Liberator', 'Thor',
                'Marauder', 'WidowMine', 'HellionTank', 'Battlecruiser', 'Ghost']
        UBE_z = ["Larva", 'Roach', 'Baneling', 'Mutalisk', 'Queen', 'Zergling', 'Corruptor',
                'Hydralisk', 'Viper', 'Ultralisk']
        UBE_p = ['Stalker', 'Colossus', 'Disruptor', 'Immortal', 'WarpPrism',
                 'Observer', 'Adept', 'Phoenix', 'Oracle', 'Zealot', 'Sentry',
                 'Tempest', 'Carrier', 'VoidRay', 'Archon', 'Mothership', 'HighTemplar']

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

        PSE = ['ff_minerals_lost_army', 'ff_minerals_lost_economy',
               'ff_minerals_lost_technology', 'ff_vespene_lost_army',
               'ff_vespene_lost_economy', 'ff_vespene_lost_technology', 'food_made',
               'food_used', 'id', 'minerals_collection_rate', 'minerals_current',
               'minerals_killed', 'minerals_killed_army', 'minerals_killed_economy',
               'minerals_killed_technology', 'minerals_lost', 'minerals_lost_army',
               'minerals_lost_economy', 'minerals_lost_technology',
               'minerals_used_active_forces', 'minerals_used_current',
               'minerals_used_current_army', 'minerals_used_current_economy',
               'minerals_used_current_technology', 'minerals_used_in_progress',
               'minerals_used_in_progress_army', 'minerals_used_in_progress_economy',
               'minerals_used_in_progress_technology', 'name', 'participant_id',
               'resources_killed', 'resources_lost', 'resources_used_current',
               'resources_used_in_progress', 'second', 'vespene_collection_rate',
               'vespene_current', 'vespene_killed', 'vespene_killed_army',
               'vespene_killed_economy', 'vespene_killed_technology', 'vespene_lost',
               'vespene_lost_army', 'vespene_lost_economy', 'vespene_lost_technology',
               'vespene_used_active_forces', 'vespene_used_current',
               'vespene_used_current_army', 'vespene_used_current_economy',
               'vespene_used_current_technology', 'vespene_used_in_progress',
               'vespene_used_in_progress_army', 'vespene_used_in_progress_economy',
               'vespene_used_in_progress_technology', 'workers_active_count']

        return {'UBE': {'Terran': UBE_t, 'Zerg': UBE_z, 'Protoss': UBE_p, 'event_column': 'unit_type_name'},
                'TPE': {'Terran': TPE_t, 'Zerg': TPE_z, 'Protoss': TPE_p, 'event_column': 'ability_name'},
                'UDE': {'Terran': UDE_t, 'Zerg': UDE_z, 'Protoss': UDE_p, 'event_column': 'unit'},
                'BCE': {'Terran': BCE_t, 'Zerg': BCE_z, 'Protoss': BCE_p, 'event_column': 'ability_name'},
                'drop_add': ['participant_id', 'second']}

    def unique_event_names(self):
        event_dictionary_ = self.event_Dictionary()
        return {'UBE': event_dictionary_['UBE']['Terran'] + event_dictionary_['UBE']['Zerg'] + event_dictionary_['UBE']['Protoss'],
                'TPE': event_dictionary_['TPE']['Terran'] + event_dictionary_['TPE']['Zerg'] + event_dictionary_['TPE']['Protoss'],
                'UDE': event_dictionary_['UDE']['Terran'] + event_dictionary_['UDE']['Zerg'] + event_dictionary_['UDE']['Protoss'],
                'BCE': event_dictionary_['BCE']['Terran'] + event_dictionary_['BCE']['Zerg'] + event_dictionary_['BCE']['Protoss']}

    def create_race_table(self):
        events_ = self.participant.events_(self.event)
        event_Dataframe = pd.DataFrame([vars(event) for event in events_])
        full_Dataframe_dummies = pd.DataFrame(columns = self.event_Dictionary()[self.event][self.participant.playrace])
        event_Dataframe_dummies = pd.get_dummies(event_Dataframe[self.event_Dictionary()[self.event]["event_column"]])
        full_event_Dataframe_dummies = pd.concat([full_Dataframe_dummies, event_Dataframe_dummies], axis = 0, sort = False)[self.event_Dictionary()[self.event][self.participant.playrace]].fillna(0)
        return full_event_Dataframe_dummies

    def create_agg_race_table(self):
        table = self.create_race_table()
        return table.cumsum(axis = 0)

    def create_table(self):
        events_ = self.participant.events_(self.event)
        event_Dataframe = pd.DataFrame([vars(event) for event in events_])
        full_Dataframe_dummies = pd.DataFrame(columns = self.unique_event_names()[self.event])
        event_Dataframe_dummies = pd.get_dummies(event_Dataframe[self.event_Dictionary()[self.event]["event_column"]])
        full_event_Dataframe_dummies = pd.concat([full_Dataframe_dummies, event_Dataframe_dummies], axis = 0, sort = False)[self.unique_event_names()[self.event]].fillna(0)

        return full_event_Dataframe_dummies

    def create_agg_table(self):
        table = self.create_table()
        return table.cumsum(axis = 0)

    def plot_table(self, type_ = "standard"):
        import matplotlib.pyplot as plt
        if type_ == "standard":
            plt.imshow(self.table.values, cmap = "Dark2")
        elif type_ == "agg":
            plt.imshow(self.create_agg_table().values, cmap = "Dark2")
        else:
            return -1;
        plt.ylabel("|Actions|")
        plt.xlabel("Action Space")
        plt.show()

    ## Now that we have our tables constructed, we need to build two modules. First, we need to find the weighted first principle
    ## vector for our events and then, using out hypersphere construction, convert those rectangular coordinates into hyperspherical
    ## coordinates (See hypersphere tab for a functional construction of hyperspheres.). In that theta space is where we will carry 
    ## our our clustering analysis and sample from. We'll also use that space to dictate the actions our AI will take in game. That is
    ## our AI will take action in order to shift its current principle component in the direction of the center of mass that is it's 
    ## desired startegy on theta space.

if __name__ == '__main__':
    print(f"Enter File: {__name__}")
    p = db.session.query(Participant)[8]
    print('Query Complete')
    tUBE = Table(p, "UBE")
    tTPE = Table(p, "TPE")
    tUDE = Table(p, "UDE")
    tBCE = Table(p, "BCE")
    print("Tables Complete")
