import settings
from bracket import get_bracket_type
from teams import generate_team

# Generate teams and brackets
teams = generate_team(settings.PARTICIPANTS)
bracket = get_bracket_type(teams)
