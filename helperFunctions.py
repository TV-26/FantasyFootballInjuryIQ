def filterHistoricalNFLInjuries(injuries_df, season=None, game_type=None, team=None, week=None, position=None, full_name=None,last_name=None, first_name=None, report_primary_injury=None, report_secondary_injury=None, report_status=None,
                                practice_primary_injury=None, practice_secondary_injury=None, practice_status=None, injured_in_game = None):
    injuries_df_copied = injuries_df.copy()
    if season is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["season"] == season]
    if game_type is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["game_type"] == game_type]
    if team is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["team"] == team]
    if week is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["week"] == week]
    if position is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["position"] == position]
    if full_name is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["full_name"] == full_name]
    if first_name is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["first_name"] == first_name]
    if last_name is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["last_name"] == last_name]
    if report_primary_injury is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["report_primary_injury"] == report_primary_injury]
    if report_secondary_injury is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["report_secondary_injury"] == report_secondary_injury]
    if report_status is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["report_status"] == report_status]
    if practice_primary_injury is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["practice_primary_injury"] == practice_primary_injury]
    if practice_secondary_injury is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["practice_secondary_injury"] == practice_secondary_injury]
    if practice_status is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["practice_status"] == practice_status]
    if injured_in_game is not None:
        injuries_df_copied = injuries_df_copied[injuries_df_copied["InjuredInGame?"] == injured_in_game]
    return injuries_df_copied

