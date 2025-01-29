#!/bin/bash

TGT_USER=$1

touch /mnt/home/$TGT_USER/.new_user_$TGT_USER
chown $TGT_USER:$TGT_USER /mnt/home/$TGT_USER/.new_user_$TGT_USER