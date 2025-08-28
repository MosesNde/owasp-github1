 NOT_SUBMITTED_CACHE = not_submitted_cache_load()
 
 def osr_load():

    if os.path.exists(OSR_CACHE_PATH):
        try:
            with open(OSR_CACHE_PATH, "r", encoding="utf-8") as f:
                content = f.read()
                logger.debug("OSR-кэш (%s): %s", OSR_CACHE_PATH, content[:200])
                f.seek(0)
                return json.load(f)
        except Exception:
            logger.exception("Ошибка чтения OSR-кэша: %s", OSR_CACHE_PATH)
    return {}
 
 def osr_save(cache):

    with open(OSR_CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4)
 
 def md5_load():
 
    if os.path.exists(MD5_CACHE_PATH):
         try:
            with open(MD5_CACHE_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
         except Exception as e:
            logger.warning("Ошибка чтения MD5-кэша: %s", e)
            return {}
    return {}

def md5_save(cache):

    with open(MD5_CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4)
 
 def get_md5(path):
 
         return None
 
 

 def proc_osr(osr_path, md5_map, cutoff, username):

    rep = parse_osr(osr_path)
    if not rep:
        logger.warning("Не удалось обработать osr: %s", osr_path)
        return None
    if rep["game_mode"] != 0:
        return None
    if rep["player_name"].lower() != username.lower():
        return None
    if rep["beatmap_md5"] not in md5_map:

        if rep["beatmap_md5"] in NOT_SUBMITTED_CACHE:
            logger.warning("md5 %s уже отмечен как не найденный, пропускаем реплей: %s", rep["beatmap_md5"], osr_path)
             return None


        from osu_api import lookup_osu
        beatmap_id_api = lookup_osu(rep["beatmap_md5"])
        if beatmap_id_api and beatmap_id_api != 0:

            new_osu_path = download_osu_file(beatmap_id_api)
            if new_osu_path:

                md5_map[rep["beatmap_md5"]] = new_osu_path
                update_osu_md5_cache(new_osu_path, rep["beatmap_md5"])
                logger.info("Скачан новый .osu файл для beatmap_id %s по md5 %s", beatmap_id_api, rep["beatmap_md5"])
             else:
                logger.error("Не удалось скачать .osu файл для beatmap_id %s", beatmap_id_api)
 
                NOT_SUBMITTED_CACHE[rep["beatmap_md5"]] = True
                not_submitted_cache_save(NOT_SUBMITTED_CACHE)
                 return None
        else:
            logger.error("Нет .osu файла для реплея: %s с md5: %s", osr_path, rep["beatmap_md5"])

            NOT_SUBMITTED_CACHE[rep["beatmap_md5"]] = True
            not_submitted_cache_save(NOT_SUBMITTED_CACHE)
            return None
 
    mtime = os.path.getmtime(osr_path)
    with OSR_CACHE_LOCK:
        if osr_path in OSR_CACHE and OSR_CACHE[osr_path].get("mtime") == mtime:
            return OSR_CACHE[osr_path].get("result")

    osu_path = md5_map[rep["beatmap_md5"]]
    res = calculate_pp_rosu(osu_path, rep)
    if res:
        beatmap_id = res.get("beatmap_id")
 
        if beatmap_id == 0:
            return None
 
        elif beatmap_id is None:
            md5 = rep.get("beatmap_md5")
            if md5 is None:
                 return None
 
            if md5 in MD5_BEATMAPID_CACHE:
                res["beatmap_id"] = MD5_BEATMAPID_CACHE[md5]
            else:
                try:
                    from osu_api import lookup_osu
                    new_id = lookup_osu(md5)
                    if new_id is not None:
                        MD5_BEATMAPID_CACHE[md5] = new_id
                        res["beatmap_id"] = new_id
                except Exception as e:
                    logger.error("Ошибка при запросе beatmap_id по md5 (%s): %s", md5, e)

                                                      
        if isinstance(rep, dict):
            if "player_name" in rep:
                res["player_name"] = rep["player_name"]
            if "score_time" in rep:
                res["score_time"] = rep["score_time"]
 
            with OSR_CACHE_LOCK:
                OSR_CACHE[osr_path] = {"mtime": mtime, "result": res}
        else:
            logger.warning(f"Неверный формат реплея для {osr_path}: {type(rep)}")
            return None
    return res
 
 
 def download_osu_file(beatmap_id):
     filename = f"beatmap_{beatmap_id}.osu"
 def update_osu_md5_cache(new_osu_path, md5_hash):
     global MD5_CACHE_PATH
     with MD5_CACHE_LOCK:
         try:
            with open(MD5_CACHE_PATH, "r", encoding="utf-8") as f:
                cache = json.load(f)
        except Exception:
            cache = {}
         try:
             mtime = os.path.getmtime(new_osu_path)
        except Exception:
             mtime = None
         cache[new_osu_path] = {"mtime": mtime, "md5": md5_hash}
         try:
             with open(MD5_CACHE_PATH, "w", encoding="utf-8") as f:
                 json.dump(cache, f, indent=4)
         except Exception as e:
            logger.error("Ошибка обновления osu_md5_cache: %s", e)
 
 def count_objs(osu_path, beatmap_id):
 