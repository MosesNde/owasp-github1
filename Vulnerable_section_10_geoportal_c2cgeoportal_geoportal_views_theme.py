 from c2cgeoportal_commons import models
 from c2cgeoportal_commons.lib.url import Url, get_url2
 from c2cgeoportal_commons.models import cache_invalidate_cb, main
 from c2cgeoportal_geoportal.lib import get_roles_id, get_typed, get_types_map, is_intranet
 from c2cgeoportal_geoportal.lib.caching import get_region
 from c2cgeoportal_geoportal.lib.common_headers import Cache, set_common_headers
             models.DBSession.query(main.OGCServer).filter_by(id=self.request.matchdict.get("id")).one()
         )
         came_from = self.request.params.get("came_from")
         if came_from:
             raise pyramid.httpexceptions.HTTPFound(location=came_from)
         return {"success": True}