 
 from apscheduler.schedulers.asyncio import AsyncIOScheduler
 from apscheduler.triggers.cron import CronTrigger
from dependency_injector.wiring import Provide, inject
 
 from feed_watchdog.api_client.client import FeedWatchdogAPIClient
 from feed_watchdog.commands.core import BaseCommand
 from feed_watchdog.domain.events import ProcessStreamEvent
 from feed_watchdog.pubsub.publisher import Publisher
from feed_watchdog.workers.container import Container
from feed_watchdog.workers.settings import Settings
 
 logger = logging.getLogger(__name__)
 
 @inject
 async def add_interval_jobs(
     scheduler: AsyncIOScheduler,
    api_client: FeedWatchdogAPIClient = Provide[Container.feed_watchdog_api_client],
 ) -> None:
     for interval in await api_client.get_intervals():
         collect = partial(collect_and_publish_streams, interval)
 @inject
 async def collect_and_publish_streams(
     cron_interval: str,
    api_client: FeedWatchdogAPIClient = Provide[Container.feed_watchdog_api_client],
    settings: Settings = Provide[Container.settings],
 ) -> None:
     logger.info("Collecting streams for %s", cron_interval)
     streams = await api_client.get_streams(interval=cron_interval)
 async def send_events(
     topic_name,
     events: Iterable[ProcessStreamEvent],
    publisher: Publisher = Provide[Container.publisher],
 ) -> None:
     i = 0
     for i, event in enumerate(events, start=1):  # noqa: B007