from zeroconf import ServiceBrowser, Zeroconf
import socket


class MyListener:

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            print("Service %s added, service info: %s" % (name, info))
            print(info.__dict__)
            print("Service %s added, IP address: %s" % (name, socket.inet_ntoa(info._addresses[0])))


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_iot._tcp.local.", listener)
try:
    input("Press enter to exit...\n\n")
finally:
    zeroconf.close()
