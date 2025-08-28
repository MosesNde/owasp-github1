 
 
 try:
    import xml.etree.cElementTree as ET
 except ImportError:
    import xml.etree.ElementTree as ET
from libnmap.objects import NmapHost, NmapService, NmapReport
 
 
 class NmapParser(object):
             )
         elif not isinstance(nmap_data, str):
             raise NmapParserException(
                "wrong nmap_data type given as "
                "argument: cannot parse data"
             )
 
         if incomplete is True:
         elif root.tag == "port":
             nmapobj = cls._parse_xml_port(root)
         else:
            raise NmapParserException("Unpexpected data structure for XML "
                                      "root node")
         return nmapobj
 
     @classmethod
     def _parse_xml_report(cls, root=None):
         """
            This method parses out a full nmap scan report from its XML root
            node: <nmaprun>.
 
            :param root: Element from xml.ElementTree (top of XML the document)
            :type root: Element
 
            :return: NmapReport object
         """
 
         nmap_scan = {
             "_nmaprun": {},
             "_scaninfo": {},
             "_hosts": [],
            "_runstats": {}
         }
 
         if root is None:
            raise NmapParserException("No root node provided to parse XML "
                                      "report")
 
         nmap_scan["_nmaprun"] = cls.__format_attributes(root)
         for el in root:
 
     @classmethod
     def parse_fromfile(
        cls, nmap_report_path,
        data_type="XML",
        incomplete=False
     ):
         """
             Call generic cls.parse() method and ensure that a correct file \
     @classmethod
     def __parse_scaninfo(cls, scaninfo_data):
         """
            Private method parsing a portion of a nmap scan result.
            Receives a <scaninfo> XML tag.
 
            :param scaninfo_data: <scaninfo> XML tag from a nmap scan
            :type scaninfo_data: xml.ElementTree.Element or a string
 
            :return: python dict representing the XML scaninfo tag
         """
 
         xelement = cls.__format_element(scaninfo_data)
     @classmethod
     def _parse_xml_host(cls, scanhost_data):
         """
            Protected method parsing a portion of a nmap scan result.
            Receives a <host> XML tag representing a scanned host with
            its services.
 
            :param scaninfo_data: <host> XML tag from a nmap scan
            :type scaninfo_data: xml.ElementTree.Element or a string
 
            :return: NmapHost object
         """
 
         xelement = cls.__format_element(scanhost_data)
             # else:
             #    print "struct host unknown attr: %s value: %s" %
             #           (h.tag, h.get(h.tag))
        _stime = ""
        _etime = ""
        if "starttime" in _host_header:
            _stime = _host_header["starttime"]
        if "endtime" in _host_header:
            _etime = _host_header["endtime"]
         nhost = NmapHost(
             _stime,
             _etime,
             _addresses,
             _status,
             _hostnames,
             _services,
            _host_extras
         )
         return nhost
 
     @classmethod
     def __parse_hostnames(cls, scanhostnames_data):
         """
            Private method parsing the hostnames list within a <host> XML tag.
 
            :param scanhostnames_data: <hostnames> XML tag from a nmap scan
            :type scanhostnames_data: xml.ElementTree.Element or a string
 
            :return: list of hostnames
         """
 
         xelement = cls.__format_element(scanhostnames_data)
     @classmethod
     def _parse_xml_ports(cls, scanports_data):
         """
            Protected method parsing the list of scanned services from
            a targeted host. This protected method cannot be called directly
            with a string. A <ports/> tag can be directly passed to parse()
            and the below method will be called and return a list of nmap
            scanned services.
 
            :param scanports_data: <ports> XML tag from a nmap scan
            :type scanports_data: xml.ElementTree.Element or a string
 
            :return: list of NmapService
         """
 
         xelement = cls.__format_element(scanports_data)
     @classmethod
     def _parse_xml_port(cls, scanport_data):
         """
            Protected method parsing a scanned service from a targeted host.
            This protected method cannot be called directly.
            A <port/> tag can be directly passed to parse() and the below
            method will be called and return a NmapService object
            representing the state of the service.
 
            :param scanport_data: <port> XML tag from a nmap scan
            :type scanport_data: xml.ElementTree.Element or a string
 
            :return: NmapService
         """
 
         xelement = cls.__format_element(scanport_data)
     @classmethod
     def __parse_service(cls, xserv):
         """
            Parse <service> tag to manage CPE object
         """
         _service = cls.__format_attributes(xserv)
         _cpelist = []
     @classmethod
     def __parse_extraports(cls, extraports_data):
         """
            Private method parsing the data from extra scanned ports.
            X extraports were in state "closed" server returned "conn-refused"
            tag: <extraports>
 
            :param extraports_data: XML data for extraports
            :type extraports_data: xml.ElementTree.Element or a string
 
            :return: python dict with following keys: state, count, reason
         """
         rdict = {"state": "", "count": "", "reasons": []}
         xelement = cls.__format_element(extraports_data)
     @classmethod
     def __parse_script_table(cls, script_table):
         """
           Private method parsing a table from NSE scripts output
 
           :param sccript_table: poertion of XML containing the table
           :type script_table: xml.ElementTree.Element
 
           :return: python dict of table structure
         """
         tdict = {}
         for telem in script_table:
     @classmethod
     def __parse_script(cls, script_data):
         """
            Private method parsing the data from NSE scripts output
 
            :param script_data: portion of XML describing the results of the
            script data
            :type script_data: xml.ElementTree.Element or a string
 
            :return: python dict holding scripts output
         """
         _script_dict = cls.__format_attributes(script_data)
 
     @classmethod
     def __parse_host_scripts(cls, scripts_data):
         """
            Private method parsing the data from scripts affecting
            the target host.
            Contents of <hostscript> is returned as a list of dict.
 
            :param scripts_data: portion of XML describing the results of the
            scripts data
            :type scripts_data: xml.ElementTree.Element or a string
 
            :return: python list holding scripts output in a dict
         """
         _host_scripts = []
         for xscript in scripts_data:
     @classmethod
     def __parse_os_fingerprint(cls, os_data):
         """
            Private method parsing the data from an OS fingerprint (-O).
            Contents of <os> is returned as a dict.
 
            :param os_data: portion of XML describing the results of the
            os fingerprinting attempt
            :type os_data: xml.ElementTree.Element or a string
 
            :return: python dict representing the XML os tag
         """
         rdict = {}
         xelement = cls.__format_element(os_data)
     @classmethod
     def __parse_osmatch(cls, osmatch_data):
         """
            This methods parses osmatch data and returns a dict. Depending
            on the nmap xml version, osmatch could contain an osclass
            dict.
 
            :param osmatch_data: <osmatch> XML tag from a nmap scan
            :type osmatch_data: xml.ElementTree.Element or a string
 
            :return: python dict representing the XML osmatch tag
         """
         rdict = {}
         xelement = cls.__format_element(osmatch_data)
     @classmethod
     def __parse_osclass(cls, osclass_data):
         """
            This methods parses osclass data and returns a dict. Depending
            on the nmap xml version, osclass could contain a cpe
            dict.
 
            :param osclass_data: <osclass> XML tag from a nmap scan
            :type osclass_data: xml.ElementTree.Element or a string
 
            :return: python dict representing the XML osclass tag
         """
         rdict = {}
         xelement = cls.__format_element(osclass_data)
     @classmethod
     def __parse_runstats(cls, scanrunstats_data):
         """
            Private method parsing a portion of a nmap scan result.
            Receives a <runstats> XML tag.
 
            :param scanrunstats_data: <runstats> XML tag from a nmap scan
            :type scanrunstats_data: xml.ElementTree.Element or a string
 
            :return: python dict representing the XML runstats tag
         """
 
         xelement = cls.__format_element(scanrunstats_data)
     @staticmethod
     def __format_element(elt_data):
         """
            Private method which ensures that a XML portion to be parsed is
            of type xml.etree.ElementTree.Element.
            If elt_data is a string, then it is converted to an
            XML Element type.
 
            :param elt_data: XML Element to be parsed or string
            to be converted to a XML Element
 
            :return: Element
         """
         if isinstance(elt_data, str):
             try:
                     "to instanciate XML Element from "
                     "string {0} - {1}".format(elt_data, e)
                 )
        elif ET.iselement(elt_data):
             xelement = elt_data
         else:
             raise NmapParserException(
     @staticmethod
     def __format_attributes(elt_data):
         """
            Private method which converts a single XML tag to a python dict.
            It also checks that the elt_data given as argument is of type
            xml.etree.ElementTree.Element
 
            :param elt_data: XML Element to be parsed or string
            to be converted to a XML Element
 
            :return: Element
         """
 
         rval = {}
        if not ET.iselement(elt_data):
             raise NmapParserException(
                 "Error while trying to parse supplied "
                 "data attributes: format is not XML or "