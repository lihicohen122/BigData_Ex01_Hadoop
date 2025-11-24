Exercise 1

Q1. How many files are there?
Without SUCCESS: 6
With SUCCESS: 7

Q2. Did number of mapper change?
No

Q3. Did number of reducer changed?
Yes- from 3 to 6

Q4. Did number of output files change? Why?
Yes- from 3 to 6 (without SUCCESS). The number of output files changed because we added more reducers and each reducer has a part file output (we added 6 instead of 3).

Q5. What does the value of 'Merged Map outputs' represents and how is it calculated?
Each reducer gets all mappers. 'Merged Map outputs' represents the number of map output files merged by the intermediate merging logic before being served to reducers. The calculation is mappers times reducers ( in our case 6*9= 54).

Exercise 2

Q1. Is your change in the mapper or in the reducer?
Mapper.

Exercise 3

Q1. Is your change in the mapper or in the reducer?
Reducer.
