 bool ProcessReader::readSmaps(const QByteArray &smapsFile, Memory &mem)
 {
     FILE *sf = nullptr;
    auto closeFile = qScopeGuard([=]() { if (sf) fclose(sf); });
 
     sf = fopen(smapsFile.constData(), "r");
     if (!sf)