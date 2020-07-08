#!/usr/bin/node
const args = process.argv.slice(2);
let biggest = args[0];
let nextbiggest = args[0];
if (args[0]) {
    if (args[0] == 1) { console.log(0); } else {
    for(var i=0;i<args.length;i++){
        if(args[i]>biggest){
            nextbiggest = biggest;
            biggest = args[i];
        }
        else if(args[i]>nextbiggest && args[i]!=biggest)
            nextbiggest = args[i];
    }
    console.log(nextbiggest);
    }
} else { console.log(0); }
