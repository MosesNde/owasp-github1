 import logging
 from typing import Any, AsyncGenerator, Literal
 
 from redis import asyncio as aioredis
 
 logger = logging.getLogger(__name__)
 
 
 class Subscriber:
     def __init__(
         self,
         *,
        redis_client: aioredis.Redis,
         topic_name: str,
         group_id: str,
         consumer_id: str,