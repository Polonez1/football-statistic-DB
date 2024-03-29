av_countries_col = ["name", "code", "flag", "source", "created_by", "updated_at"]
av_season_col = ["available_seasons", "source", "created_by", "updated_at"]
leagues_info_col = [
    "id",
    "name",
    "type",
    "logo",
    "country_name",
    "country_code",
    "country_flag",
    "leagues_seasons_id",
    "source",
    "created_by",
    "updated_at",
]
leagues_additional_col = [
    "leagues_seasons_id",
    "seasons_year",
    "seasons_start",
    "seasons_end",
    "seasons_current",
    "seasons_coverage_fixtures_events",
    "seasons_coverage_fixtures_lineups",
    "seasons_coverage_fixtures_statistics_fixtures",
    "seasons_coverage_fixtures_statistics_players",
    "seasons_coverage_standings",
    "seasons_coverage_players",
    "seasons_coverage_top_scorers",
    "seasons_coverage_top_assists",
    "seasons_coverage_top_cards",
    "seasons_coverage_injuries",
    "seasons_coverage_predictions",
    "seasons_coverage_odds",
    "source",
    "created_by",
    "updated_at",
]
venue_col = [
    "id",
    "name",
    "address",
    "city",
    "country",
    "capacity",
    "surface",
    "image",
    "source",
    "created_by",
    "updated_at",
]
teams_col = [
    "id",
    "name",
    "code",
    "country",
    "founded",
    "national",
    "logo",
    "venue_id",
    "source",
    "created_by",
    "updated_at",
]
standings_col = [
    "id",
    "league_id",
    "season",
    "team_name",
    "team_id",
    "rank",
    "points",
    "goalsDiff",
    "group",
    "form",
    "status",
    "description",
    "team_logo",
    "all_played",
    "all_win",
    "all_draw",
    "all_lose",
    "all_goals_for",
    "all_goals_against",
    "home_played",
    "home_win",
    "home_draw",
    "home_lose",
    "home_goals_for",
    "home_goals_against",
    "away_played",
    "away_win",
    "away_draw",
    "away_lose",
    "away_goals_for",
    "away_goals_against",
    "stats_id",
    "source",
    "created_by",
    "updated_at",
]
stats_standings_col = [
    "stats_id",
    "fixtures_stats_id",
    "goals_stats_id",
    "records_stats_id",
    "lineups_stats_id",
    "cards_stats_id",
    "league_id",
    "league_country",
    "league_season",
    "team_id",
    "team_name",
    "clean_sheet_home",
    "clean_sheet_away",
    "clean_sheet_total",
    "failed_to_score_home",
    "failed_to_score_away",
    "failed_to_score_total",
    "penalty_total",
    "penalty_scored_total",
    "penalty_scored_percentage",
    "penalty_missed_total",
    "penalty_missed_percentage",
    "form",
]
stats_standings_cards_col = [
    "cards_stats_id",
    "stats_id",
    "season",
    "league_id",
    "team_id",
    "cards_yellow_0-15_total",
    "cards_yellow_0-15_percentage",
    "cards_yellow_16-30_total",
    "cards_yellow_16-30_percentage",
    "cards_yellow_31-45_total",
    "cards_yellow_31-45_percentage",
    "cards_yellow_46-60_total",
    "cards_yellow_46-60_percentage",
    "cards_yellow_61-75_total",
    "cards_yellow_61-75_percentage",
    "cards_yellow_76-90_total",
    "cards_yellow_76-90_percentage",
    "cards_yellow_91-105_total",
    "cards_yellow_91-105_percentage",
    "cards_yellow_106-120_total",
    "cards_yellow_106-120_percentage",
    "cards_red_0-15_total",
    "cards_red_0-15_percentage",
    "cards_red_16-30_total",
    "cards_red_16-30_percentage",
    "cards_red_31-45_total",
    "cards_red_31-45_percentage",
    "cards_red_46-60_total",
    "cards_red_46-60_percentage",
    "cards_red_61-75_total",
    "cards_red_61-75_percentage",
    "cards_red_76-90_total",
    "cards_red_76-90_percentage",
    "cards_red_91-105_total",
    "cards_red_91-105_percentage",
    "cards_red_106-120_total",
    "cards_red_106-120_percentage",
    # "cards_yellow__total",
    # "cards_yellow__percentage",
    # "cards_red__total",
    # "cards_red__percentage",
]
stats_standings_fixtures_col = [
    "fixtures_stats_id",
    "stats_id",
    "season",
    "league_id",
    "team_id",
    "fixtures_played_home",
    "fixtures_played_away",
    "fixtures_played_total",
    "fixtures_wins_home",
    "fixtures_wins_away",
    "fixtures_wins_total",
    "fixtures_draws_home",
    "fixtures_draws_away",
    "fixtures_draws_total",
    "fixtures_loses_home",
    "fixtures_loses_away",
    "fixtures_loses_total",
]
stats_standings_goals_col = [
    "goals_stats_id",
    "stats_id",
    "season",
    "league_id",
    "team_id",
    "goals_for_total_home",
    "goals_for_total_away",
    "goals_for_total_total",
    "goals_for_average_home",
    "goals_for_average_away",
    "goals_for_average_total",
    "goals_for_minute_0-15_total",
    "goals_for_minute_0-15_percentage",
    "goals_for_minute_16-30_total",
    "goals_for_minute_16-30_percentage",
    "goals_for_minute_31-45_total",
    "goals_for_minute_31-45_percentage",
    "goals_for_minute_46-60_total",
    "goals_for_minute_46-60_percentage",
    "goals_for_minute_61-75_total",
    "goals_for_minute_61-75_percentage",
    "goals_for_minute_76-90_total",
    "goals_for_minute_76-90_percentage",
    "goals_for_minute_91-105_total",
    "goals_for_minute_91-105_percentage",
    "goals_for_minute_106-120_total",
    "goals_for_minute_106-120_percentage",
    "goals_against_total_home",
    "goals_against_total_away",
    "goals_against_total_total",
    "goals_against_average_home",
    "goals_against_average_away",
    "goals_against_average_total",
    "goals_against_minute_0-15_total",
    "goals_against_minute_0-15_percentage",
    "goals_against_minute_16-30_total",
    "goals_against_minute_16-30_percentage",
    "goals_against_minute_31-45_total",
    "goals_against_minute_31-45_percentage",
    "goals_against_minute_46-60_total",
    "goals_against_minute_46-60_percentage",
    "goals_against_minute_61-75_total",
    "goals_against_minute_61-75_percentage",
    "goals_against_minute_76-90_total",
    "goals_against_minute_76-90_percentage",
    "goals_against_minute_91-105_total",
    "goals_against_minute_91-105_percentage",
    "goals_against_minute_106-120_total",
    "goals_against_minute_106-120_percentage",
]
stats_standings_lineups_col = [
    "lineups_stats_id",
    "stats_id",
    "season",
    "league_id",
    "team_id",
    "lineups_formation",
    "lineups_played",
]
stats_standings_records_col = [
    "biggest_stats_id",
    "stats_id",
    "season",
    "league_id",
    "team_id",
    "biggest_streak_wins",
    "biggest_streak_draws",
    "biggest_streak_loses",
    "biggest_wins_home",
    "biggest_wins_away",
    "biggest_loses_home",
    "biggest_loses_away",
    "biggest_goals_for_home",
    "biggest_goals_for_away",
    "biggest_goals_against_home",
    "biggest_goals_against_away",
]

stats_standings_col_dict = {
    "stats_standings": stats_standings_col,
    "stats_standings_fixtures": stats_standings_fixtures_col,
    "stats_standings_goals": stats_standings_goals_col,
    "stats_standings_records": stats_standings_records_col,
    "stats_standings_lineups": stats_standings_lineups_col,
    "stats_standings_cards": stats_standings_cards_col,
}
fixtures_col = [
    "fixture_id",
    "fixture_referee",
    "fixture_timezone",
    "fixture_date",
    "fixture_timestamp",
    "fixture_periods_first",
    "fixture_periods_second",
    "fixture_venue_id",
    "fixture_venue_name",
    "fixture_venue_city",
    "fixture_status_long",
    "fixture_status_short",
    "fixture_status_elapsed",
    "league_id",
    "league_name",
    "league_country",
    "league_logo",
    "league_flag",
    "league_season",
    "league_round",
    "teams_home_id",
    "teams_home_name",
    "teams_home_logo",
    "teams_home_winner",
    "teams_away_id",
    "teams_away_name",
    "teams_away_logo",
    "teams_away_winner",
    "goals_home",
    "goals_away",
    "score_halftime_home",
    "score_halftime_away",
    "score_fulltime_home",
    "score_fulltime_away",
    "score_extratime_home",
    "score_extratime_away",
    "score_penalty_home",
    "score_penalty_away",
    "source",
    "created_by",
    "updated_at",
]
fixtures_event_col = [
    "fixture_id",
    "type",
    "detail",
    "comments",
    "time_elapsed",
    "time_extra",
    "team_id",
    "team_name",
    "team_logo",
    "player_id",
    "player_name",
    "assist_id",
    "assist_name",
    "source",
    "created_by",
    "updated_at",
]
fixtures_stats_col = [
    "team_id",
    "team_name",
    "team_logo",
    "Shots on Goal",
    "Shots off Goal",
    "Total Shots",
    "Blocked Shots",
    "Shots insidebox",
    "Shots outsidebox",
    "Fouls",
    "Corner Kicks",
    "Offsides",
    "Ball Possession",
    "Yellow Cards",
    "Red Cards",
    "Goalkeeper Saves",
    "Total passes",
    "Passes accurate",
    "Passes %",
    "fixtures_stats_team_id",
    "fixture_id",
    # "expected_goals",
    "source",
    "created_by",
    "updated_at",
]
player_fixture_col = [
    "fixture_id",
    "team_id",
    "team_name",
    "team_logo",
    "team_update",
    "player_id",
    "player_name",
    "player_photo",
    "index",
    "offsides",
    "games_minutes",
    "games_number",
    "games_position",
    "games_rating",
    "games_captain",
    "games_substitute",
    "shots_total",
    "shots_on",
    "goals_total",
    "goals_conceded",
    "goals_assists",
    "goals_saves",
    "passes_total",
    "passes_key",
    "passes_accuracy",
    "tackles_total",
    "tackles_blocks",
    "tackles_interceptions",
    "duels_total",
    "duels_won",
    "dribbles_attempts",
    "dribbles_success",
    "dribbles_past",
    "fouls_drawn",
    "fouls_committed",
    "cards_yellow",
    "cards_red",
    "penalty_won",
    "penalty_commited",
    "penalty_scored",
    "penalty_missed",
    "penalty_saved",
    "source",
    "created_by",
    "updated_at",
]
lineups_info_col = [
    "team_id",
    "team_name",
    "team_logo",
    "coach_id",
    "coach_name",
    "coach_photo",
    "formation",
    "fixture_id",
    "source",
    "created_by",
    "updated_at",
]
lineups_col = [
    "id",
    "name",
    "number",
    "pos",
    "grid",
    "fixture_id",
    "team_id",
    "source",
    "created_by",
    "updated_at",
]
injuries_fixtures_col = [
    "player_id",
    "player_name",
    "player_photo",
    "player_type",
    "player_reason",
    "team_id",
    "team_name",
    "team_logo",
    "fixture_id",
    "fixture_timezone",
    "fixture_date",
    "fixture_timestamp",
    "league_id",
    "league_season",
    "league_name",
    "league_country",
    "league_logo",
    "league_flag",
    "source",
    "created_by",
    "updated_at",
]
squad_col = [
    "id",
    "name",
    "age",
    "number",
    "position",
    "photo",
    "team_id",
    "source",
    "created_by",
    "updated_at",
]
