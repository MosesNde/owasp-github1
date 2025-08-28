                 server_game.start_game()
                 
 
             # manue room
             if len(self.waiting_rooms[room]) == 1 and 'manue' in room :
                for i in range(3):
                    thread = threading.Thread(target=self.run_manue, args=(room, f"manue{i}"), daemon=True)
                    thread.start()
                     
 
     def run_manue(self, room_name, player_name):
         proc = subprocess.run([
                f"docker build -t manue:dev manue/. && docker run --rm manue:dev /mjai/mjai/run_manue.sh {player_name} {room_name}"
                 ], 
             shell=True,
             stdout=subprocess.DEVNULL,