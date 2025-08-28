                 raise OSError(E_ADDR_IN_USE[0], "")
             self.srv.append(srv)
         except (OSError, socket.error) as ex:
             if ex.errno in E_ADDR_IN_USE:
                 e = "\033[1;31mport {} is busy on interface {}\033[0m".format(port, ip)
             elif ex.errno in E_ADDR_NOT_AVAIL: