select s.league_country,
    l.name as 'League',
    s.league_season,
    count(s.team_id) as 'team_count',
    count(c.cards_stats_id) as 'cards_stats_count',
    count(f.fixtures_stats_id) as 'cards_stats_count',
    count(g.goals_stats_id) as 'goals_stats_count',
    count(rr.biggest_stats_id) as 'records_stats_count',
    count(ln.lineups_stats_count) as 'lineups_stats_count'
from stats_standings s
    left outer join leagues_info l on s.league_id = l.id
    left outer join stats_standings_cards c on s.cards_stats_id = c.cards_stats_id
    left outer join stats_standings_fixtures f on s.fixtures_stats_id = f.fixtures_stats_id
    left outer join stats_standings_goals g on s.goals_stats_id = g.goals_stats_id
    left outer join stats_standings_records rr on s.records_stats_id = rr.biggest_stats_id
    left outer join (
        select lineups_stats_id,
            count(distinct(stats_id)) as 'lineups_stats_count'
        from stats_standings_lineups
        group by lineups_stats_id
    ) ln on ln.lineups_stats_id = s.lineups_stats_id
group by s.league_country,
    l.name,
    s.league_season