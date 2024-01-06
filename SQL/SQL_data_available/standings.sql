select l.name as 'League',
    s.season,
    count(s.team_name) as 'teams count',
    s.league_id
from standings s
    left outer join leagues_info l on s.league_id = l.id
group by s.season,
    s.league_id,
    l.name