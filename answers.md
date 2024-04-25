# CMPS 2200 Recitation 08

## Answers

**Name:** Nicole Davis
**Name:** Cece Haase


Place all written answers from `recitation-08.md` here for easier grading.



- **1a)**

  The work of the algorithm can be calculated by looking at the number of vertices and edges in the graph. The initialization of the dictionary will be O(|V|), where V is the number of vertices we are working with.
  Given the loop irerates icer each vertex and edge of the graph, updating the shortest path info, it would execute O(|V| + |E|) times, given E is number of edges. The time it takes to update is constant, so the work is O(|V| + |E|).

  The initialization of the dictionary is done in parallel, so it has a span of O(1), then we look to the main loop which cannot be parallelized because it has to constantly update the shortest path info because it's data dependent. Each iteration is dependent on what results from the previous iteration, so the span would be O(|V|+|E|).








