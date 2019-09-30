rows=$(cat file.txt | head -n 1)
i=1
for r in $rows
do
    cat file.txt | awk "{print \$$i}" | tr -s "\n" " "
    printf "\n"
    i=$((i+1))
done
