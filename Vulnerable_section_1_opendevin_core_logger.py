         self.baseFilename = os.path.join(self.log_directory, filename)
         self.stream = self._open()
         super().emit(record)
        self.stream.close
         opendevin_logger.debug('Logging to %s', self.baseFilename)
         self.message_counter += 1
 