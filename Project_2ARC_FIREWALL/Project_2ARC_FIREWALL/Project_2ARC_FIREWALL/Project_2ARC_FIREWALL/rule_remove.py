from Rule import *

# This function deletes a rule from our database, thanks to the input entered by the user.
# Before sending this new rule into our database, we check if there are rules having a higher id number.
# If yes, we will decrement the id of these rules. Finally, we display the rules of our database.


def rule_remove():
    print_rules()
    id_remove = int(input("Enter the ID of the rule you want to remove: "))

    cursor.execute("DELETE FROM RulesConnection WHERE ID = (?)", str(id_remove))
    id_remove = str(int(id_remove) + 1)

    cursor.execute("SELECT ID FROM RulesConnection ORDER BY ID DESC")
    rules_connection = cursor.fetchall()
    if len(rules_connection) > 0:
        last_rule = rules_connection[0]
        last_id = str(last_rule[0])

        while id_remove <= last_id:
            new_id = str(int(id_remove) - 1)
            cursor.execute("UPDATE RulesConnection SET ID = ? WHERE ID = ?", (new_id, id_remove))
            id_remove = str(int(id_remove) + 1)

    print_rules()
    conn.commit()


rule_remove()
