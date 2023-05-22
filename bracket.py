def get_bracket_type(teams):
    nb_teams = len(teams)
    # Multiplier of any power of 2
    if (nb_teams & (nb_teams - 1)) == 0:
        return generate_knockouts_bracket(teams)
    else:
        return generate_group_bracket(teams)


def generate_knockouts_bracket(teams):
    bracket = {}
    num_teams = len(teams)
    num_rounds = int(num_teams / 2)
    for i in range(num_rounds):
        round_name = "Round " + str(i + 1)
        bracket[round_name] = {}
        for j in range(0, len(teams), 2):
            match_name = "Match " + str(j // 2 + 1)
            bracket[round_name][match_name] = (teams[j], teams[j + 1])
            # Each match contains a tuple with two teams
    return bracket


def generate_group_bracket(teams):
    pass
