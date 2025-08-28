 void StaticFileServing::setSSDPDescription(const QString& desc)
 {
 	if(desc.isEmpty())
 		_ssdpDescription.clear();
	else
 		_ssdpDescription = desc.toLocal8Bit();
 }
 
void StaticFileServing::printErrorToReply (QtHttpReply * reply, QtHttpReply::StatusCode code, QString errorMessage)
 {
 	reply->setStatusCode(code);
 	reply->addHeader ("Content-Type", QByteArrayLiteral ("text/html"));
 	if (errorPage.open (QFile::ReadOnly))
 	{
 		QByteArray data = errorPage.readAll();
		data = data.replace("{MESSAGE}", errorMessage.toLocal8Bit() );
 		reply->appendRawData (data);
 		errorPage.close ();
 	}
 	else
 	{
		reply->appendRawData (QString(QString::number(code) + " - " +errorMessage).toLocal8Bit());
 	}
 
 	if (errorPageFooter.open (QFile::ReadOnly))
 				}
 				return;
 			}
			else if(uri_parts.at(0) == "description.xml" && !_ssdpDescription.isNull())
 			{
 				reply->addHeader ("Content-Type", "text/xml");
 				reply->appendRawData (_ssdpDescription);