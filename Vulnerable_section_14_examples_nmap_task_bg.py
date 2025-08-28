     if nmaptask:
         print(
             "Task {0} ({1}): ETC: {2} DONE: {3}%".format(
                nmaptask.name,
                nmaptask.status,
                nmaptask.etc,
                nmaptask.progress
             )
         )
 print("rc: {0} output: {1}".format(nmap_proc.rc, nmap_proc.summary))