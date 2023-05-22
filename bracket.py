import math


def get_bracket_type(teams):
    nb_teams = len(teams)
    # Multiplier of any power of 2
    if (nb_teams & (nb_teams - 1)) == 0:
        return generate_knockouts_bracket(teams)
    else:
        return generate_group_bracket(teams)


def simulate_match(player1, player2):
    number = input("Enter winner 1 or 2: ")
    if number == "1":
        return player1
    elif number == "2":
        return player2


def generate_knockouts_bracket(teams):
    print("\nBracket:")
    bracket = {}
    num_teams = len(teams)
    print(f"\nNumber of teams: {num_teams}")
    num_rounds = int(math.log(num_teams, 2))

    current_participants = teams

    for round_num in range(num_rounds):
        round_name = "Round " + str(round_num + 1)
        print(round_name)
        next_round = []

        for i in range(0, len(current_participants), 2):

            match_name = "Match " + str(i // 2 + 1)
            participant1 = current_participants[i]
            participant2 = current_participants[i + 1]
            print(f"{match_name} : {participant1} vs {participant2}")

            winner = simulate_match(participant1, participant2)
            next_round.append(winner)
        current_participants = next_round

    winner = current_participants[0]
    print("Overall Winner:", winner)
    return bracket


def generate_group_bracket(teams):
    pass
