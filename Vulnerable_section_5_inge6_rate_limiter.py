             self.redis_client.expire(ip_key, ip_expire_s)
 
         if ip_key_exists > nof_attempts_s:
            raise TooManyRequestsFromOrigin(
                f"Too many requests from the same ip_address during the last {ip_expire_s} seconds."
            )
 
     def user_limit_test(self, idp_prefix: str, user_limit_key: str) -> None:
         """
         user_limit = int(user_limit)
         timeslot = int(datetime.utcnow().timestamp())
 
        timeslot_key = f"tvs:limiter:{idp_prefix.upper()}:{str(timeslot)}"
         num_users = self.redis_client.incr(timeslot_key)
 
         if num_users == 1:
             self.redis_client.expire(timeslot_key, 2)
 
         if num_users > user_limit:
            raise TooBusyError(
                "Servers are too busy at this point, please try again later"
            )
 
     def rate_limit_test(self, ip_address: str) -> str:
         """
             primary_idp = primary_idp.decode()
         else:
             raise ExpectedRedisValue(
                f"Expected {self.settings.primary_idp_key} key to be set in redis. Please check the primary_idp_key setting"
             )
 
         overflow_idp = self.redis_client.get(self.settings.overflow_idp_key)