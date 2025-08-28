 	}
 
 	foreach(const QString &dev, qlInputDevs) {
		QString t=QString::fromLatin1("[%1] %2").arg(dev).arg(cards->qhInput.value(dev));
 		qlReturn << audioDevice(t, dev);
 	}
 
 	}
 
 	foreach(const QString &dev, qlOutputDevs) {
		QString t=QString::fromLatin1("[%1] %2").arg(dev).arg(cards->qhOutput.value(dev));
 		qlReturn << audioDevice(t, dev);
 	}
 