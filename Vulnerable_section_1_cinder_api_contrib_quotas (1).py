 QUOTAS = quota.QUOTAS
 
 
authorize_update = extensions.extension_authorizer('compute', 'quotas:update')
authorize_show = extensions.extension_authorizer('compute', 'quotas:show')
 
 
 class QuotaTemplate(xmlutil.TemplateBuilder):
 
     name = "Quotas"
     alias = "os-quota-sets"
    namespace = "http://docs.openstack.org/compute/ext/quotas-sets/api/v1.1"
     updated = "2011-08-08T00:00:00+00:00"
 
     def get_resources(self):