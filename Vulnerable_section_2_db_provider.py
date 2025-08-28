     try:
         for pool_id in pool_id_list:
             sql_24h = "select point,sum(fee_x) as fee_x,sum(fee_y) as fee_y,sum(tvl_x_l) as tvl_x_l," \
                      "sum(tvl_y_l) as tvl_y_l from dcl_pool_analysis where pool_id = '%s' " \
                      "and `timestamp` >= %s GROUP BY point order by point" % (pool_id, timestamp)
            cursor.execute(sql_24h)
             point_data_24h = cursor.fetchall()
             redis_conn.add_pool_point_24h_assets(network_id, pool_id, json.dumps(point_data_24h))
             add_redis_data(network_id, Cfg.NETWORK[network_id]["REDIS_POOL_POINT_24H_DATA_KEY"], pool_id, json.dumps(point_data_24h))
     db_conn = get_burrow_connect(network_id)
 
     sql = "insert into liquidation_result_info(`key`, `values`, `timestamp`, `created_time`, `updated_time`) " \
          "values('%s','%s',%s, now(), now())" % (key, values, now_time)
     cursor = db_conn.cursor(cursor=pymysql.cursors.DictCursor)
     try:
        cursor.execute(sql)
         db_conn.commit()
 
     except Exception as e:
 
 def update_liquidation_result(network_id, key, values):
     db_conn = get_burrow_connect(network_id)
    sql = "update liquidation_result_info set `values` = '%s' where `key` = '%s'" % (values, key)
     cursor = db_conn.cursor(cursor=pymysql.cursors.DictCursor)
     try:
        cursor.execute(sql)
         db_conn.commit()
     except Exception as e:
         # Rollback on error
 
 def add_user_wallet_info(network_id, account_id, wallet_address):
     db_conn = get_db_connect(network_id)
    query_sql = "select id from t_user_wallet_info where account_id = '%s' and wallet_address = '%s'" % (account_id, wallet_address)
     sql = "insert into t_user_wallet_info(account_id, wallet_address, `created_time`, `updated_time`) " \
          "values('%s','%s', now(), now())" % (account_id, wallet_address)
     cursor = db_conn.cursor()
     try:
        cursor.execute(query_sql)
         row = cursor.fetchone()
         if row is None:
            cursor.execute(sql)
             db_conn.commit()
     except Exception as e:
         db_conn.rollback()