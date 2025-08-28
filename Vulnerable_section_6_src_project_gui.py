 import generate_image as img_mod
 from analyzer import scan_replays, make_top
 
 BASE_SRC_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 ICON_PATH = os.path.join(BASE_SRC_PATH, "assets", "icons")
 FONT_PATH = os.path.join(BASE_SRC_PATH, "assets", "fonts")
         self.top_completed = threading.Event()
         self.img_completed = threading.Event()
 
                                                           
         self.overall_progress = 0
                                       
         self.progress_bar.setValue(0)
         self.current_task = "Ошибка выполнения задачи"
         self.status_label.setText(self.current_task)
        self.scan_completed.set()                                          
 
     def browse_directory(self):
         folder = QFileDialog.getExistingDirectory(self, "Select osu! Game Directory", "")
             QMessageBox.warning(self, "Ошибка", "Укажите папку osu! и ввод профиля (URL/ID/Ник).")
             return
 
                                               
         self.btn_all.setDisabled(True)
         self.browse_button.setDisabled(True)
                                         
         self.current_task = "Запуск сканирования..."
         self.status_label.setText(self.current_task)
 
                                                                    
         threading.Thread(target=self._run_sequence, daemon=True).start()
                 self.btn_scan, "click",
                 QtCore.Qt.ConnectionType.QueuedConnection
             )
            self.scan_completed.wait()
 
                                                        
             QtCore.QMetaObject.invokeMethod(
                 self.btn_top, "click",
                 QtCore.Qt.ConnectionType.QueuedConnection
             )
            self.top_completed.wait()
 
                                                       
             QtCore.QMetaObject.invokeMethod(
                 self.btn_img, "click",
                 QtCore.Qt.ConnectionType.QueuedConnection
             )
            self.img_completed.wait()
                                                                             
            QtCore.QMetaObject.invokeMethod(
                self, "all_completed_successfully",
                QtCore.Qt.ConnectionType.QueuedConnection
            )
         except Exception as e:
             logger.error(f"Ошибка последовательного запуска: {e}")
             QtCore.QMetaObject.invokeMethod(
                 self, "enable_all_button",
                 QtCore.Qt.ConnectionType.QueuedConnection