 #!/usr/bin/env python
 from sqlalchemy import create_engine
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime, LargeBinary
 from sqlalchemy.ext.declarative import declarative_base
 from sqlalchemy.orm import sessionmaker
 
 from libnmap.plugins.backendplugin import NmapBackendPlugin
from libnmap.reportjson import ReportEncoder, ReportDecoder

import json
from datetime import datetime
 
 Base = declarative_base()
 
 
 class NmapSqlPlugin(NmapBackendPlugin):
     """
        This class handle the persistence of NmapRepport object in SQL backend
        Implementation is made using sqlalchemy(0.8.1)
        usage :

        #get a nmapReport object
        from libnmap.parser import NmapParser
        from libnmap.reportjson import ReportDecoder, ReportEncoder
        import json
        nmap_report_obj = NmapParser.parse_fromfile(
               '/home/vagrant/python-nmap-lib/libnmap/test/files/1_hosts.xml')

         #get a backend with in memory sqlite
         from libnmap.plugins.backendpluginFactory import BackendPluginFactory
         mybackend_mem = BackendPluginFactory.create(plugin_name='sql',
                                                     url='sqlite://',
                                                     echo=True)

         mybackend_mysql = BackendPluginFactory.create(plugin_name='sql',
                            url='mysql+mysqldb://scott:tiger@localhost/foo',
                            echo=True)
         mybackend = BackendPluginFactory.create(plugin_name='sql',
                                        url='sqlite:////tmp/reportdb.sql',
                                        echo=True)
         #lets save!!
         nmap_report_obj.save(mybackend)
         mybackend.getall()
         mybackend.get(1)
     """
 
     class Reports(Base):
         """
            Embeded class for ORM map NmapReport to a
            simple three column table
         """
 
         __tablename__ = "reports"
 
     def __init__(self, **kwargs):
         """
            constructor receive a **kwargs as the **kwargs in the sqlalchemy
            create_engine() method (see sqlalchemy docs)
            You must add to this **kwargs an 'url' key with the url to your
            database
            This constructor will :
            - create all the necessary obj to discuss with the DB
            - create all the mapping(ORM)

            todo : suport the : sqlalchemy.engine_from_config

            :param **kwargs:
            :raises: ValueError if no url is given,
                    all exception sqlalchemy can throw
            ie sqlite in memory url='sqlite://' echo=True
            ie sqlite file on hd url='sqlite:////tmp/reportdb.sql' echo=True
            ie mysql url='mysql+mysqldb://scott:tiger@localhost/foo'
         """
         NmapBackendPlugin.__init__(self)
         self.engine = None
             Base.metadata.create_all(bind=self.engine, checkfirst=True)
             self.Session.configure(bind=self.engine)
         except Exception as e:
            raise(e)
 
     def insert(self, nmap_report):
         """
 
     def get(self, report_id=None):
         """
            retreive a NmapReport from the backend
 
            :param id: str
 
            :returns: NmapReport
         """
         if report_id is None:
             raise ValueError
 
     def getall(self):
         """
            :param filter: Nice to have implement a filter capability
 
            :returns: collection of tuple (id,NmapReport)
         """
         sess = self.Session()
         nmapreportList = []
 
     def delete(self, report_id=None):
         """
            Remove a report from the backend
 
            :param id: str
 
            :returns: The number of rows deleted
         """
         if report_id is None:
             raise ValueError