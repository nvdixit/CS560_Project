# CS560_Project
 ## Actual Bugs Found:
 - In the syntax portion for maps, the technique found several bugs in how legal maps were being generated. There are no do-while loops in python, so I had to do some hacky stuff to generate legal maps correctly. The technqiue found some bugs in this convoluted generation code.
 - In the duplicate value semantic portion for maps, the technique found a bug in how values were being processed into the list of tuples in the correct parsing method. I was accidentally trimming too many characters off the start of the value string literal when processing it into the list of tuples used to represent the map in python. The technique found that this was happening.
