# -*- coding: utf-8 -*-
# (C) Copyright 2015 Hewlett Packard Enterprise Development LP
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License") you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
##########################################################################

"""
OpenSwitch Test for switchd related configurations.
"""

# from pytest import set_trace
# from time import sleep

TOPOLOGY = """
# +-------+
# |  ops1 |
# +-------+

# Nodes
[type=openswitch name="OpenSwitch 1"] ops1
"""


dutarray = []


def add_bgp_ip_prefix_list_permit_prefix(step):
    step("Test to add ip prefix-list permit prefix configurations")
    plist_created = False
    s1 = dutarray[0]
    s1("configure terminal")
    s1("ip prefix-list test#1 seq 101 permit 10.0.0.1/8")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#1 seq 101 permit 10.0.0.1/8" in line:
            plist_created = True
    assert plist_created is True


def validate_show_ip_prefix_list(step):
    step("Test to validate show ip prefix-list configurations")
    plist_created = False
    s1 = dutarray[0]
    dump = s1("show ip prefix-list")
    lines = dump.split('\n')
    i = 0
    for line in lines:
        if ("ip prefix-list test#1: 1 entries" in lines[i] and
           "seq 101 permit 10.0.0.1/8" in lines[i+1]):
            plist_created = True
        i = i + 1
    assert plist_created is True


def validate_show_ip_prefix_list_seq(step):
    step("Test to validate show ip prefix-list seq configurations")
    plist_created = False
    s1 = dutarray[0]
    dump = s1("show ip prefix-list test#1 seq 101")
    lines = dump.split('\n')
    for line in lines:
        if "seq 101 permit 10.0.0.1/8" in line:
            plist_created = True
    assert plist_created is True


def validate_show_ip_prefix_list_detail(step):
    step("Test to validate show ip prefix-list detail configurations")
    plist_created = False
    s1 = dutarray[0]
    dump = s1("show ip prefix-list detail test#1")
    lines = dump.split('\n')
    i = 0
    for line in lines:
        if (
            "ip prefix-list test#1:" in lines[i] and
            "count: 1, sequences: 101 - 101" in lines[i+1] and
            "seq 101 permit 10.0.0.1/8" in lines[i+2]
        ):
            plist_created = True
        i = i + 1
    assert plist_created is True


def validate_show_ip_prefix_list_summary(step):
    step("Test to validate show ip prefix-list summary configurations")
    plist_created = False
    s1 = dutarray[0]
    dump = s1("show ip prefix-list summary test#1")
    lines = dump.split('\n')
    i = 0
    for line in lines:
        if ("ip prefix-list test#1:" in lines[i] and
           "count: 1, sequences: 101 - 101" in lines[i+1]):
            plist_created = True
        i = i + 1
    assert plist_created is True


def delete_bgp_ip_prefix_list_permit_prefix(step):
    step("Test to delete ip prefix-list permit prefix configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#1 seq 101 permit 10.0.0.1/8")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#1 seq 101 permit 10.0.0.1/8" in line:
            plist_deleted = False
    assert plist_deleted is True


def delete_bgp_ip_prefix_list_word_permit_prefix(step):
    step("Test to delete ip prefix-list permit WORD configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#1")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#1" in line:
            plist_deleted = False
    assert plist_deleted is True


def add_bgp_ip_prefix_list_deny_prefix(step):
    step("Test to add ip prefix-list deny prefix configurations")
    plist_created = False
    s1 = dutarray[0]
    s1("configure terminal")
    s1("ip prefix-list test#2 seq 102 deny 10.0.0.2/8")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#2 seq 102 deny 10.0.0.2/8" in line:
            plist_created = True
    assert plist_created is True


def delete_bgp_ip_prefix_list_deny_prefix(step):
    step("Test to delete ip prefix-list deny prefix configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#2 seq 102 deny 10.0.0.2/8")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#2 seq 102 deny 10.0.0.2/8" in line:
            plist_deleted = False
    assert plist_deleted is True


def delete_bgp_ip_prefix_list_word_deny_prefix(step):
    step("Test to delete ip prefix-list permit WORD deny prefix "
         "configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#2")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#2" in line:
            plist_deleted = False
    assert plist_deleted is True


def add_bgp_ip_prefix_list_permit_prefix_ge(step):
    step("Test to add ip prefix-list permit prefix ge configurations")
    plist_created = False
    s1 = dutarray[0]
    s1("configure terminal")
    s1("ip prefix-list test#3 seq 103 permit 10.0.0.3/8 ge 10")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#3 seq 103 permit 10.0.0.3/8 ge 10" in line:
            plist_created = True
    assert plist_created is True


def delete_bgp_ip_prefix_list_permit_prefix_ge(step):
    step("Test to delete ip prefix-list permit prefix ge configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#3 seq 103 permit 10.0.0.3/8 ge 10")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#3 seq 103 permit 10.0.0.3/8 ge 10" in line:
            plist_deleted = False
    assert plist_deleted is True


def delete_bgp_ip_prefix_list_word_permit_ge(step):
    step("Test to delete ip prefix-list permit WORD permit prefix ge "
         "configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#3")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#3" in line:
            plist_deleted = False
    assert plist_deleted is True


def add_bgp_ip_prefix_list_deny_prefix_ge(step):
    step("Test to add ip prefix-list deny prefix ge configurations")
    plist_created = False
    s1 = dutarray[0]
    s1("configure terminal")
    s1("ip prefix-list test#4 seq 104 deny 10.0.0.4/8 ge 11")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#4 seq 104 deny 10.0.0.4/8 ge 11" in line:
            plist_created = True
    assert plist_created is True


def delete_bgp_ip_prefix_list_deny_prefix_ge(step):
    step("Test to delete ip prefix-list deny prefix ge configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#4 seq 104 deny 10.0.0.4/8 ge 11")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#4 seq 104 deny 10.0.0.4/8 ge 11" in line:
            plist_deleted = False
    assert plist_deleted is True


def delete_bgp_ip_prefix_list_word_deny_ge(step):
    step("Test to delete ip prefix-list permit WORD permit prefix ge "
         "configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#4")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#4" in line:
            plist_deleted = False
    assert plist_deleted is True


def add_bgp_ip_prefix_list_permit_prefix_le(step):
    step("Test to add ip prefix-list permit prefix le configurations")
    plist_created = False
    s1 = dutarray[0]
    s1("configure terminal")
    s1("ip prefix-list test#5 seq 105 permit 10.0.0.3/8 le 10")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#5 seq 105 permit 10.0.0.3/8 le 10" in line:
            plist_created = True
    assert plist_created is True


def delete_bgp_ip_prefix_list_permit_prefix_le(step):
    step("Test to delete ip prefix-list permit prefix "
         "le configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#5 seq 105 permit 10.0.0.3/8 le 10")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#5 seq 105 permit 10.0.0.3/8 le 10" in line:
            plist_deleted = False
    assert plist_deleted is True


def delete_bgp_ip_prefix_list_word_permit_le(step):
    step("Test to delete ip prefix-list permit WORD permit prefix le "
         "configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#5")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#5" in line:
            plist_deleted = False
    assert plist_deleted is True


def add_bgp_ip_prefix_list_deny_prefix_le(step):
    step("Test to add ip prefix-list deny prefix le configurations")
    plist_created = False
    s1 = dutarray[0]
    s1("configure terminal")
    s1("ip prefix-list test#6 seq 106 deny 10.0.0.4/8 le 11")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#6 seq 106 deny 10.0.0.4/8 le 11" in line:
            plist_created = True
    assert plist_created is True


def delete_bgp_ip_prefix_list_deny_prefix_le(step):
    step("Test to delete ip prefix-list deny prefix le configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#6 seq 106 deny 10.0.0.4/8 le 11")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#6 seq 106 deny 10.0.0.4/8 le 11" in line:
            plist_deleted = False
    assert plist_deleted is True


def delete_bgp_ip_prefix_list_word_deny_le(step):
    step("Test to delete ip prefix-list permit WORD deny prefix le "
         "configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#6")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#6" in line:
            plist_deleted = False
    assert plist_deleted is True


def add_bgp_ip_prefix_list_permit_prefix_ge_le(step):
    step("Test to add ip prefix-list permit prefix ge le configurations")
    plist_created = False
    s1 = dutarray[0]
    s1("configure terminal")
    s1("ip prefix-list test#5 seq 105 permit 10.0.0.3/8 ge 10 le 20")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#5 seq 105 permit 10.0.0.3/8 ge 10" in line:
            plist_created = True
    assert plist_created is True


def delete_bgp_ip_prefix_list_permit_prefix_ge_le(step):
    step("Test to delete ip prefix-list permit prefix ge le configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#5 seq 105 permit 10.0.0.3/8 ge 10 le 20")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if ("ip prefix-list test#5 seq 105 permit 10.0.0.3/8 ge 10 "
           "le 20" in line):
            plist_deleted = False
    assert plist_deleted is True


def delete_bgp_ip_prefix_list_word_permit_ge_le(step):
    step("Test to delete ip prefix-list permit WORD permit prefix ge le "
         "configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#5")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#5" in line:
            plist_deleted = False
    assert plist_deleted is True


def add_bgp_ip_prefix_list_deny_prefix_ge_le(step):
    step("Test to add ip prefix-list deny prefix ge le configurations")
    plist_created = False
    s1 = dutarray[0]
    s1("configure terminal")
    s1("ip prefix-list test#6 seq 106 deny 10.0.0.4/8 ge 11 le 21")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if ("ip prefix-list test#6 seq 106 deny 10.0.0.4/8 ge 11 le"
           " 21" in line):
            plist_created = True
    assert plist_created is True


def delete_bgp_ip_prefix_list_deny_prefix_ge_le(step):
    step("Test to delete ip prefix-list deny prefix ge le configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#6 seq 106 deny 10.0.0.4/8 ge 11 le 21")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if ("ip prefix-list test#6 seq 106 deny 10.0.0.4/8 ge 11 le"
           " 21" in line):
            plist_deleted = False
    assert plist_deleted is True


def delete_bgp_ip_prefix_list_word_deny_ge_le(step):
    step("Test to delete ip prefix-list permit WORD permit prefix ge le "
         "configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test#6")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test#6" in line:
            plist_deleted = False
    assert plist_deleted is True


def add_bgp_ip_prefix_list_permit_prefix_any(step):
    step("Test to add ip prefix-list permit prefix any configurations")
    plist_created = False
    s1 = dutarray[0]
    s1("configure terminal")
    s1("ip prefix-list test seq 105 permit any")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test seq 105 permit any" in line:
            plist_created = True
    assert plist_created is True


def delete_bgp_ip_prefix_list_permit_prefix_any(step):
    step("Test to delete ip prefix-list permit prefix "
         "any configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test seq 105 permit any")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test seq 105 permit any" in line:
            plist_deleted = False
    assert plist_deleted is True


def delete_bgp_ip_prefix_list_word_permit_any(step):
    step("Test to delete ip prefix-list permit "
         "WORD permit prefix any configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test" in line:
            plist_deleted = False
    assert plist_deleted is True


def add_bgp_ip_prefix_list_deny_prefix_any(step):
    step("Test to add ip prefix-list deny prefix "
         "any configurations")
    plist_created = False
    s1 = dutarray[0]
    s1("configure terminal")
    s1("ip prefix-list test seq 105 deny any")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test seq 105 deny any" in line:
            plist_created = True
    assert plist_created is True


def delete_bgp_ip_prefix_list_deny_prefix_any(step):
    step("Test to delete ip prefix-list deny prefix "
         "any configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test seq 105 deny any")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test seq 105 deny any" in line:
            plist_deleted = False
    assert plist_deleted is True


def delete_bgp_ip_prefix_list_word_deny_any(step):
    step("Test to delete ip prefix-list permit "
         "WORD deny prefix any configurations")
    plist_deleted = True
    s1 = dutarray[0]
    s1("configure terminal")
    s1("no ip prefix-list test")
    s1("end")
    dump = s1("show running-config")
    lines = dump.split('\n')
    for line in lines:
        if "ip prefix-list test" in line:
            plist_deleted = False
    assert plist_deleted is True


def test_vtysh_ct_bgp_ip_prefix_cli(topology, step):
    ops1 = topology.get("ops1")
    assert ops1 is not None

    global dutarray
    dutarray = [ops1]

    add_bgp_ip_prefix_list_permit_prefix(step)
    validate_show_ip_prefix_list(step)
    validate_show_ip_prefix_list_seq(step)
    validate_show_ip_prefix_list_detail(step)
    validate_show_ip_prefix_list_summary(step)
    delete_bgp_ip_prefix_list_permit_prefix(step)
    delete_bgp_ip_prefix_list_word_permit_prefix(step)
    add_bgp_ip_prefix_list_deny_prefix(step)
    delete_bgp_ip_prefix_list_deny_prefix(step)
    delete_bgp_ip_prefix_list_word_deny_prefix(step)
    add_bgp_ip_prefix_list_permit_prefix_ge(step)
    delete_bgp_ip_prefix_list_permit_prefix_ge(step)
    delete_bgp_ip_prefix_list_word_permit_ge(step)
    add_bgp_ip_prefix_list_deny_prefix_ge(step)
    delete_bgp_ip_prefix_list_deny_prefix_ge(step)
    delete_bgp_ip_prefix_list_word_deny_ge(step)
    add_bgp_ip_prefix_list_permit_prefix_le(step)
    delete_bgp_ip_prefix_list_permit_prefix_le(step)
    delete_bgp_ip_prefix_list_word_permit_le(step)
    add_bgp_ip_prefix_list_deny_prefix_le(step)
    delete_bgp_ip_prefix_list_deny_prefix_le(step)
    delete_bgp_ip_prefix_list_word_deny_le(step)
    add_bgp_ip_prefix_list_permit_prefix_ge_le(step)
    delete_bgp_ip_prefix_list_permit_prefix_ge_le(step)
    delete_bgp_ip_prefix_list_word_permit_ge_le(step)
    add_bgp_ip_prefix_list_deny_prefix_ge_le(step)
    delete_bgp_ip_prefix_list_deny_prefix_ge_le(step)
    delete_bgp_ip_prefix_list_word_deny_ge_le(step)
    add_bgp_ip_prefix_list_permit_prefix_any(step)
    delete_bgp_ip_prefix_list_permit_prefix_any(step)
    delete_bgp_ip_prefix_list_word_permit_any(step)
    add_bgp_ip_prefix_list_deny_prefix_any(step)
    delete_bgp_ip_prefix_list_deny_prefix_any(step)
    delete_bgp_ip_prefix_list_word_deny_any(step)
