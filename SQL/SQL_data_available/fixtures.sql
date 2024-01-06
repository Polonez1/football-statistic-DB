select league_country,
    league_name,
    league_season,
    count(f.fixture_id) as 'count fixtures',
    count(distinct(teams_home_id)) as 'home_teams_count',
    count(distinct(teams_away_id)) as 'away_teams_count',
    count(fe.count) as 'event_count',
    count(fs.count) as 'stats_count',
    count(pf.fixture_count) as 'fixture_count_players',
    count(pf.players_count) as 'players_count',
    count(pf.team_id) as 'players_team_count'
from fixtures f
    left outer join (
        select fixture_id,
            count(distinct(fixture_id)) as 'count'
        from fixtures_event
        group by fixture_id
    ) fe on f.fixture_id = fe.fixture_id
    left outer join (
        select fixture_id,
            count(distinct(fixture_id)) as 'count'
        from fixtures_stats
        group by fixture_id
    ) fs on f.fixture_id = fs.fixture_id
    left outer join (
        select fixture_id,
            count(distinct(fixture_id)) as 'fixture_count',
            count(distinct(player_id)) as 'players_count',
            count(distinct(team_id)) as 'team_id'
        from player_fixture
        group by fixture_id
    ) pf on f.fixture_id = pf.fixture_id
group by league_country,
    league_name,
    league_season;