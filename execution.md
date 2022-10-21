### + (increment data)
- data out, changer in /
- changer out, data in /
- counter increment /

### - (decrement data)
- data out, changer in /
- changer sub, changer out, data in /
- counter increment /

### , (get input)
- 
- input await, input out, data in /
- counter increment /

### . (set output)
- data out, output in /
- 
- counter increment /

### < (decrement pointer)
- pointer decrement /
- 
- counter increment /

### > (increment pointer)
- pointer increment /
- 
- counter increment /

### [
- if data zero
  - Latch depth - 1 into target_depth and iterate down the program until depth == target_depth
- if data nonzero
  - pass

### ]
- if data zero
  - pass
- if data nonzero
  - Latch depth into target_depth and iterate up the program until depth == target_depth
