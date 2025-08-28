                         part = select_paths[i][j]
                         if part['file'] in express_train.Caozhou_Jilong.values():
                             # 先獲取兩班車與transfer_points，會落在哪個位置，
                            conn = get_db_connection(express_train.data_path + part['file'])
                            cursor = conn.cursor()
                            cursor.execute(f"""SELECT 車站 FROM train
                                                WHERE 車站 IN ('{sql_transfer_points}', '{part['departure_place']}', '{part['arrival_place']}')
                                                ORDER BY rowid;""")
                            record = [trans[0] for trans in cursor.fetchall()]
                            conn.close()
 
                            # 如果都在 "板橋" 往北，"新左營" 往南，則不考慮，
                            if record[1] is part['departure_place'] or record[-2] is part['arrival_place']:
                                break
                            # ! 如果獲取兩班車中包含兩或以上transfer_point則考慮換車，
                            departure_i = record.index(part['departure_place'])
                            arrival_i = record.index(part['arrival_place'])
                            trans = [1] if departure_i is 0 else [departure_i - 1, departure_i + 1]
                            if arrival_i is len(record) - 1:
                                trans = [(i, arrival_i - 1) for i in trans]
                            else:
                                trans = [(i, arrival_i - 1) for i in trans] + [(i, arrival_i + 1) for i in trans]
 
                            orig_spend_time = get_spend_path_minutes(select_paths[i][j:])
 
                            flag = False
                            for m, n in trans:
                                list1 = ExpressTrain(departure_time=start_date, start=part['departure_place'],
                                                     end=record[m]).create()
                                list2 = HighSpeedRail(departure_time=start_date,
                                                      start=HighSpadeRail_transfer_points[ExpressTrain_transfer_points.index(record[m])],
                                                      end=HighSpadeRail_transfer_points[ExpressTrain_transfer_points.index(record[n])],
                                                      discount=True, reserved=True).create()
                                list3 = ExpressTrain(departure_time=start_date, start=record[n],
                                                     end=select_paths[i][-1]['arrival_place']).create()
 
                                list1 = min(list1, key=get_spend_path_minutes)
                                list2 = min(list2, key=get_spend_path_minutes)
                                list3 = min(list3, key=get_spend_path_minutes)
                                if list1 and list2 and list3:
                                    spend_time = get_spend_path_minutes(list1 + list2 + list3)
                                    if spend_time < orig_spend_time:
                                        ExpressTrain_X_HighSpeedRail_paths.append(select_paths[i][:j] + list1 + list2 + list3)
                                        flag = True
                            if flag:
                                break
             paths.extend(ExpressTrain_X_HighSpeedRail_paths)
 
         for i in range(len(paths)):