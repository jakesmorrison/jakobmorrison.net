
class Config(object):
    COLUMN_NAMES = "AB,BB,CS,Date,DBO,1B,4B,Games,H,HIDP,HR,PA,Player,R,RBI,SB,Season,2B,SO,3B".split(",")
    COLUMN_NAMES_ORDER = "Season,Date,Player,Games,PA,AB,BB,SO,HIDP,CS,DBO,SB,H,1B,2B,3B,4B,HR,R,RBI".split(",")

    Spring_2016_Roster = "Chance,Grak,Jack,Jake,Josh,Lucas,Mat,Nic,Stubbs,Terry,Ty".split(",")
    Fall_2016_Roster = "Matt,Grak,Jack,Jake,Josh,Lucas,Sean,Nic,Stubbs,Nuggets,Ty".split(",")

    CURRENT_SEASON_ROSTER = Spring_2016_Roster
    CURRENT_SEASON = "2016 Spring"