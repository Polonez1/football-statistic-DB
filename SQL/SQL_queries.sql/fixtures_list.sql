select fixture_id,
    league_id
from fixtures
where league_name in { leagues }
    and league_season in { season }