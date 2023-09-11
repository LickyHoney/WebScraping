// Creating a stack
function createStack() {
    const stack = [];
    return stack;
  }
  
  // Creating an empty stack
  function checkEmpty(stack) {
    return stack.length === 0;
  }
  
  // Adding items into the stack
  function push(stack, item) {
    stack.push(item);
    console.log("pushed item: " + item);
  }
  
  // Removing an element from the stack
  function pop(stack) {
    if (checkEmpty(stack)) {
      return "stack is empty";
    }
  
    return stack.pop();
  }
  
  const stack = createStack();
  push(stack, "1");
  push(stack, "2");
  push(stack, "3");
  push(stack, "4");
  console.log("popped item: " + pop(stack));
  console.log("stack after popping an element: " + stack);
  