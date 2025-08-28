 			return this._session;
 		}
 
		internal bool IsStandalone => this._session is GxSession || this._isSumbited || this.HttpContext == null;
 
 		internal void SetSession(IGxSession value)
 		{
 					return Guid.Empty.ToString();
 			}
 		}

 		public string GetImageSrcSet(string baseImage)
 		{
 			if (!String.IsNullOrEmpty(baseImage))
 		}
 		public string FileFromBase64(string b64)
 		{
			Guid tmpGuid = Guid.NewGuid();
			string tmpFileName;
			if (tmpGuid == Guid.Empty)//Guid.NewGuid is not guaranteed to not equal Guid.Empty
				tmpFileName = Math.Truncate(NumberUtil.Random() * 9999).ToString();
			else
				tmpFileName = tmpGuid.ToString();
 			string filePath = Path.Combine(Preferences.getTMP_MEDIA_PATH(), "Blob" + tmpFileName);
 			GxFile auxFile = new GxFile(GetPhysicalPath(), filePath, GxFileType.Private);
 			auxFile.FromBase64(b64);
 		}
 		public string FileFromByteArray(byte[] bArray)
 		{
			Guid tmpGuid = Guid.NewGuid();
			string tmpFileName;
			if (tmpGuid == Guid.Empty) //Guid.NewGuid is not guaranteed to not equal Guid.Empty
				tmpFileName = Math.Truncate(NumberUtil.Random() * 9999).ToString();
			else
				tmpFileName = tmpGuid.ToString();
 			string filePath = Path.Combine(Preferences.getTMP_MEDIA_PATH(), "Blob" + tmpFileName);
 			GxFile auxFile = new GxFile(GetPhysicalPath(), filePath, GxFileType.Private);
 			auxFile.FromByteArray(bArray);