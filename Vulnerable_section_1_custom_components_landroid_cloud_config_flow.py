 from homeassistant import config_entries, core, exceptions
 from homeassistant.const import CONF_EMAIL, CONF_PASSWORD, CONF_TYPE
 from pyworxcloud import WorxCloud
 
 from .const import DOMAIN, LOGLEVEL
 from .scheme import DATA_SCHEMA
     worx = WorxCloud(
         data.get(CONF_EMAIL), data.get(CONF_PASSWORD), data.get(CONF_TYPE).lower()
     )
    LOGGER.log(LoggerType.CONFIG, "This works")
    auth = await hass.async_add_executor_job(worx.authenticate)
    LOGGER.log(LoggerType.CONFIG, "So far so good")
     if not auth:
         raise InvalidAuth
    LOGGER.log(LoggerType.CONFIG, "Reached")
 
     return {"title": f"{data[CONF_TYPE]} - {data[CONF_EMAIL]}"}
 