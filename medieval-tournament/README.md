# Medieval Tournament Simulation

This program simulates a medieval tournament where knights participate in jousting matches. The knights are arranged in a circular formation, and each knight is initially assigned a random strength (between 1 and 100). The game continues over multiple rounds until only one knight remains or all remaining knights have equal strength.

## Tournament Rules

1. **Knights Setup**: Knights are arranged in a circular formation (represented as an array). Each knight is assigned a random strength value between 1 and 100.

2. **Rounds**:

   - Each knight fights the knight to their right by subtracting the opponent's strength from their own.
   - Since the formation is circular, the last knight in the array fights the first knight.
   - All matches in a round occur simultaneously, so strength updates are applied only after all matches are completed.

3. **Defeat and Removal**:
   - If a knight’s strength falls to zero or below after a round, they are defeated and removed from the game in the following round.
4. **End Condition**:
   - The tournament ends when either:
     - Only one knight remains.
     - All remaining knights have equal strength (no further matches can result in a change in strength).

## Objective

Given an initial list of knights' strengths, the program calculates the total number of rounds in the tournament.

## Example

If the initial strengths are `[45, 32, 78, 51, 62]`, the simulation will calculate and return the number of rounds until a winner is determined or no more moves are possible.

## Implementation

To implement this simulation:

- Initialize an array of knights with random strength values.
- Run rounds according to the rules above.
- Track the number of rounds and output this value when the end condition is met.
