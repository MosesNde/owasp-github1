         self.Shulin_Taidong = {"to": "東部往南（樹林→臺東).db", "from": "東部往北（臺東→樹林）.db"}
         self.Taidong_Xinzuoying = {"to": "南迴往西（臺東→枋寮→新左營）.db", "from": "南迴往東（新左營→枋寮→臺東）.db"}
 
    def count_distance(self, place1, place2, file):
         # print(f"place1: {place1}, place2: {place2}, file: {file}")
        conn = get_db_connection(self.data_path + file)
        cursor = conn.cursor()
        cursor.execute(f"""
                         SELECT 
                            (SELECT 距離 FROM train WHERE 車站 = ?) AS 出發距離,
                            (SELECT 距離 FROM train WHERE 車站 = ?) AS 到達距離
                                
                        """, (place1, place2))
        distance1, distance2 = cursor.fetchone()
         # print(distance1, distance2)
        conn.close()
         return abs(float(distance2) - float(distance1))
 
     # 找尋車站在哪個表之中
    def find_table(self, station_name):
         files = [self.Caozhou_Jilong["to"], self.Shulin_Taidong["to"], self.Taidong_Xinzuoying["to"]]
 
         file_set = set()
 
         raise ValueError(f"{station_name} is not found in any of the databases")
 
    def check_route_direction(self, db_file, start_station, end_station):
        conn = get_db_connection(self.data_path + db_file)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT 車站 FROM train 
                            WHERE 車站 IN ('{start_station}', '{end_station}') 
                            ORDER BY rowid;""")
        records = cursor.fetchone()
        conn.close()
        if records is None:
            raise ValueError(f"Cannot find a valid route from {start_station} to {end_station} in {db_file}")
        return records[0] == start_station
 
    def create_path(self):
         # 順時針
         clockwise_to_file = {"高雄": self.Caozhou_Jilong["to"], "臺北": self.Shulin_Taidong["to"], "臺東": self.Taidong_Xinzuoying["to"]}
         # 逆時針
         counterclockwise_to_file = {"臺北": self.Caozhou_Jilong["to"], "臺東": self.Taidong_Xinzuoying["to"], "高雄": self.Taidong_Xinzuoying["to"]}
         file_to_start_end = {self.Caozhou_Jilong["to"]: ("高雄", "臺北"), self.Shulin_Taidong["to"]: ("臺北", "臺東"), self.Taidong_Xinzuoying["to"]: ("臺東", "高雄")}
         
        files1= self.find_table(self.start)
        files2 = self.find_table(self.end)
         if len(files1) == 0 or len(files2) == 0:
             raise ValueError(f"Cannot find a valid route from {self.start} to {self.end}")
 
                 file_set = frozenset({file1, file2})
             elif len(files1) == 0:
                 start, end = file_to_start_end[file1]
                distance1 = self.count_distance(start, self.start, file1) + self.count_distance(start, self.end, counterclockwise_to_file[start])
                distance2 = self.count_distance(end, self.start, file1) + self.count_distance(end, self.end, clockwise_to_file[end])
                 file_set = frozenset({file1, counterclockwise_to_file[start]}) if distance1 < distance2 else frozenset({file1, clockwise_to_file[end]})
             elif len(files2) == 0:
                 start, end = file_to_start_end[file2]
                distance1 = (self.count_distance(start, self.end, file2) + self.count_distance(start, self.start, counterclockwise_to_file[start]))
                distance2 = self.count_distance(end, self.end, file2) + self.count_distance(end, self.start, clockwise_to_file[end])
                 file_set = frozenset({file2, counterclockwise_to_file[start]}) if distance1 < distance2 else frozenset({file2, clockwise_to_file[end]})
             else:
                 raise ValueError(f"Cannot find a valid route from {self.start} to {self.end}")
         if file_set in transfer_points:
             transfer_station = transfer_points[file_set]
 
            if not self.check_route_direction(file1, self.start, transfer_station):
                 file1 = reverse_direction[file1]
            if not self.check_route_direction(file2, transfer_station, self.end):
                 file2 = reverse_direction[file2]
 
             self.paths = [[
                             "arrival_place": self.end}
             ]]
 
    def create_time(self):
         if len(self.paths[0]) == 1:  # 不需轉車
            fastest_train, cheapest_train = self.find_best_train(self.paths[0][0]["file"], self.start, self.end)
 
             self.paths = copy.deepcopy(self.paths)
             self.paths.append(copy.deepcopy(self.paths[0]))
             second_leg_file = self.paths[0][1]["file"]
 
             # 取得第一段所有列車
            first_leg_fastest_train, first_leg_cheapest_train = self.find_best_train(first_leg_file, self.start, transfer_station)
 
             # 取得所有可銜接的第二段列車(最快)
            second_leg_fastest_train, _ = self.find_best_train(second_leg_file, transfer_station, self.end, first_leg_fastest_train["arrival_time"])
 
             # 取得所有可銜接的第二段列車(最便宜)
            _, second_leg_cheapest_train = self.find_best_train(second_leg_file, transfer_station, self.end, first_leg_cheapest_train["arrival_time"])
 
             self.paths = copy.deepcopy(self.paths)
             self.paths.append(copy.deepcopy(self.paths[0]))
             self.paths[1][0].update(first_leg_cheapest_train)
             self.paths[1][1].update(second_leg_cheapest_train)
 
    def find_best_train(self, db_file, departure_station, arrival_station, min_departure_time=None):
         date_part, time_part = self.departure_time.split(' ')
         if min_departure_time is not None:
             time_part = datetime.strptime(self.departure_time, '%Y-%m-%d %H:%M').strftime('%H:%M')
                     else:
                         train_data["arrival_time"] = date_part + " " + train_data["arrival_time"]
                     available_trains.append(train_data)

         conn.close()
 
         if not available_trains:
             cheapest_train = fastest_train
         return fastest_train, cheapest_train
 
    def create_cost(self):
         for path_i in range(len(self.paths)):
             for route_i in range(len(self.paths[path_i])):
                 route = self.paths[path_i][route_i]
                conn = get_db_connection(self.data_path + route.get("file"))
                cursor = conn.cursor()
                cursor.execute("""
                                SELECT 
                                    (SELECT 距離 FROM train WHERE 車站 = ?) AS 出發距離,
                                    (SELECT 距離 FROM train WHERE 車站 = ?) AS 到達距離
                                """, (route.get("departure_place"), route.get("arrival_place")))
                departure_distance, arrival_distance = cursor.fetchone()
                conn.close()

                distance = max(float(arrival_distance) - float(departure_distance), 10)
                transportation_name = route.get("transportation_name")
                cost = 0
                for name, rate in (("莒光", 1.75), ("自強",2.27), ("普悠瑪", 2.27)):
                    if name  in transportation_name:
                        cost = rate * distance
                        break
                if cost == 0:
                    raise ValueError(f"transportation {transportation_name} not in 莒光, 自強 or 普悠瑪")

                route.update({"cost": round(cost)})
\ No newline at end of file
\ No newline at end of file