
```bash
unset -v sub
while getopts ":i:d:s:f:" opt
   do
     case $opt in
        i ) initial=$OPTARG;;
        d ) dir=$OPTARG;;
        s ) sub=("$OPTARG")
            until [[ $(eval "echo \${$OPTIND}") =~ ^-.* ]] || [ -z $(eval "echo \${$OPTIND}") ]; do
                sub+=($(eval "echo \${$OPTIND}"))
                OPTIND=$((OPTIND + 1))
            done
            ;;
        f ) files=$OPTARG;;
     esac
done

echo sub: ${sub[@]}
echo sub0: ${sub[0]}
echo sub1: ${sub[1]}
echo files: $files


# sh getopt.sh -i test -d directory -s subdirectory1 subdirectory2 -f file1

# sub: subdirectory1 subdirectory2
# sub0: subdirectory1
# sub1: subdirectory2
# files: file1

```