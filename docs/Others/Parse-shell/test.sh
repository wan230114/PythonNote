# set -ve
# test1
sleep 1  && echo 1  &
sleep 2  && echo 2  &
sleep 3  && echo 3  &
@echo err1 &
wait

echo sleep ok


@echo err2

echo end
