import json
import re
import sys
import pytest


members_file = open('member_info.json')
members = json.load(members_file)
members_file.close()


def test_a_print_members(capsys):
    """ a_print_members.py should print members """
    import a_print_members
    output = capsys.readouterr().out.strip()
    assert output.endswith(str(members)), "a_print_members.py should print the members variable"

def test_b_print_in_loop(capsys):
    """ b_print_in_loop.py should print each member on a separate line """
    import b_print_in_loop
    last_line = capsys.readouterr().out.strip().split('\n')[-1]
    assert last_line == str(members[-1]), "b_print_in_loop.py should print each member on a separate line"

def test_c_name_variables(capsys):
    """ c_name_variables.py should print each member's name and phone number """
    import c_name_variables
    output = capsys.readouterr().out.strip()
    last_member = members[-1]
    assert last_member[0] in output and last_member[1] in output and last_member[2] not in output, "c_name_variables.py should print members' name and phone number but not address"

def test_d_print_demand_letters(capsys):
    """ d_print_demand_letters.py should print each member's demand letter """
    import d_print_demand_letters
    output = capsys.readouterr().out.strip()
    output = re.sub(r'\s+', r' ', output, flags=re.S)
    for i, member in enumerate(members):
        # address
        address = '%s %s, %s %s' % (member[2], member[3], member[4], member[5])
        assert address in output, "Demand letter %s should include the address '%s':\n\n%s" % (i, address, output[:200])
        output = output.split(address, 1)[1]

        # product
        last_product = member[6][-1]
        last_product_title = re.sub(r'\s+', r' ', last_product[1].title())
        assert last_product_title in output, "Demand letter %s should include the product %s:\n\n%s" % (i, last_product_title, output[:600])
        output = output.split(last_product_title, 1)[1]
        total = str(int(sum(float(product[2]) for product in member[6])))
        assert total in output, "Demand letter %s should include total damages of about $%s (test code only checks for nearest int):\n\n%s" % (i, total, output[:600])
        output = output.split(total, 1)[1]

        # phone number
        assert member[1] in output, "Demand letter %s should include the phone number %s:\n\n%s" % (i, member[1], output[:800])
        output = output.split(member[1], 1)[1]

        # name
        assert member[0] in output, "Demand letter %s should include the name %s:\n\n%s" % (i, member[0], output[:200])
        output = output.split(member[0], 1)[1]


if __name__ == '__main__':
    pytest.main(sys.argv)
