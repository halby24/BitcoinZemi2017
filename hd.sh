#!/usr/bin/env bash

# create a new master private key from a seed and store in file "m"
m=`bx seed | bx hd-new`

# generate the M/0 extended public key
pub=`bx hd-public ${m}`

# generate the m/0 extended private key
priv=`bx hd-private ${m}`

# show the private key of m/0 as a WIF
wifpriv=`bx hd-private ${m} | bx hd-to-ec | bx ec-to-wif`

# show the bitcoin address of M/0
wifaddress=`bx hd-public ${m} | bx hd-to-ec | bx ec-to-address`

# generate m/0/12'/4
#bx hd-private | bx hd-private --index 12 --hard | bx hd-private --index 4

echo -e "Master Private: ${m}\nMaster Public: ${pub}\nChain Code: ${priv}\nWIF private: ${wifpriv}\nWIF address: ${wifaddress}"
