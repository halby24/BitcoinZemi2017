#!/bin/bash

seed=`bx seed`
priv=`bx ec-new ${seed}`
pub=`bx ec-to-public ${priv}`
address=`bx ec-to-address ${pub}`

echo -e "シードは${seed}だよ"
echo -e "秘密鍵は${priv}だよ"
echo -e "公開鍵は${pub}だよ"
echo -e "アドレスは${address}だよ"

