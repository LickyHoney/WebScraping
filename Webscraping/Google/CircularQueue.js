function createCircularQueue(k) {
    const queue = new Array(k).fill(null);
    let head = -1;
    let tail = -1;
  
    // Insert an element into the circular queue
    function enqueue(data) {
      if ((tail + 1) % k === head) {
        console.log("The circular queue is full");
      } else if (head === -1) {
        head = 0;
        tail = 0;
        queue[tail] = data;
      } else {
        tail = (tail + 1) % k;
        queue[tail] = data;
      }
    }
  
    // Delete an element from the circular queue
    function dequeue() {
      if (head === -1) {
        console.log("The circular queue is empty");
      } else if (head === tail) {
        const temp = queue[head];
        head = -1;
        tail = -1;
        return temp;
      } else {
        const temp = queue[head];
        head = (head + 1) % k;
        return temp;
      }
    }
  
    // Display the circular queue
    function printCQueue() {
      if (head === -1) {
        console.log("No element in the circular queue");
      } else if (tail >= head) {
        for (let i = head; i <= tail; i++) {
          console.log(queue[i]);
        }
      } else {
        for (let i = head; i < k; i++) {
          console.log(queue[i]);
        }
        for (let i = 0; i <= tail; i++) {
          console.log(queue[i]);
        }
      }
    }
  
    return {
      enqueue,
      dequeue,
      printCQueue,
    };
  }
  
  // Your circularQueue object will be instantiated and called as such:
  const circularQueue = createCircularQueue(5);
  circularQueue.enqueue(1);
  circularQueue.enqueue(2);
  circularQueue.enqueue(3);
  circularQueue.enqueue(4);
  circularQueue.enqueue(5);
  
  console.log("Initial queue");
  circularQueue.printCQueue();
  
  circularQueue.dequeue();
  console.log("After removing an element from the queue");
  circularQueue.printCQueue();
  