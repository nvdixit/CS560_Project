# CS560_Project 
Nikhil Dixit, Jimson Huang, Stephan Zapodeanu

## Execution Instructions:
Navigate to each subdirectory depending on which syntactic or semantic property is wanted.
If testing a Graph or Map property, run testing.py (for syntax) or testing_*.py (for semantic).
If testing a  Binary Tree, run verify_bt.py (for syntax) or verify_bt_*.py (for semantic).

For example, to run the map syntax tester from the root directory of the project:
```
cd Map/Syntax
python testing.py
```

To run the Data Structure generation go to the specified subdirectory and run generate_legal_*.py or generate_illegal_*.py files.

For example, to run the map syntax legal and illegal generator from the root directory of the project:
```
cd Map/Syntax
python generate_legal_map.py
python generate_illegal_map.py
```

## Actual Bugs Found:
 - In the syntax portion for maps, the technique found several bugs in how legal maps were being generated. There are no do-while loops in python, so I had to do some hacky stuff to generate legal maps correctly. The technqiue found some bugs in this convoluted generation code.
 - In the duplicate value semantic portion for maps, the technique found a bug in how values were being processed into the list of tuples in the correct parsing method. I was accidentally trimming too many characters off the start of the value string literal when processing it into the list of tuples used to represent the map in python. The technique found that this was happening.
- In the adjacency list semantic portion for maps, the technique found a bug in the code that checked that no vertex connects to a vertex that doesn't exist. I was not processing when vertices have no outgoing edges correctly and was not checking for the existance of each vertex in each adjacency list in the map correctly.
