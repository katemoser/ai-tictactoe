This is my version of a basic AI tictactoe player. 

Starter code and project framing are from CS50ai, a free course from Harvard Extension School that anyone can "take". It's an excellent quality resource!

Although the AI is playing "optimally", I still want to:

- Refactor the code (my `winner` function in particular could be spruced up)
- Add in some alpha-beta pruning to make the `minimax` function more efficient
- Have the AI randomly pick an action to take when there's more than one action with the same utility. Right now it will always pick the first one, which makes it extremely predictable.
