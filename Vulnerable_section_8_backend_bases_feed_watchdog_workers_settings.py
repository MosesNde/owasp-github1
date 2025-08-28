 from pydantic_settings import BaseSettings, SettingsConfigDict
 
 from feed_watchdog.domain.models import BaseModel
         env_prefix="FW_WRK_",
         env_nested_delimiter="__",
         env_file=".env",
     )
 
 
 def get_settings() -> Settings:
     return Settings()