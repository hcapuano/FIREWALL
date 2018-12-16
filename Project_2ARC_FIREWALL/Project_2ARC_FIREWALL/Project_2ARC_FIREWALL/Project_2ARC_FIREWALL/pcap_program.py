from check import *
from scapy.all import *


# This function handles if the packet must be accepted. We send this Scapy package to another
# function named check_packet, which will return the decision, if we have to accept the package.
def packet_manager(packet):

    decision = check_packet(packet)
    if decision:
        print('Accepted')
    else:
        print('Drop')

# We retrieve all the packages from the "pcap" file in our "packets" variables.
# Then, we create a variable "count" which will be incremented later,
# in order to know which decision belongs to which packet. Then, we create an iteration that will loop for each packet
# of the "packets" variable. The packet number and its information are displayed.
# Finally we send our packet in the function "packet_manager" to know the decision, if we accept the package.
if __name__ == '__main__':

    try:
        packets = rdpcap("capture.pcap")
        count = 1
        for packet in packets:
            print("Packet n°:", count)
            packet.show() # You need to comment this statement to see only the decision (accept / drop)
            packet_manager(packet)
            count += 1
    except KeyboardInterrupt:
        print('Error')
