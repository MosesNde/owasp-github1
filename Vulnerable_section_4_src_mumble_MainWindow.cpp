 
 	unsigned int version = g.sh->uiVersion;
 
	QString qsVersion=tr("<h2>Version</h2><p>Protocol %1.%2.%3. Release %4.<br />Running on %5 %6.</p>").arg((version >> 16) & 0xFF).arg((version >> 8) & 0xFF).arg(version & 0xFF).arg(g.sh->qsRelease).arg(g.sh->qsOS).arg(g.sh->qsOSVersion);
	QString qsControl=tr("<h2>Control channel</h2><p>Encrypted with %1 bit %2<br />%3 ms average latency (%4 deviation)</p>").arg(qsc.usedBits()).arg(qsc.name()).arg(boost::accumulators::mean(g.sh->accTCP), 0, 'f', 2).arg(sqrt(boost::accumulators::variance(g.sh->accTCP)),0,'f',2);
 	QString qsVoice, qsCrypt, qsAudio;
 
 	if (NetworkConfig::TcpModeEnabled()) {