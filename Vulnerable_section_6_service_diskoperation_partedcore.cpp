     bool needRewrite = gptIsExpanded(devicePath);
     if (needRewrite) {
         QString outPutFix, errorFix;
        QString cmdFix = QString("echo w | fdisk %1").arg(devicePath);
        Utils::executWithPipeCmd(cmdFix, outPutFix, errorFix);
         qDebug() << __FUNCTION__ << "createPartition Partition Table Rewrite Done";
         return false;
     }
     bool needRewrite = gptIsExpanded(devicePath);
     if (needRewrite) {
         QString outPutFix, errorFix;
        QString cmdFix = QString("echo w | fdisk %1").arg(devicePath);
        Utils::executWithPipeCmd(cmdFix, outPutFix, errorFix);
         qDebug() << __FUNCTION__ << "createPartition Partition Table Rewrite Done";
         return;
     }