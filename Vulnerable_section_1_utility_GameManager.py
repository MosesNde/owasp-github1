     def drawTheme(self):
         theme = choice(self.loadThemes())
         try: 
            self.sqlManager.insert("UPDATE rooms SET theme='{}' WHERE room_id={}".format(theme, self.roomId))
             self.drawingTheme = theme
         except sqlError as err:
             print(err)
 
     def sendDrawing(self, pixelList: list):
        try: 
            self.sqlManager.insert("INSERT INTO drawings (creator, pixels, room_id) VALUES ('{}', '{}','{}')".format(self.username, str(pixelList), self.roomId))
         except sqlError as err:
             print(err)
 