# Congkak

## Background
Congkak is a South East Asian mancala game, which is a two-player turn-based strategy board games played with small stones, beans, or seeds and rows of holes or pits in the earth (https://en.wikipedia.org/wiki/Southeast_Asian_mancala).

There are various variations on the rules of the game, but this project sets out to implement a base set of rules that the author grew up with.

## Terminology

On a Congkak board, there are 7 'pits' on each side, and a 2 warehouses at each end - one for each player.
The player's warehouse is on the lefthand side of the board on the player's perspective.


```
                Player 2
        /-[ 0, 0, 0, 0, 0, 0, 0]-\  [00]
       <-------------------------->
   [00] \-[ 0, 0, 0, 0, 0, 0, 0]-/
                Player 1
```
## Rules
On a player's turn, they may choose one of pits on their side, and distribute one marble per pit in a clockwise direction. They should start distributing one pit after the selected pit.
Example:
```
                Player 2                                          Player 2
        /-[ 0, 0, 0, 0, 0, 0, 0]-\  [00]                 /-[ 0, 0, 0, 0, 0, 0, 0]-\  [00]
       <-------------------------->       ------>       <-------------------------->
  [00]  \-[ 0, 0, 0, 2, 0, 4, 0]-/                 [00]  \-[ 0, 1, 1, 3, 1, 0, 0]-/
                Player 1                                          Player 1
```

*ONLY* when distributing on their own side, the player should put one marble in their warehouse after crossing over the left-most pit.

Example 1:
```
Player 1's go, 1 turn remaining

                Player 2                                          Player 2
        /-[ 0, 0, 0, 0, 0, 0, 0]-\  [00]                 /-[ 1, 1, 0, 0, 0, 0, 0]-\  [00]
       <-------------------------->       ------>       <-------------------------->
  [00]  \-[ 0, 4, 0, 0, 0, 0, 0]-/                 [01]  \-[ 1, 0, 0, 0, 0, 0, 0]-/
                Player 1                                          Player 1

It is now Player 2's go, 1 turn remaining
```

Example 2:
```
Player 1's go, 1 turn remaining

                Player 2                                          Player 2
        /-[ 0, 0, 0, 0, 0, 0, 0]-\  [00]                 /-[ 1, 1, 1, 1, 1, 1, 1]-\  [00]
       <-------------------------->       ------>       <-------------------------->
  [00]  \-[ 0,11, 0, 0, 0, 0, 0]-/                 [01]  \-[ 1, 0, 0, 0, 0, 1, 1]-/
                Player 1                                          Player 1

It is now Player 2's go, 1 turn remaining
```

## Special Cases
There are a few Special Cases that is triggered by where the last marble lands. They are discussed below:

### Free Turn
If the final marble lands on your own warehouse, you get an additional turn

Example:
```
Player 1's go, 1 turn remaining

                Player 2                                          Player 2
        /-[ 0, 0, 0, 0, 0, 0, 0]-\  [00]                 /-[ 0, 0, 0, 0, 0, 0, 0]-\  [00]
       <-------------------------->       ------>       <-------------------------->
  [00]  \-[ 0, 2, 0, 0, 0, 0, 0]-/                 [01]  \-[ 1, 0, 0, 0, 0, 0, 0]-/
                Player 1                                          Player 1

It is now Player 1's go, 1 turn remaining
```

### Steal
If the final marble lands on an empty pit on the player's own side, the player steals the opposing player's marbles on the pit parallel to the landed pit

Example:
```
Player 1's go, 1 turn remaining

                Player 2                                          Player 2
        /-[ 0, 0,12, 0, 0, 0, 0]-\  [00]                 /-[ 0, 0, 0, 0, 0, 0, 0]-\  [00]
       <-------------------------->       ------>       <-------------------------->
  [00]  \-[ 0, 0, 0, 0, 2, 0, 0]-/                 [12]  \-[ 0, 0, 1, 1, 0, 0, 0]-/
                Player 1                                          Player 1

It is now Player 2's go, 1 turn remaining
```

### Lose Turn
If the final marble lands on an empty pit on the opponent's side, the player's turn ends immediately and the opponent gets 2 turns

Example:
```
Player 1's go, 2 turns remaining

                Player 2                                          Player 2
        /-[ 1, 0, 1, 2, 3, 4, 0]-\  [00]                 /-[ 1, 1, 1, 2, 3, 4, 0]-\  [00]
       <-------------------------->       ------>       <-------------------------->
  [00]  \-[ 0, 0, 5, 0, 0, 0, 0]-/                 [01]  \-[ 0, 0, 0, 0, 0, 0, 0]-/
                Player 1                                          Player 1

It is now Player 2's go, 2 turns remaining
```

## End of Game
The game ends when either side reaches 0 Marbles, and the winner is the player with the most marbles.
