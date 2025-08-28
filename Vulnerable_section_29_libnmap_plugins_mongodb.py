 #!/usr/bin/env python
 import json
from pymongo import MongoClient
 from bson.objectid import ObjectId
 
from libnmap.reportjson import ReportEncoder
 from libnmap.parser import NmapParser
 from libnmap.plugins.backendplugin import NmapBackendPlugin
 
 
 class NmapMongodbPlugin(NmapBackendPlugin):
     """
        This class handle the persistence of NmapRepport object in mongodb
        Implementation is made using pymongo
        Object of this class must be create via the
        BackendPluginFactory.create(**url) where url is a named dict like
        {'plugin_name': "mongodb"} this dict may reeive all the param
        MongoClient() support
     """
 
     def __init__(self, dbname=None, store=None, **kwargs):
 
     def insert(self, report):
         """
            create a json object from an NmapReport instance
            :param NmapReport: obj to insert
            :return: str id
         """
         j = json.dumps(report, cls=ReportEncoder)
         try:
         return str(oid)
 
     def get(self, str_report_id=None):
        """ select a NmapReport by Id
            :param str: id
            :return: NmapReport object
         """
         rid = str_report_id
         nmapreport = None
 
     def getall(self, dict_filter=None):
         """return a list of tuple (id,NmapReport) saved in the backend
           TODO : add a filter capability
         """
         nmapreportlist = []
         resultset = self.collection.find()
 
     def delete(self, report_id=None):
         """
            delete an obj from the backend
            :param str: id
            :return: dict document with result or None
         """
         if report_id is not None and isinstance(report_id, str):
             return self.collection.remove({"_id": ObjectId(report_id)})