         self.assertIn('mydf', om_restore.datasets.list())
         self.assertEqual(imported, [meta])
 
     def test_runtime_exporter_export_promote(self):
         om = self.om
         om_restore = self.om_restore