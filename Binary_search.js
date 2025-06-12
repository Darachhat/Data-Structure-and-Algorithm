let list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];

function binarySearch(array, key){
    let left =0;
    let right = array.length - 1;
    while(left <= right){
        const mid = Math.floor((left + right) /2);
        console.log(`Checking middle index: ${mid}, value: ${array[mid]}`); // Log the current middle index and its value
        
        if(array[mid] === key){
            return console.log(`Element found at index: ${mid}`); // Return the index of the target element
        }
        if(array[mid] < key){
            left = mid + 1; // Search in the right half
        } else {
            right = mid - 1; // Search in the left half
        }
        console.log(`Searching in range: ${left} to ${right}`); // Log the current search range
    }
    return console.log(`Element not found`); // Return -1 if the target element is not found
}
binarySearch(list, 8); // Example usage, searching for the number 5

