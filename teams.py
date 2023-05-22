import settings


def generate_team(participants):
    number_participants = settings.NUMBER_PLAYERS_PER_TEAM
    teams = []
    for player in range(0, len(participants), number_participants):
        team = (participants[player], participants[player + 1])
        teams.append(team)
    return teams
