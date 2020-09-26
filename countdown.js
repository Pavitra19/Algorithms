// use recursion to implement a countdown counter

function countdown(x) {
    if (x === 0) {
        console.log("done!");
        return;
    } else {
        console.log(`${x}`);
        countdown(x - 1);
    }
}

countdown(4);