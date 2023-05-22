import random
import settings


def generate_team(participants):
    number_participants = settings.NUMBER_PLAYERS_PER_TEAM
    random.shuffle(participants)  # Shuffle the names randomly
    teams = []

    for player in range(0, len(participants), number_participants):
        team = (participants[player], participants[player + 1])
        teams.append(team)

    print("Teams:")
    for i, team in enumerate(teams):
        print("Team", i + 1, ":", team)

    return teams
