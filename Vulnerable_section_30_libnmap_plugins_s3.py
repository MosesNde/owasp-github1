 .. moduleauthor:: Mike Boutillier
 """
 import json
from bson.objectid import ObjectId
from boto.s3.connection import S3Connection, OrdinaryCallingFormat
from boto.s3.key import Key
from boto.s3.bucketlistresultset import bucket_lister
 from boto.exception import S3ResponseError
from libnmap.reportjson import ReportEncoder
 from libnmap.parser import NmapParser
 from libnmap.plugins.backendplugin import NmapBackendPlugin
 
 
 class NmapS3Plugin(NmapBackendPlugin):
     """
        This plugin save the reports on S3 and compatible.
     """
 
     def __init__(self, **kwargs):
         """
            - create the conn object
            - create the bucket (if it doesn't exist)
                - if not given, awsaccessKey_nmapreport
            - may raise exception (ie in case of conflict bucket name)
            - sample :
            To connect to walrus:
            from libnmap.plugins.backendpluginFactory import
                            BackendPluginFactory
            walrusBackend =
              BackendPluginFactory.create(
                    plugin_name='s3',
                    host="walrus.ecc.eucalyptus.com",
                    path="/services/Walrus",port=8773,
                    is_secure=False,
                    aws_access_key_id='UU72FLVJCAYRATLXI70YH',
                    aws_secret_access_key=
                               'wFg7gP5YFHjVlxakw1g1uCC8UR2xVW5ax9ErZCut')
           To connect to S3:
           mybackend_S3 =
             BackendPluginFactory.create(
                plugin_name='s3',
                is_secure=True,
                aws_access_key_id='MYACCESSKEY',
                aws_secret_access_key='MYSECRET')
         """
         NmapBackendPlugin.__init__(self)
         try:
 
     def insert(self, report):
         """
            create a json string from an NmapReport instance
            and push it to S3 bucket.
 
            :param NmapReport: obj to insert
            :rtype: string
            :return: str id
            :todo: Add tagging option
         """
         try:
             oid = ObjectId()
 
     def get(self, str_report_id=None):
         """
            select a NmapReport by Id.
 
            :param str: id
            :rtype: NmapReport
            :return: NmapReport object
         """
         nmapreport = None
         if str_report_id is not None and isinstance(str_report_id, str):
 
     def getall(self, dict_filter=None):
         """
            :rtype: List of tuple
            :return: list of key/report
            :todo: add a filter capability
         """
         nmapreportlist = []
         for key in bucket_lister(self.bucket):
 
     def delete(self, report_id=None):
         """
            delete an obj from the backend
 
            :param str: id
            :return: dict document with result or None
         """
         rcode = None
         if report_id is not None and isinstance(report_id, str):