 	// ROS_INFO("Received command %s", c.c_str());
 	if(cmd == "reset") { resetCLIPS(); }
 	else if(cmd == "clear") { clearCLIPS(); }
	else if(cmd == "raw")   { clips::sendCommand(arg); }
 	else if(cmd == "print") { handlePrint(arg); }
 	else if(cmd == "watch") { handleWatch(arg); }
 	else if(cmd == "load")  { loadFile(arg); }