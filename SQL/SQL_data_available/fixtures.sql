select league_country,
    league_name,
    league_season,
    count(fixture_id) as 'count fixtures',
    count(distinct(teams_home_id)) as 'home_teams_count',
    count(distinct(teams_away_id)) as 'away_teams_count'
from fixtures f
group by league_country,
    league_name,
    league_season