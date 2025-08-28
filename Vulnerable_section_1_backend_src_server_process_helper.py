         self._port = _find_free_port()
         self._base_url = f"http://127.0.0.1:{self._port}"
         self._session = None
 
     async def start(self, flags: Iterable[str] = []):
        logger.info("Starting worker process...")
         self._process = _WorkerProcess([str(self._port), *flags])
         self._session = aiohttp.ClientSession(base_url=self._base_url)
         await self.wait_for_ready()
         logger.info("Worker process started")
 
         logger.info("Worker process stopped")
 
     async def restart(self, flags: Iterable[str] = []):
         await self.stop()
         await self.start(flags)
 
     async def wait_for_ready(self, timeout: float = 300):
        start = time.time()
        while time.time() - start < timeout:
            if (
                self._process is not None
                and self._session is not None
                and _port_in_use(self._port)
            ):
                try:
                    await self._session.get("/nodes", timeout=5)
                    return
                except Exception:
                    pass
 
             await asyncio.sleep(0.1)
 
        raise TimeoutError("Server did not start in time")
 
     async def proxy_request(self, request: Request, timeout: int | None = 300):
        await self.wait_for_ready()
        assert self._session is not None
         if request.route is None:
             raise ValueError("Route not found")
         async with self._session.request(
             request.method,
             f"/{request.route.path}",
         await self.wait_for_ready()
         assert self._session is not None
         logger.debug("Fetching packages...")
        packages_resp = await self._session.get(
             "/packages", params={"hideInternal": "false"}
        )
        packages_json = await packages_resp.json()
        packages = [Package.from_dict(p) for p in packages_json]
        return packages