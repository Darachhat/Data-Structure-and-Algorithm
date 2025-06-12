let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function linearSearch(array, target){
    for(i = 0; i<array.length; i++){
        if(array[i] === target){
            return i
            ; // Return the index of the target element
        }
    }
    return -1; // Return -1 if the target element is not found
}

function verify(index){
    if(index === -1){
        return console.log("Element not found");
    }
    else{
        return console.log(`Element found at index: ${index}`); // Log the index of the found element
    }
}

result =linearSearch(array, 4);
verify(result); // Example usage, searching for the number 11