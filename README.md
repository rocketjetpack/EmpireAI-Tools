# Empire AI Logo

## Empire AI Account Manager

## Overview
This repo contains the account management scripts for the Empire AI Alpha project. 

### How Does it Work?
This codebase makes use of the Nvidia Base Command `pythoncm` Python module to access the Base Command API according to the
[Nvidia Base Command Developer Manual](https://support.brightcomputing.com/manuals/10/developer-manual.pdf)

### What Scripts are There?
The scripts in this repository are broken down into cron and interactive scripts:

|Name|Type|Description|
|:-|-|-|
|eai_new_user|Interactive|Enables coordinator role users to create new EmpireAI users.|
|eai_reset_password|Interactive|Enables coordinator role users to reset the password of EmpireAI users.|
|eai_cron_new_users|Cron|This script polls Base Command for users and ensures that Lustre directories and Slurm accounts are configured correctly.|
|eai_rotate_partition_prio|Cron|This script should run weekly via Cron and will rotate which partition has priority for preemption.|

### Other Information
[Base Command Developer Manual](https://support.brightcomputing.com/manuals/10/developer-manual.pdf)

## Installation
This repo is intended to be cloned to /opt/EmpireAI-Tools. 
Once cloned, do the following:
- Copy `share/zz_modulepath.sh` to `/etc/profile.d`
- Copy the contents of `share/crontab.entries` and paste into `crontab -e`

## Tool Documentation
### eai_new_user
User information may be passed to eai_new_user in several different ways:
- Specify `eai_new_user -I` to run interactive where you will be prompted to enter all the necessary information.
- Review the `eai_new_user --help` screen on how to specify all the necessary information via command line arguments.
- Use the `eai_new_user -B filename.yaml` argument to run in batch mode with input from filename.yaml

### eai_reset_password
This tool is used to randomize user passwords. This should be used if a user has forgotten their password or when a new user is requesting their initial password. There are two flags, one required and one optional:
- `-u USERNAME` Required: Specify the username of the account to reset the password for.
- `-l INT` Optional: Specify the length of the generated password (default: 15, minimum: 10)

Note: This tool does not generate a *completely* random password. The list of characters that can appear in passwords has been restricted slightly to ensure that generated passwords lack characters that can be difficult to tell apart in many fonts, such as `l` and `1` or `O` and `0`. As a result, longer passwords are preferred to ensure sufficient entropy to prevent brute force attacks on newly created accounts.

