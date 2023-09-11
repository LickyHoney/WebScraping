function createDeque() {
    const items = [];
  
    function isEmpty() {
      return items.length === 0;
    }
  
    function addRear(item) {
      items.push(item);
    }
  
    function addFront(item) {
      items.unshift(item);
    }
  
    function removeFront() {
      if (isEmpty()) {
        return undefined;
      }
      return items.shift();
    }
  
    function removeRear() {
      if (isEmpty()) {
        return undefined;
      }
      return items.pop();
    }
  
    function size() {
      return items.length;
    }
  
    return {
      isEmpty,
      addRear,
      addFront,
      removeFront,
      removeRear,
      size,
      items,
    };
  }
  
  const d = createDeque();
  console.log(d.isEmpty());
  d.addRear(8);
  d.addRear(5);
  d.addFront(7);
  d.addFront(10);
  console.log(d.size());
  console.log(d.isEmpty());
  d.addRear(11);
  console.log(d.removeRear());
  console.log(d.removeFront());
  d.addFront(55);
  d.addRear(45);
  console.log(d.items);
  