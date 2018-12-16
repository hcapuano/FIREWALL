from connection import *

# This class creates rule objects that we retrieve from our database. These rules will allow us to check if
# we can accept a package, thanks to the check.py file. This class has six attributes,
# with their method of access: the source and destination IP addresses, the source and destination ports,
# the protocol of the rule and finally the decision (accept or drop).
class RuleConnectionClass:

    def __init__(self, ip_src, ip_dst, port_src, port_dst, proto, decision):
        self.__ip_src = ip_src
        self.__ip_dst = ip_dst
        self.__port_src = port_src
        self.__port_dst = port_dst
        self.__proto = proto
        self.__decision = decision

    def get_ip_src(self):
        return self.__ip_src

    def get_ip_dst(self):
        return self.__ip_dst

    def get_port_src(self):
        return self.__port_src

    def get_port_dst(self):
        return self.__port_dst

    def get_proto(self):
        return self.__proto

    def get_decision(self):
        return self.__decision

# This function retrieves all created rules from the database and displays them to the user
def print_rules():
    cursor.execute("SELECT * FROM RulesConnection ORDER BY ID")
    rules_connection = cursor.fetchall()
    print("Actual rules: \n")

    for rule_connection in rules_connection:
        print("Index: " + str(rule_connection[0]) + " Type: " + str(rule_connection[6]) +
              " IpSource: " + str(rule_connection[1]) + " IpDestination: " + str(rule_connection[2]) +
              " PortSource: " + str(rule_connection[3]) + " PortDestination: " + str(rule_connection[4]) +
              " Protocol: " + str(rule_connection[5]))

    print('----- \n')

# This function returns the number of columns, not having a null value, from the parameter rule
def get_field_not_null(rule_connection):
    field_not_null = 0

    for value in rule_connection:
        if value != '':
            field_not_null += 1

    return field_not_null - 2
