 
             if not ip_profile.get("subnet_address"):
                 # Fake subnet is required
                subnet_rand = random.randint(0, 255)
                 ip_profile["subnet_address"] = "192.168.{}.0/24".format(subnet_rand)
 
             if "ip_version" not in ip_profile: