 	long long int version = json["version"]->asIntegerNumber();
 	if (version != 2) {
 		error("Cannot load savegame version %lld", version);
 		return false;
 	}
 	uint32 gameTime = (uint32)json["gameTime"]->asNumber();
 
 	sqcall("postLoad");
 
 	return true;
 }
 