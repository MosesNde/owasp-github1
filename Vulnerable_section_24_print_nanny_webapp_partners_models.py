             self.qrcode.save(f"{self.key}.png", ContentFile(output.read()))
 
     def __str__(self):
        return self.key.hex