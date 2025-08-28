 
 class NmapReport(object):
     """
        NmapReport is the usual interface for the end user to
        read scans output.
 
        A NmapReport as the following structure:
 
        - Scan headers data
        - A list of scanned hosts (NmapReport.hosts)
        - Scan footer data
 
        It is to note that each NmapHost comprised in NmapReport.hosts array
        contains also a list of scanned services (NmapService object).
 
        This means that if NmapParser.parse*() is the input interface for the
        end user of the lib. NmapReport is certainly the output interface for
        the end user of the lib.
     """
 
     def __init__(self, raw_data=None):
         """
            Constructor for NmapReport object.
 
            This is usually called by the NmapParser module.
         """
         self._nmaprun = {}
         self._scaninfo = {}
 
     def save(self, backend):
         """
            This method gets a NmapBackendPlugin representing the backend.
 
            :param backend: libnmap.plugins.PluginBackend object.
 
            Object created by BackendPluginFactory and enabling nmap reports
            to be saved/stored in any type of backend implemented in plugins.
 
            The primary key of the stored object is returned.
 
            :return: str
         """
         if backend is not None:
             _id = backend.insert(self)
 
     def diff(self, other):
         """
            Calls NmapDiff to check the difference between self and
            another NmapReport object.
 
            Will return a NmapDiff object.
 
            :return: NmapDiff object
            :todo: remove is_consistent approach, diff() should be generic.
         """
         if self.is_consistent() and other.is_consistent():
             _rdiff = NmapDiff(self, other)
     @property
     def started(self):
         """
            Accessor returning a unix timestamp of when the scan was started.
 
            :return: integer
         """
         rval = -1
         try:
     @property
     def startedstr(self):
         """
            Accessor returning a human readable string of when the
            scan was started
 
            :return: string
         """
         rval = ""
         try:
     @property
     def commandline(self):
         """
            Accessor returning the full nmap command line fired.
 
            :return: string
         """
         return self._nmaprun["args"]
 
     @property
     def version(self):
         """
            Accessor returning the version of the
            nmap binary used to perform the scan.
 
            :return: string
         """
         return self._nmaprun["version"]
 
     @property
     def xmlversion(self):
         """
            Accessor returning the XML output
            version of the nmap report.
 
            :return: string
         """
         return self._nmaprun["xmloutputversion"]
 
     @property
     def scan_type(self):
         """
            Accessor returning a string which identifies what type of scan
            was launched (syn, ack, tcp,...).
 
            :return: string
         """
         return self._scaninfo.get("type")
 
     @property
     def numservices(self):
         """
            Accessor returning the number of services the
            scan attempted to enumerate.
 
            :return: integer
         """
         rval = -1
         try:
     @property
     def hosts(self):
         """
            Accessor returning an array of scanned hosts.
 
            Scanned hosts are NmapHost objects.
 
            :return: array of NmapHost
         """
         return self._hosts
 
     def get_host_byid(self, host_id):
         """
           Gets a NmapHost object directly from the host array
           by looking it up by id.
 
           :param ip_addr: ip address of the host to lookup
           :type ip_addr: string
 
           :return: NmapHost
         """
         rval = None
         for _rhost in self._hosts:
     @property
     def endtime(self):
         """
            Accessor returning a unix timestamp of when the scan ended.
 
            :return: integer
         """
         rval = -1
         try:
     @property
     def endtimestr(self):
         """
            Accessor returning a human readable time string
            of when the scan ended.
 
            :return: string
         """
         rval = ""
         try:
     @property
     def summary(self):
         """
            Accessor returning a string describing and
            summarizing the scan.
 
            :return: string
         """
         rval = ""
         try:
                     self.endtimestr,
                     self.hosts_total,
                     self.hosts_up,
                    self.elapsed
                 )
             )
         return rval
 
     @property
     def elapsed(self):
         """
            Accessor returning the number of seconds the scan took
 
            :return: float (0 >= or -1)
         """
         rval = -1
         try:
     @property
     def hosts_up(self):
         """
            Accessor returning the numer of host detected
            as 'up' during the scan.
 
            :return: integer (0 >= or -1)
         """
         rval = -1
         try:
     @property
     def hosts_down(self):
         """
            Accessor returning the numer of host detected
            as 'down' during the scan.
 
            :return: integer (0 >= or -1)
         """
         rval = -1
         try:
     @property
     def hosts_total(self):
         """
            Accessor returning the number of hosts scanned in total.
 
            :return: integer (0 >= or -1)
         """
         rval = -1
         try:
 
     def get_raw_data(self):
         """
            Returns a dict representing the NmapReport object.
 
            :return: dict
            :todo: deprecate. get rid of this uglyness.
         """
         raw_data = {
             "_nmaprun": self._nmaprun,
 
     def is_consistent(self):
         """
            Checks if the report is consistent and can be diffed().
 
            This needs to be rewritten and removed: diff() should be generic.
 
            :return: boolean
         """
        rval = False
         rdata = self.get_raw_data()
         _consistent_keys = ["_nmaprun", "_scaninfo", "_hosts", "_runstats"]
        if (
            set(_consistent_keys) == set(rdata.keys()) and
            len([dky for dky in rdata.keys() if rdata[dky] is not None]) == 4
        ):
            rval = True
         return rval
 
     def get_dict(self):
         """
            Return a python dict representation of the NmapReport object.
            This is used to diff() NmapReport objects via NmapDiff.
 
            :return: dict
         """
         rdict = dict(
             [
     @property
     def id(self):
         """
            Dummy id() defined for reports.
         """
         return hash(1)
 
     def __eq__(self, other):
         """
            Compare eq NmapReport based on :
 
                - create a diff obj and check the result
                report are equal if added&changed&removed are empty
 
            :return: boolean
         """
         rval = False
         if self.__class__ == other.__class__ and self.id == other.id:
 
     def __ne__(self, other):
         """
            Compare ne NmapReport based on:
 
                - create a diff obj and check the result
                report are ne if added|changed|removed are not empty
 
            :return: boolean
         """
         rval = True
         if self.__class__ == other.__class__ and self.id == other.id:
             self.__class__.__name__,
             self.started,
             self.hosts_up,
            self.hosts_total
         )