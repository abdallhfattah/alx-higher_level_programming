#!/usr/bin/node

if (isNaN(parseInt(process.argv[2]))) {
    console.log(1);
} else {
    let result = 1;
    for (let fact = 1; fact <= parseInt(process.argv[2]); fact++) {
        result *= fact;
    }
    console.log(result);
}