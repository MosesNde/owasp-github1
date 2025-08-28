 {
     QString output, error, strmatch, strcmd;
     m_blocksSize = m_numOfFreeOrUsedBlocks = m_totalNumOfBlock = -1;
    strcmd = QString("xfs_db -r -c 'sb 0' -c 'print blocksize' -c 'print dblocks'"
                     " -c 'print fdblocks' %1")
                  .arg(partition.getPath());
    if (Utils::executWithPipeCmd(strcmd, output, error) == 0) {
         auto strList = output.split("\n");
         foreach (auto &item, strList) {
             auto value = item.split("=", QString::SkipEmptyParts);