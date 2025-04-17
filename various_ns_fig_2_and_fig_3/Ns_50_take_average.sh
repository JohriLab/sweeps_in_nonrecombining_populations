#!/bin/bash

dir="Ns_50_average_data"
output_file="post_fix_Ns_50.txt"

# Using awk to sum up the values for the same row numbers across files
awk '
{
    sum[$1] += $2; 
    count[$1]++;
}
END {
    for (i in sum) {
        print i, sum[i] / count[i];
    }
}
' $(ls "$dir"/*.txt | sort -V) | sort -n > "$output_file"

echo "Averages written to $output_file."
