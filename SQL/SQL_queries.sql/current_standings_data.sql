select season,
    league_id,
    team_id,
    stats_id
from standings
where season = { season }