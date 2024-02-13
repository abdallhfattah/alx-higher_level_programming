#!/bin/bash

num_files=28

base_name="answer.txt"

for ((i = 1; i <= num_files; i++)); do
    touch "${i}-${base_name}"
done

ls -l *.txt
