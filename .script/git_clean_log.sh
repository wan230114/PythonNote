#!/usr/bin/bash

tools_path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd $tools_path/..

tail -10000 log >log_tmp
mv log_tmp log

