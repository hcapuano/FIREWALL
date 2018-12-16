import os

from Rule import *

# This function creates a new rule, asking the user to enter different information about the rule.
# Each information entered by the user is stored in a dictionary. Before sending this new rule into our database,
# we check if there are rules with the same id entered, or having a higher id number.
# If yes, we will increment the id of these rules, then we will send our new rule in the database.
# Finally, we display the rules of our database


def rule_creation():
    print(os.system("clear"))
    print_rules()

    print("Enter the different information about your rule:\nPress enter to set the field blank")

    rule = {}

    rule["Position"] = str(input("Index: "))
    rule["Decision"] = str(input("Type: "))
    rule["IpSrc"] = str(input("Ip Source: "))
    rule["IpDst"] = str(input("Ip Destination: "))
    rule["PortSrc"] = str(input("Port Source: "))
    rule["PortDst"] = str(input("Port Destination: "))
    rule["Proto"] = str(input("Protocol: "))

    cursor.execute("SELECT ID FROM RulesConnection ORDER BY ID DESC")
    rules_connection = cursor.fetchall()
    if len(rules_connection) > 0:
        last_rule = rules_connection[0]
        last_id = str(last_rule[0])

        while last_id >= rule["Position"]:
            new_id = str(int(last_id) + 1)
            cursor.execute("UPDATE RulesConnection SET ID=(?) WHERE ID=(?)", (new_id, last_id))
            last_id = str(int(last_id) - 1)

    cursor.execute("""INSERT INTO RulesConnection(ID, IpSrc, IpDst, PortSrc, PortDst, Proto, Decision) 
    VALUES(:Position, :IpSrc, :IpDst, :PortSrc, :PortDst, :Proto, :Decision)""", rule)

    conn.commit()

    print_rules()


rule_creation()
