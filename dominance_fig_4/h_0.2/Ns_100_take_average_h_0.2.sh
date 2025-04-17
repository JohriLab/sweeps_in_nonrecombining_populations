#!/bin/bash

dir="Ns_100_average_data_h_0.2"
output_file="post_fix_h_0.2_more_loci.txt"

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
