function heapify(arr, n, i) {
    let largest = i;
    const l = 2 * i + 1;
    const r = 2 * i + 2;
  
    if (l < n && arr[i] < arr[l]) {
      largest = l;
    }
  
    if (r < n && arr[largest] < arr[r]) {
      largest = r;
    }
  
    if (largest !== i) {
      [arr[i], arr[largest]] = [arr[largest], arr[i]];
      heapify(arr, n, largest);
    }
  }
  
  function insert(array, newNum) {
    const size = array.length;
    if (size === 0) {
      array.push(newNum);
    } else {
      array.push(newNum);
      for (let i = Math.floor((size / 2) - 1); i >= 0; i--) {
        heapify(array, size, i);
      }
    }
  }
  
  function deleteNode(array, num) {
    const size = array.length;
    let i;
    for (i = 0; i < size; i++) {
      if (num === array[i]) {
        break;
      }
    }
  
    [array[i], array[size - 1]] = [array[size - 1], array[i]];
    array.pop();
  
    for (let i = Math.floor((array.length / 2) - 1); i >= 0; i--) {
      heapify(array, array.length, i);
    }
  }
  
  const arr = [];
  
  insert(arr, 3);
  insert(arr, 4);
  insert(arr, 9);
  insert(arr, 5);
  insert(arr, 2);
  
  console.log("Max-Heap array: " + arr);
  
  deleteNode(arr, 4);
  console.log("After deleting an element: " + arr);
  