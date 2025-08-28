 # -*- coding: utf-8 -*-
 
 import warnings
 from libnmap.objects.cpe import CPE
 
 
 class OSFPPortUsed(object):
     """
        Port used class: this enables the user of NmapOSFingerprint class
        to have a common and clear interface to access portused data which
        were collected and used during os fingerprint scan
     """
 
     def __init__(self, port_used_dict):
     @property
     def state(self):
         """
            Accessor for the portused state (closed, open,...)
         """
         return self._state
 
     @property
     def proto(self):
         """
            Accessor for the portused protocol (tcp, udp,...)
         """
         return self._proto
 
     @property
     def portid(self):
         """
            Accessor for the referenced port number used
         """
         return self._portid
 
 
 class NmapOSMatch(object):
     """
        NmapOSMatch is an internal class used for offering results
        from an nmap os fingerprint. This common interfaces makes
        a compatibility between old nmap xml (<1.04) and new nmap
        xml versions (used in nmapv6 for instance).

        In previous xml version, osclass tags from nmap fingerprints
        were not directly mapped to a osmatch. In new xml version,
        osclass could be embedded in osmatch tag.

        The approach to solve this is to create a common class
        which will, for older xml version, match based on the accuracy
        osclass to an osmatch. If no match, an osmatch will be made up
        from a concat of os class attributes: vendor and osfamily.
        Unmatched osclass will have a line attribute of -1.

        More info, see issue #26 or http://seclists.org/nmap-dev/2012/q2/252
     """
 
     def __init__(self, osmatch_dict):
     def add_osclass(self, osclass_obj):
 
         """
            Add a NmapOSClass object to the OSMatch object. This method is
            useful to implement compatibility with older versions of NMAP
            by providing a common interface to access os fingerprint data.
         """
         self._osclasses.append(osclass_obj)
 
     @property
     def osclasses(self):
         """
            Accessor for all NmapOSClass objects matching with this OS Match
         """
         return self._osclasses
 
     @property
     def name(self):
         """
            Accessor for name attribute (e.g.: Linux 2.4.26 (Slackware 10.0.0))
         """
         return self._name
 
     @property
     def line(self):
         """
            Accessor for line attribute as integer. value equals -1 if this
            osmatch holds orphans NmapOSClass objects. This could happen with
            older version of nmap xml engine (<1.04 (e.g: nmapv6)).
 
            :return: int
         """
         return int(self._line)
 
     @property
     def accuracy(self):
         """
            Accessor for accuracy
 
            :return: int
         """
         return int(self._accuracy)
 
     def get_cpe(self):
         """
            This method return a list of cpe stings and not CPE objects as
            the NmapOSClass.cpelist property. This method is a helper to
            simplify data management.
 
            For more advanced handling of CPE data, use NmapOSClass.cpelist
            and use the methods from CPE class
         """
         _cpelist = []
         for osc in self.osclasses:
 
 class NmapOSClass(object):
     """
        NmapOSClass offers an unified API to access data from analysed
        osclass tag. As implemented in libnmap and newer version of nmap,
        osclass objects will always be embedded in a NmapOSMatch.
        Unmatched NmapOSClass will be stored in "dummy" NmapOSMatch objects
        which will have the particularity of have a line attribute of -1.
        On top of this, NmapOSClass will have optional CPE objects
        embedded.
     """
 
     def __init__(self, osclass_dict):
     @property
     def cpelist(self):
         """
            Returns a list of CPE Objects matching with this os class
 
            :return: list of CPE objects
            :rtype: Array
         """
         return self._cpelist
 
     @property
     def vendor(self):
         """
            Accessor for vendor information (Microsoft, Linux,...)
 
            :return: string
         """
         return self._vendor
 
     @property
     def osfamily(self):
         """
            Accessor for OS family information (Windows, Linux,...)
 
            :return: string
         """
         return self._osfamily
 
     @property
     def accuracy(self):
         """
            Accessor for OS class detection accuracy (int)
 
            :return: int
         """
         return int(self._accuracy)
 
     @property
     def osgen(self):
         """
            Accessor for OS class generation (7, 8, 2.4.X,...).
 
            :return: string
         """
         return self._osgen
 
     @property
     def type(self):
         """
            Accessor for OS class type (general purpose,...)
 
            :return: string
         """
         return self._type
 
     @property
     def description(self):
         """
            Accessor helper which returns a concataned string of
            the valuable attributes from NmapOSClass object
 
            :return: string
         """
         rval = "{0}: {1}, {2}".format(self.type, self.vendor, self.osfamily)
         if len(self.osgen):
 
 class NmapOSFingerprint(object):
     """
        NmapOSFingerprint is a easier API for using os fingerprinting.
        Data for OS fingerprint (<os> tag) is instanciated from
        a NmapOSFingerprint which is accessible in NmapHost via NmapHost.os
     """
 
     def __init__(self, osfp_data):
 
     def get_osmatch(self, osclass_obj):
         """
            This function enables NmapOSFingerprint to determine if an
            NmapOSClass object could be attached to an existing NmapOSMatch
            object in order to respect the common interface for
            the nmap xml version < 1.04 and >= 1.04
 
            This method will return an NmapOSMatch object matching with
            the NmapOSClass provided in parameter
            (match is performed based on accuracy)
 
            :return: NmapOSMatch object
         """
         rval = None
         for _osmatch in self.__osmatches:
 
     def _add_dummy_osmatch(self, osclass_obj):
         """
            This functions creates a dummy NmapOSMatch object in order to
            encapsulate an NmapOSClass object which was not matched with an
            existing NmapOSMatch object
         """
         _dname = "{0}:{1}:{2}".format(
             osclass_obj.type, osclass_obj.vendor, osclass_obj.osfamily
             "osmatch": {
                 "name": _dname,
                 "accuracy": osclass_obj.accuracy,
                "line": -1
             },
             "osclasses": [],
         }
     @property
     def ports_used(self):
         """
            Return an array of OSFPPortUsed object with the ports used to
            perform the os fingerprint. This dict might contain another dict
            embedded containing the ports_reason values.
         """
         return self.__ports_used
 