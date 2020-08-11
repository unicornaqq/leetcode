# 3Sum.

This is an advanced case of 2sum, fix one value of (x, y, z) and then find a solution for the 2Sum problem.

1. In order to solve the 3Sum problem, need to adjust the 2Sum problem to allow it to return multiple solution.
2. Profiler is the best tool to check the performance, especially the time % used by each steps of the code, and for this case, I have noticed that the original design to avoid the dup item in the final result - some check/search in the list to find out whether the to-be-added item exists in the list or not - this actually introduced some unexpected time complexility.
3. **Set** is a good method/data structure to handle the unique requirements. The element/data type that can be added to a set shoulde be hashable. List is not the case, we can't add a List to a set, since the list is updatable. However, the tuple (), and the string can be added to a list. The same case for the key of the dict, the List can't be used as a key of the dict.
4. Tuple is good alternative to List, especially in the case when the hashable is needed.
5. Pay attention to the boundary cases.