         chat_meta=chat_meta,
         messages=messages,
         character_dict=g.user.json_info(),
        user_info=json.dumps(user_info),
         legacy_bbcode=g.redis.sismember('use-legacy-bbcode', chat_url)
     )
 