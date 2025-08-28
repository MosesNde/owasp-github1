import asyncio
 import logging
 import uuid
 
from dependency_injector.wiring import Provide, inject
 
 from feed_watchdog.api_client.client import FeedWatchdogAPIClient, StreamResp
 from feed_watchdog.commands.core import BaseCommand
 from feed_watchdog.domain.events import MessageBatch
 from feed_watchdog.handlers import HandlerType, get_handler_by_name
from feed_watchdog.workers.container import Container, container
from feed_watchdog.workers.settings import Settings
 
 logger = logging.getLogger(__name__)
 
 
 class ProcessStreamsByScheduleWorker(BaseCommand):
     @inject
    def setup(
         self,
        settings: Settings = Provide[Container.settings],
        api_client: FeedWatchdogAPIClient = Provide[Container.feed_watchdog_api_client],
     ) -> None:
         self._settings = settings
         self._api_client = api_client
        self._subscriber = container.subscriber(
             topic_name=self._settings.app.messages_topic,
             group_id="send_messages",
             consumer_id=uuid.uuid4().hex,
         )
 
    def handle(self, args) -> None:  # noqa: U100
        asyncio.run(self.process_messages(), debug=True)
 
     async def process_messages(self) -> None:
         logger.info("Start processing messages for sending")