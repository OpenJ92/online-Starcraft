# User
    # has-one:
    # has-many: Participants
# Participant
    # has-one: Game, User
    # has-many: Events
# Game
    # has-one:
    # has-many: Participants
# Events
    # has-one: Participant
    # has-many:

# ORDER OF CONSTRUCTION:
    # 1) User -- if not yet constructed
    # 2) Game
    # 3) Participant(Game, User)
    # 4) [Event(Participant) for event in EVENTS]

# Game(1) - Participant (A) - User (A)
#             |
#           events ()

# Game(1) - Participant (B) - User (B)
#             |
#           events ()

from createonlineDB import db
import sc2reader
from onlineModels import Participant, User, Game, PlayerStatsEvent, UnitBornEvent, \
                         UnitTypeChangeEvent, UpgradeCompleteEvent, UnitDoneEvent, \
                         BasicCommandEvent, TargetPointCommandEvent, UnitDiedEvent, UnitInitEvent

class Inject():
    def __init__(self, replays):
        self.replays_ = replays
        self.eventHASH_ = self.eventHASH()

    def run(self):
        for replay in self.replays_:
            game, users, participants = self.buildReplayMetaData(replay)
            replayMetaData = {
                 'Participant': {participant.name: participant for participant in participants},
                 'Game': game,
                 'Users': {user.name : user for user in users}
                             }
            # import pdb; pdb.set_trace()
            if False in [False if replayMetaData[element] in [[], {}] else True for element in replayMetaData.keys()]:
                # import pdb; pdb.set_trace()
                pass
            else:
                replayEvents = [event for event in self.buildEvents(replay, replayMetaData) if event != None]
                # import pdb; pdb.set_trace()
                self.injectIntoDataBase(game, users, participants, replayEvents)

    def buildEvent(self, event, replayMetaData):
        try:
            constructed_event = self.eventHASH()[event.name](event, replayMetaData)
            return constructed_event
        except Exception as e:
            # print('buildEvent -', e)
            pass
    def buildEvents(self, replay, replayMetaData):
        return [self.buildEvent(event, replayMetaData) for event in replay.events if event.name in self.eventHASH().keys()]


    def buildPlayerStatsEvent(self, event, replayMetaData):
        # import pdb; pdb.set_trace()
        participant_name  = event.player.name
        return PlayerStatsEvent(
             participant = replayMetaData['Participant'][participant_name],
             name = event.name,
             second = event.second,
             minerals_current = event.minerals_current,
             vespene_current = event.vespene_current,
             minerals_collection_rate = event.minerals_collection_rate,
             vespene_collection_rate = event.vespene_collection_rate,
             workers_active_count = event.workers_active_count,
             minerals_used_in_progress_army = event.minerals_used_in_progress_army,
             minerals_used_in_progress_economy = event.minerals_used_in_progress_economy,
             minerals_used_in_progress_technology = event.minerals_used_in_progress_technology,
             minerals_used_in_progress = event.minerals_used_in_progress,
             vespene_used_in_progress_army = event.vespene_used_in_progress_army,
             vespene_used_in_progress_economy = event.vespene_used_in_progress_economy,
             vespene_used_in_progress_technology = event.vespene_used_in_progress_technology,
             vespene_used_in_progress = event.vespene_used_in_progress,
             resources_used_in_progress = event.resources_used_in_progress,
             minerals_used_current_army = event.minerals_used_current_army,
             minerals_used_current_economy = event.minerals_used_current_economy,
             minerals_used_current_technology = event.minerals_used_current_technology,
             minerals_used_current = event.minerals_used_current,
             vespene_used_current_army = event.vespene_used_current_army,
             vespene_used_current_economy = event.vespene_used_current_economy,
             vespene_used_current_technology = event.vespene_used_current_technology,
             vespene_used_current = event.vespene_used_current,
             resources_used_current = event.resources_used_current,
             minerals_lost_army = event.minerals_lost_army,
             minerals_lost_economy = event.minerals_lost_economy,
             minerals_lost_technology = event.minerals_lost_technology,
             minerals_lost = event.minerals_lost,
             vespene_lost_army = event.vespene_lost_army,
             vespene_lost_economy = event.vespene_lost_economy,
             vespene_lost_technology = event.vespene_lost_technology,
             vespene_lost = event.vespene_lost,
             resources_lost = event.resources_lost,
             minerals_killed_army = event.minerals_killed_army,
             minerals_killed_economy = event.minerals_killed_economy,
             minerals_killed_technology = event.minerals_killed_technology,
             minerals_killed = event.minerals_killed,
             vespene_killed_army = event.vespene_killed_army,
             vespene_killed_economy = event.vespene_killed_economy,
             vespene_killed_technology = event.vespene_killed_technology,
             vespene_killed = event.vespene_killed,
             resources_killed = event.resources_killed,
             food_used = event.food_used,
             food_made = event.food_made,
             minerals_used_active_forces = event.minerals_used_active_forces,
             vespene_used_active_forces = event.vespene_used_active_forces,
             ff_minerals_lost_army = event.ff_minerals_lost_army,
             ff_minerals_lost_economy = event.ff_minerals_lost_economy,
             ff_minerals_lost_technology = event.ff_minerals_lost_technology,
             ff_vespene_lost_army = event.ff_vespene_lost_army,
             ff_vespene_lost_economy = event.ff_vespene_lost_economy,
             ff_vespene_lost_technology = event.ff_vespene_lost_technology
                           )
    def buildUnitBornEvent(self, event, replayMetaData):
        # import pdb; pdb.set_trace()
        particiapnt_name = event.unit_controller.name
        return UnitBornEvent(
              participant = replayMetaData['Participant'][participant_name],
              name = event.name,
              second = event.second,
              unit_type_name = event.unit_type_name,
              loc_x = event.x,
              loc_y = event.y
                            )
    def buildUnitTypeChangeEvent(self, event, replayMetaData):
        # import pdb; pdb.set_trace()
        participant_name = event.unit.owner.name
        return UnitTypeChangeEvent(
            participant = replayMetaData['Participant'][participant_name],
            name = event.name,
            second = event.second,
            unit = event.unit.name,
            unit_type_name = event.unit_type_name
            )
    def buildUpgradeCompleteEvent(self, event, replayMetaData):
        # import pdb; pdb.set_trace()
        participant_name = event.player.name
        return UpgradeCompleteEvent(
             participant = replayMetaData['Participant'][participant_name],
             name = event.name,
             second = event.second,
             upgrade_type_name = event.upgrade_type_name
             )
    def buildUnitDoneEvent(self, event, replayMetaData):
        # import pdb; pdb.set_trace()
        participant_name = event.unit.owner.name
        return UnitDoneEvent(
            participant = replayMetaData['Participant'][participant_name],
            name = event.name,
            second = event.second,
            unit = event.unit.name
            )
    def buildBasicCommandEvent(self, event, replayMetaData):
        # import pdb; pdb.set_trace()
        participant_name = event.player.name
        return BasicCommandEvent(
            participant = replayMetaData['Participant'][participant_name],
            name = event.name,
            second = event.second,
            ability_name = event.ability_name
            )
    def buildTargetPointCommandEvent(self, event, replayMetaData):
        # import pdb; pdb.set_trace()
        participant_name = event.player.name
        return TargetPointCommandEvent(
             participant = replayMetaData['Participant'][participant_name],
             name = event.name,
             second = event.second,
             ability_name = event.ability_name,
             loc_x = event.x,
             loc_y = event.y
             )
    def buildUnitDiedEvent(self, event, replayMetaData):
        # import pdb; pdb.set_trace()
        participant_name = event.killing_player.name
        return UnitDiedEvent(
              participant = replayMetaData['Participant'][participant_name],
              name = event.name,
              second = event.second,
              killing_unit = event.killing_unit.name,
              unit = event.unit.name,
              loc_x = event.x,
              loc_y = event.y
              )
    def buildUnitInitEvent(self, event, replayMetaData):
        # import pdb; pdb.set_trace()
        participant_name = event.unit_controller.name
        return UnitInitEvent(
              participant = replayMetaData['Participant'][participant_name],
              name = event.name,
              second = event.second,
              unit_type_name = event.unit_type_name,
              loc_x = event.x,
              loc_y = event.y
              )
    def eventHASH(self):
        return {
            'PlayerStatsEvent' : self.buildPlayerStatsEvent,
            'UnitBornEvent' : self.buildUnitBornEvent,
            'UnitTypeChangeEvent' : self.buildUnitTypeChangeEvent,
            'UpgradeCompleteEvent' : self.buildUpgradeCompleteEvent,
            'UnitDoneEvent' : self.buildUnitDoneEvent,
            'BasicCommandEvent' : self.buildBasicCommandEvent,
            'TargetPointCommandEvent' : self.buildTargetPointCommandEvent,
            'UnitDiedEvent' : self.buildUnitDiedEvent,
            'UnitInitEvent' : self.buildUnitInitEvent,
                }

    def buildParticipant(self, user, game, player):
        # import pdb; pdb.set_trace()
        return Participant(
           name = user.name,
           user = [user],
           game = [game],
           playrace = player.play_race,
           winner = user.name == game.game_winner
           )
    def buildUser(self, player):
        # import pdb; pdb.set_trace()
        return User(
            name = player.name,
            region = player.region,
            subregion = player.subregion
            )
    def queryUser(self, id):
        # import pdb; pdb.set_trace()
        return db.session.query(User).filter_by(id = id).first()
    def buildGame(self, replay):
        # import pdb; pdb.set_trace()
        return Game(
            name = str(replay.date) + '_' + replay.players[0].play_race + ' v ' + replay.players[1].play_race + '_' + replay.players[0].name + ' v ' + replay.players[1].name,
            map = replay.map_name,
            game_winner = replay.winner.players[0].name,
            start_time = replay.start_time,
            end_time = replay.end_time,
            category = replay.category,
            expansion = replay.expansion,
            time_zone = replay.time_zone
            )

    def checkExistanceUser(self, player):
        # import pdb; pdb.set_trace()
        return db.session.query(User.id).filter(User.name == player.name).first()
    def checkExistanceGame(self, replay):
        # import pdb; pdb.set_trace()
        return db.session.query(Game.id).filter(Game.name == str(replay.date) + '_' + replay.players[0].play_race + ' v ' + replay.players[1].play_race + '_' + replay.players[0].name + ' v ' + replay.players[1].name).first()

### Rethink how to carry out this function. We really need to reconsider how we're building this functionself.
### Currently, I'm having a difficult time debugging currently.

    def buildReplayMetaData(self, replay):
        try:
            if not self.checkExistanceGame(replay):
                game = self.buildGame(replay)
            else:
                return [], [], []
            users, participants = [], []
            for player in replay.players:
                # import pdb; pdb.set_trace()
                id_ = self.checkExistanceUser(player)
                user = self.buildUser(player) if not id_ else self.queryUser(id_[0])
                participant = self.buildParticipant(user, game, player)
                users.append(user)
                participants.append(participant)
            return [game], users, participants
        except Exception as e:
            # print('buildReplayMetaData - ', e)
            return [], [], []
    def injectIntoDataBase(self, game, users, participants, replayEvents):
        try:
            print(game, users)
        except:
            pass
        #import pdb; pdb.set_trace()
        db.session.add_all(game + users + participants + replayEvents)
        db.session.commit()

if __name__ == '__main__':
    pass
