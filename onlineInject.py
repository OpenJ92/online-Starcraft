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
                         BasicCommandEvent, TargetPointEvent, UnitDiedEvent, UnitInitEvent

class Inject():
    def __init__(self, replays):
        self.replays_ = replays

    def run(self):
        for replay in self.replays_:
            #replayMetaData = buildReplayMetaData(replay)
            replayEvents = self.buildEvents(replay)
            #injectIntoDatabase(replayMetaData, replayEvents)

    def buildEvent(self, event):
        # Each event has a participant.
        try:
            return self.eventHASH()[event.name](event)
        except:
            return None
    def buildEvents(self, replay):
        return [self.buildEvent(event) for event in replay.events]

    def buildParticipant(self, user, game):
        return Participant(
                           user = user,
                           game = game,
                           league = user.league,
                           scaled_rating = replay.raw_data['replay.initData']['user_initial_data'][user_index]['scaled_rating'],
                           playrace = replay.players[player_index].playrace,
                           winner == user.name == game.winner
                           )
    def buildUser(self, player, player_index):
        return User(
                    name = player.name,
                    region = player.region,
                    subregion = player.subregion
                    )
    def buildGame(self, replay):
        return Game(
                    name = name = str(replay.date) + '_' + replay.players[0].play_race + ' v ' + replay.players[1].play_race + '_' + replay.players[0].name + ' v ' + replay.players[1].name,
                    map = replay.map_name,
                    game_winner = replay.winner.players[0].name,
                    start_time = replay.start_time,
                    end_time = replay.end_time,
                    category = replay.category,
                    expansion = replay.expansion,
                    time_zone = replay.time_zone
                    )
    def buildPlayerStatsEvent(self, event):
        pass
    def buildUnitBornEvent(self, event):
        pass
    def buildUnitTypeChangeEvent(self, event):
        pass
    def buildUpgradeCompleteEvent(self, event):
        pass
    def buildUnitDoneEvent(self, event):
        pass
    def buildBasicCommandEvent(self, event):
        pass
    def buildTargetPointEvent(self, event):
        pass
    def buildUnitDiedEvent(self, event):
        pass
    def buildUnitInitEvent(self, event):
        pass
    def eventHASH(self):
        return {
            'PlayerStatsEvent' : self.buildPlayerStatsEvent,
            'UnitBornEvent' : self.buildUnitBornEvent,
            'UnitBornEvent' : self.buildUnitBornEvent,
            'UnitTypeChangeEvent' : self.buildUnitTypeChangeEvent,
            'UpgradeCompleteEvent' : self.buildUpgradeCompleteEvent,
            'UnitDoneEvent' : self.buildUnitDoneEvent,
            'BasicCommandEvent' : self.buildBasicCommandEvent,
            'TargetPointEvent' : self.buildTargetPointEvent,
            'UnitDiedEvent' : self.buildUnitDiedEvent,
            'UnitInitEvent' : self.buildUnitInitEvent,
                }

    def checkExistanceUser(replay):
        pass
    def checkExistanceGame(replay):
        pass
    def buildReplayMetaData(self, replay):
        pass
    def injectIntoDataBase(self):
        pass
