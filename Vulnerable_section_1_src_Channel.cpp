 }
 
 Channel::operator const QString() const {
	return QString::fromLatin1("%1[%2:%3%4]").arg(qsName).arg(iId).arg(cParent ? cParent->iId : -1).arg(bTemporary ? QLatin1String("*") : QLatin1String(""));
 }