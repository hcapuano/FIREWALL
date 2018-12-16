from netfilterqueue import NetfilterQueue
from check import *
from scapy.layers.inet import IP
from Rule import *

print(os.system("clear"))
print("OK")
print_rules()


# This function handles if the packet must be accepted. The nfqueue packet from the parameter
# is converted into a Scapy packet. Then we send this Scapy package to another function named check_packet,
# which will return the decision, if we have to accept the packet.
def packet_manager(pkt):

    # print(pkt)
    packet = IP(pkt.get_payload())
    decision = check_packet(packet)
    print("decision = ", decision)
    if decision:
        print('Accepted')
        pkt.accept()
    else:
        print('Drop')


print("Welcome to SupFireWall !! \n")

# We create two nfqueue thanks to iptables by assigning them a number and a type (Input / output)
print(os.system("iptables -F"))
print(os.system("iptables -A INPUT -j NFQUEUE --queue-num 1"))
print(os.system("iptables -A OUTPUT -j NFQUEUE --queue-num 2"))

# We bind our nfqueue two times, assigning them the function "packet_manager"
nfqueue = NetfilterQueue()
nfqueue.bind(1, packet_manager)
nfqueue.bind(2, packet_manager)

# We run nfqueue, which will be able to detect all the packets circulating in our network,
# and will accept or block these packets
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

# We unbind our nfqueue
nfqueue.unbind()
