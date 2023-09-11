// class Queue {
//     constructor() {
//       this.queue = [];
//     }
  
//     // Add an element
//     enqueue(item) {
//       this.queue.push(item);
//     }
  
//     // Remove an element
//     dequeue() {
//       if (this.queue.length < 1) {
//         return null;
//       }
//       return this.queue.shift();
//     }
  
//     // Display the queue
//     display() {
//       console.log(this.queue);
//     }
  
//     size() {
//       return this.queue.length;
//     }
//   }
  
//   const q = new Queue();
//   q.enqueue(1);
//   q.enqueue(2);
//   q.enqueue(3);
//   q.enqueue(4);
//   q.enqueue(5);
  
//   q.display();
  
//   q.dequeue();
  
//   console.log("After removing an element");
//   q.display();
  

// Using Function

function createQueue() {
    const queue = [];
  
    function enqueue(item) {
      queue.push(item);
    }
  
    function dequeue() {
      if (queue.length < 1) {
        return null;
      }
      return queue.shift();
    }
  
    function display() {
      console.log(queue);
    }
  
    function size() {
      return queue.length;
    }
  
    return {
      enqueue,
      dequeue,
      display,
      size
    };
  }
  
  const q = createQueue();
  q.enqueue(1);
  q.enqueue(2);
  q.enqueue(3);
  q.enqueue(4);
  q.enqueue(5);
  
  q.display();
  
  q.dequeue();
  
  console.log("After removing an element");
  q.display();
  