#!/usr/bin/env python3

# This utility will attempt to find an EmpireAI user by their phone number
#
# Arguments:
#   -p|--phone
#
# This makes use of the EmpyreAI module and ultimately the Base Command API
#   to provide user management capabilities to coordinators without requiring
#   elevated privileges on the cluster.
#
# Return Codes:
#   0 = Success
#   1 = Unknown Error
#   100 = Missing argument
#
# Author: Kali McLennan (Flatiron Institute) - kmclennan@flatironinstitute.org

import EmPyreAI.EmpireAPI
from EmPyreAI.EmpireUser import EmpireUser
import EmPyreAI.EmpireUtils as EUtils
import os
import getpass
import sys
from prettytable import PrettyTable
import argparse as ap
import json
import subprocess

def ParseArgs():
    parser = ap.ArgumentParser()
    parser.add_argument("-p", "--phone", type=str, help="The users phone number.", action="store")
    args = parser.parse_args()

    if args.phone == None:
        print("The phone number to search for is a required flag. Please use [-p|--phone] to provide this information.")
        sys.exit(100)

    args.phone = args.phone.strip().replace('-','').replace('(', '').replace(')', '')

    return args

if __name__ == "__main__":
    if not (EUtils.CheckAPI()):
        print("At least one API access key or certificate file is not present. You will not be able to interact with the Base Command API without these files.")
        sys.exit(1)

    args = ParseArgs()

    all_user_data = EmPyreAI.EmpireAPI.CMSH_Cluster.get_by_type('User')

    for entry in all_user_data:
        if len(entry["notes"]) > 0:
            try:
                entry_phone = json.loads(entry["notes"])["phone"]
                match_phone = entry_phone.strip().replace('-','').replace('(', '').replace(')', '')
                if match_phone == args.phone:
                    print(f"Found a matching user named {entry['name']}!")
            except Exception as e:
                pass
