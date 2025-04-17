#!/bin/bash

dir="average_data"
output_file="average_data_pt_5_correct.txt"

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
