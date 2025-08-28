 		Channel *c = qhChannels.value(msg.channel_id());
 
 		userEnterChannel(pDstServerUser, c);
		log(uSource, QString("Moved %1 to %2").arg(*pDstServerUser).arg(*c));
 	}
 
 
 		if (msg.has_suppress())
 			pDstServerUser->bSuppress = msg.suppress();
 
		log(uSource, QString("Changed speak-state of %1 (%2 %3 %4)").arg(*pDstServerUser).arg(pDstServerUser->bMute).arg(pDstServerUser->bDeaf).arg(pDstServerUser->bSuppress));
 	}
 
 	if (msg.has_user_id()) {
 
 	sendAll(msg);
 	if (ban)
		log(uSource, QString("Kickbanned %1 (%2)").arg(*pDstServerUser).arg(u8(msg.reason())));
 	else
		log(uSource, QString("Kicked %1 (%2)").arg(*pDstServerUser).arg(u8(msg.reason())));
 	pDstServerUser->disconnectSocket();
 }
 
 		updateChannel(c);
 
 		msg.set_channel_id(c->iId);
		log(uSource, QString("Added channel %1 under %2").arg(*c).arg(*p));
 		emit channelCreated(c);
 		sendAll(msg);
 
 		// All permission checks done -- the update is good.
 
 		if (p) {
			log(uSource, QString("Moved channel %1 from %2 to %3").arg(*c).arg(* c->cParent).arg(*p));
 
 			c->cParent->removeChannel(c);
 			p->addChannel(c);
 		}
 		if (! qsName.isNull()) {
			log(uSource, QString("Renamed channel %1 to %2").arg(*c).arg(qsName));
 			c->qsName = qsName;
 		}
 		if (! qsDesc.isNull())
 				unregisterUser(id);
 			} else {
 				const QString &name = u8(u.name());
				log(uSource, QString::fromLatin1("Renamed user %1 to '%2'").arg(id).arg(name));
 
 				QMap<QString, QString> info;
 				info.insert("name", name);