         logger.warning("Пустой список скоров в find_lost_scores")
         return []
 
    groups = {}
     for rec in scores:
         try:
                                                       
            if not all(key in rec for key in ["beatmap_id", "mods", "pp", "total_score"]):
                 logger.warning(f"Скор не содержит все необходимые ключи: {rec.keys()}")
                 continue
 
             key = (rec["beatmap_id"], tuple(rec["mods"]))
             groups.setdefault(key, []).append(rec)
         except Exception as e:
             if len(recs) < 2:
                 continue
 
            if not all(isinstance(s.get("pp", 0), (int, float)) for s in recs):
                logger.warning(f"Недопустимое значение PP в скорах: {[s.get('pp') for s in recs]}")
                continue

            if not all(isinstance(s.get("total_score", 0), (int, float)) for s in recs):
                logger.warning(f"Недопустимое значение total_score в скорах")
                continue

            best_pp = max(recs, key=lambda s: float(s.get("pp", 0)))
            best_total = max(recs, key=lambda s: int(s.get("total_score", 0)))
 
             if not all(k in best_pp for k in ["total_score", "pp", "beatmap_id"]):
                 logger.warning(f"best_pp не содержит необходимые ключи")
                 logger.warning(f"best_total не содержит необходимые ключи")
                 continue
 
            pp_better = float(best_pp["pp"]) > float(best_total["pp"])
            score_worse = int(best_pp["total_score"]) < int(best_total["total_score"])
 
             if score_worse and pp_better:
                 bid = best_pp["beatmap_id"]
 
     lost_results = []
     map_scores = {}
    for rec in scores:
        if "beatmap_id" not in rec:
            continue
         map_scores.setdefault(rec["beatmap_id"], []).append(rec)
 
     for bid, candidates in possible_lost.items():
         try:
             if not candidates:
                 continue
 
            candidate = max(candidates, key=lambda s: float(s.get("pp", 0)))
             all_scores = map_scores.get(bid, [])
 
             if not all_scores:
                 continue
 
            best_score = max(all_scores, key=lambda s: float(s.get("pp", 0)))
 
            if float(candidate.get("pp", 0)) >= float(best_score.get("pp", 0)):
                 lost_results.append(candidate)
         except Exception as e:
             logger.warning(f"Ошибка при обработке потенциально потерянного скора: {e}")
             continue
 
     try:
        lost_results.sort(key=lambda s: float(s.get("pp", 0)), reverse=True)
     except Exception as e:
         logger.warning(f"Ошибка при сортировке результатов: {e}")
 
     return lost_results
 

 def parse_top(raw, token):
     def format_date(iso_str):
         if not iso_str:
     if gui_log:
         gui_log("Инициализация...", update_last=True)
 
    db_init()
    token = token_osu()
    user_json = user_osu(user_identifier, lookup_key, token)
    if not user_json:
        gui_log(f"Ошибка: Не удалось получить данные пользователя '{user_identifier}' (тип: {lookup_key}).", False)
        raise ValueError(f"Пользователь не найден: {user_identifier}")
    username = user_json["username"]
    user_id = user_json["id"]

    profile_link = f"https://osu.ppy.sh/users/{user_id}"
    gui_log(f"Найден пользователь: {username} ({profile_link})", False)
 
     songs = os.path.join(game_dir, "Songs")
     replays = os.path.join(game_dir, "Data", "r")
 
     gui_log("Сканирую .osu файлы в Songs: 0%", update_last=True)
     last_songs_update = {"time": 0}
 