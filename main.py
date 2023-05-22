from bracket import get_bracket_type
from teams import generate_team

# Example usage
participants = ["Alice", "Bob", "Charlie", "David", "Nita", "Anca", "Teo", "Ana-Maria"]
teams = generate_team(participants)
bracket = get_bracket_type(teams)

# Print the generated teams and bracket
print("Teams:")
for i, team in enumerate(teams):
    print("Team", i + 1, ":", team)

print("\nBracket:")
for round_name, matches in bracket.items():
    print(round_name)
    for match_name, teams in matches.items():
        print(match_name, ":", teams)
