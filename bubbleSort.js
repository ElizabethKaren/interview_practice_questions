array = [8,5,2,9,5,6,3]

bubbleSort = array => {
    let isSorted = false;
    while (!isSorted) {
        isSorted = true;
        for (let i = 0; i < array.length - 1; i++){
            if (array[i] > array[i+1]){
                swap(i, i+1, array);
                isSorted = false
            }
        }
    }
    return array;
}

swap = (i,j,array) => {
    const temp = array[j];
    array[j] = array[i];
    array[i] = temp;
}


console.log(bubbleSort(array))



