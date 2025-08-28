 	if (reply.isValid())
 		name = reply.value();
 	else {
		server->log(QString("DBus Authenticator failed getUserName for %1: %2").arg(id).arg(reply.error().message()));
 		removeAuthenticator();
 	}
 }
 	qsAuthPath = path.path();
 	qsAuthService = msg.service();
 	bReentrant = reentrant;
	server->log(QString("DBus Authenticator set to %1 %2 (%3)").arg(qsAuthService).arg(qsAuthPath).arg(reentrant));
 }
 
 void MurmurDBus::setTemporaryGroups(int channel, int userid, const QStringList &groups, const QDBusMessage &msg) {