from scapy.layers.inet import*
from Rule import *

# This function returns the object according to the protocol of the packet, as well as the name of the object
def get_protocol(packet_object):

    protocol = packet_object[IP].proto

    dict_protocol = {6: [TCP, "TCP"], 17: [UDP, "UDP"], 1: [ICMP, "ICMP"]}

    if protocol in dict_protocol.keys():
        return dict_protocol[protocol][0], dict_protocol[protocol][1]

# This function compares each field of the rule with those of the packet being checked
def rule_packet_match(rule_object, packet_object, field_not_null):

    protocol, protocol_string = get_protocol(packet_object)
    port_src = packet_object[protocol].sport
    port_dport = packet_object[protocol].dport

    valid_field = 0

    if rule_object.get_ip_src() != "" and rule_object.get_ip_src() == packet_object[IP].src:
        valid_field += 1

    if rule_object.get_ip_dst() != "" and rule_object.get_ip_dst() == packet_object[IP].dst:
        valid_field += 1

    if rule_object.get_proto() != "" and rule_object.get_proto() == protocol_string:
        valid_field += 1

    if rule_object.get_port_src() != 0 and rule_object.get_port_src() == port_src:
        valid_field += 1

    if rule_object.get_port_dst() != 0 and rule_object.get_port_dst() == port_dport:
        valid_field += 1

    if valid_field == field_not_null:
        return True

    return False

# This function fetches all the rules of the database, depending on the id in ascending order.
# For each of the rules we compare the fields with the current packet thanks to the "rule_packet_match" function.
# Finally, the function returns us a Boolean
def check_packet(packet):

    cursor.execute("SELECT * FROM RulesConnection ORDER BY ID ASC")

    rules_connection = cursor.fetchall()

    for rule_connection in rules_connection:
        field_not_null = get_field_not_null(rule_connection)

        rule_object = RuleConnectionClass(rule_connection[1], rule_connection[2], rule_connection[3],
                                          rule_connection[4], rule_connection[5], rule_connection[6])

        check_in = rule_packet_match(rule_object, packet, field_not_null)
        if check_in:
            if rule_object.get_decision() == "accept":
                return True
            else:
                return False
    return False
