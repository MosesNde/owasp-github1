import asyncio
 import logging
 import uuid
 from dataclasses import asdict
 from typing import Sequence
 
from dependency_injector.wiring import Provide, inject
 
 from feed_watchdog.commands.core import BaseCommand
 from feed_watchdog.domain.events import (
 from feed_watchdog.domain.models import Post
 from feed_watchdog.handlers import HandlerType, get_handler_by_name
 from feed_watchdog.pubsub.publisher import Publisher
 from feed_watchdog.repositories.post import RedisPostRepository
 from feed_watchdog.sentry.error_tracking import write_warn_message
from feed_watchdog.workers.container import Container, container
from feed_watchdog.workers.settings import Settings
 
 logger = logging.getLogger(__name__)
 
 
 class ProcessStreamsByScheduleWorker(BaseCommand):
     @inject
    def setup(
         self,
        settings: Settings = Provide[Container.settings],
        post_repository: RedisPostRepository = Provide[Container.post_repository],
        publisher: Publisher = Provide[Container.publisher],
     ) -> None:
         self._settings = settings
         self._post_repository = post_repository
         self._publisher = publisher
        self._subscriber = container.subscriber(
             topic_name=self._settings.app.streams_topic,
             group_id="fetch_posts_from_streams",
             consumer_id=uuid.uuid4().hex,
         )
 
    def handle(self, args) -> None:  # noqa: U100
        asyncio.run(self.process_streams(), debug=True)
 
     async def process_streams(self) -> None:
         logger.info("Start processing streams for fetching")