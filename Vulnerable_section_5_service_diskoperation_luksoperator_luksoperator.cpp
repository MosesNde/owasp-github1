 
 bool LUKSOperator::format(const LUKS_INFO &luks)
 {
    QProcess proc;
    QStringList options;
    options << "-c" << QString("echo -n '%1' | cryptsetup --cipher %2 --key-size 256 --hash sha256 luksFormat --label=%3 %4 -q")
            .arg(luks.m_decryptStr)
            .arg(Utils::getCipherStr(luks.m_crypt))
            .arg(luks.m_fileSystemLabel)
            .arg(luks.m_devicePath);
    proc.start("/bin/bash", options);
    proc.waitForFinished(-1);
    proc.waitForReadyRead();
    QString outPut = proc.readAllStandardOutput();
    QString error = proc.errorString();
    proc.close();
    bool success = (proc.exitCode() == 0);
     if (!success) {
         qCritical() << Q_FUNC_INFO << "output:" << outPut << "\terror:" << error;
     }
 
 bool LUKSOperator::open(const LUKS_INFO &luks)
 {
    QProcess proc;
    QStringList options;
    options << "-c" << QString("echo -n '%1' | cryptsetup open %2 %3 -q")
            .arg(luks.m_decryptStr)
            .arg(luks.m_devicePath)
            .arg(luks.m_mapper.m_dmName);
    proc.start("/bin/bash", options);
    proc.waitForFinished(-1);
    proc.waitForReadyRead();//
    proc.close();
    return proc.exitCode() == 0;
 }
 
 bool LUKSOperator::testKey(const LUKS_INFO &luks)
 {
    QProcess proc;
    QStringList options;
    options << "-c" << QString("echo -n '%1' | cryptsetup open --test-passphrase  %2 %3 -q")
            .arg(luks.m_decryptStr)
            .arg(luks.m_devicePath)
            .arg(luks.m_mapper.m_dmName);
    proc.start("/bin/bash", options);
    proc.waitForFinished(-1);
    proc.waitForReadyRead();//
    proc.close();
    return proc.exitCode() == 0;
 }
 
 bool LUKSOperator::close(const LUKS_INFO &luks)
     }
 
     //添加key
    QProcess proc;
    QStringList options;
    options << "-c" << QString("echo -n '%1' | cryptsetup luksAddKey %2 %3 -q")
            .arg(luks.m_decryptStr)
            .arg(luks.m_devicePath)
            .arg(filePath);
    proc.start("/bin/bash", options);
    proc.waitForFinished();
    proc.waitForReadyRead();//
    proc.close();
    return proc.exitCode() == 0;
 }
 
 bool LUKSOperator::deleteKeyFile(const LUKS_INFO &luks)