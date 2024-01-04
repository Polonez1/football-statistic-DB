select fixture_id,
    league_id
from fixtures
where league_name in { leagues }
    and league_season = { season }
    and fixture_status_elapsed not in ('TBD', 'NS')