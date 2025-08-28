     return exitcode;
 }
 
int Utils::executWithPipeCmd(const QString &strCmd, QString &outPut, QString &error)
 {
    QStringList argList;
    argList << "-c" << strCmd;
 
    return executeCmdWithArtList("/bin/bash", argList, outPut, error);
 }
 
 int Utils::executWithErrorCmd(const QString &strCmd, const QStringList &strArg, QString &outPut, QString &outPutError, QString &error)