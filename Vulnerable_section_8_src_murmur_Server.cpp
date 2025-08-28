 }
 
 void Server::log(ServerUser *u, const QString &str) {
	QString msg = QString("<%1:%2(%3)> %4").arg(u->uiSession).arg(u->qsName).arg(u->iId).arg(str);
 	log(msg);
 }
 