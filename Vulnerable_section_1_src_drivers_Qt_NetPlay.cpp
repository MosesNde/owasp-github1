 			{
 				FILE *fp;
 				QString filepath = QDir::tempPath();
 				const char *romData = client->romLoadData.buf;
 				const size_t romSize = client->romLoadData.size;
 
 				filepath.append( "/" );
				filepath.append( client->romLoadData.fileName );
 
 				//printf("Load ROM Request Received: %s\n", filepath.c_str());
 				//printf("Dumping Temp Rom to: %s\n", filepath.c_str());