 """Knowledge about the PSA key store as implemented in Mbed TLS.
 """
 
 # Copyright The Mbed TLS Contributors
         This is the content of the PSA storage file. When PSA storage is
         implemented over stdio files, this does not include any wrapping made
         by the PSA-storage-over-stdio-file implementation.
         """
         header = self.MAGIC + self.pack('L', self.version)
         if self.version == 0: