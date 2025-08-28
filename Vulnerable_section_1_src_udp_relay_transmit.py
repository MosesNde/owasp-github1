                 "Send to (%s, %i) message: %r",
                 remote_relay, self.remote_port, relay_payload,
             )
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(relay_payload, (str(remote_relay), self.remote_port))
 
     def _send_to_relays_packet(self, packet: scapy.packet.Packet):
         """
                 "Send to (%s, %i) message: %r",
                 remote_relay, self.remote_port, pkt_raw,
             )
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(pkt_raw, (str(remote_relay), self.remote_port))
 
         # # Check the packet source. If broadcast a packet with this source in the last
         # # second then we shouldn't do so again