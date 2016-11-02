/**
 * Directions Reduction (5 kyu)
 *
 * # Once upon a time, on a way through the old wild west,…
 *
 * … a man was given directions to go from one point to another. The directions
 * were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are
 * opposite, "WEST" and "EAST" too. Going to one direction and coming back the
 * opposite direction is a needless effort. Since this is the wild west, with
 * dreadfull weather and not much water, it's important to save yourself some
 * energy, otherwise you might die of thirst!
 *
 * ## How I crossed the desert the smart way.
 *
 * The directions given to the man are, for example, the following:
 *
 *     plan = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
 *
 * You can immediatly see that going "NORTH" and then "SOUTH" is not
 * reasonable, better stay to the same place! So the task is to give to the man
 * a simplified version of the plan. A better plan in this case is simply:
 *
 *     plan = ["WEST"]
 *
 * Other examples: In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH"
 * + "SOUTH" is going north and coming back right away. What a waste of time!
 * Better to do nothing. The path becomes ["EAST", "WEST"], now "EAST" and
 * "WEST" annihilate each other, therefore, the final result is [] (nil in
 * Clojure). In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH"
 * and "SOUTH" are not
 * directly opposite but they become directly opposite after the reduction o
 * "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].
 *
 * # Task
 *
 * You have to write a function dirReduc which will take an array of strings
 * and returns an array of strings with the needless directions removed (W<->E
 * or S<->N side by side).
 *
 * The Haskell version takes a list of directions with data Direction = North |
 * East | West | South. The Clojure version returns nil when the path is
 * reduced to nothing.
 *
 * # Examples
 *
 *     dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) => ["WEST"] dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]) => []
 *
 *     dirReduc(new String[]{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"}) => new String[]{"WEST"} dirReduc(new String[]{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"}) => new String[]{}
 *
 * # Note
 *
 * All paths can't be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"]
 * is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST"
 * are not directly opposite of each other and can't become such. Hence the
 * result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
 *
 * https://www.codewars.com/kata/550f22f4d758534c1100025a
 */

function dirReduc (arr) {
  let result = [];
  for (let dir of arr) {
    if (result.length && isOpposite(dir, result[result.length - 1])) {
      result.pop();
      continue;
    }
    result.push(dir);
  }
  return result;
}

function isOpposite (dir1, dir2) {
  return (dir1 === 'NORTH' && dir2 === 'SOUTH') ||
         (dir1 === 'SOUTH' && dir2 === 'NORTH') ||
         (dir1 === 'WEST' && dir2 === 'EAST') ||
         (dir1 === 'EAST' && dir2 === 'WEST');
}

const test = require('tape');

test('dirReduc', (t) => {
  t.deepEqual(dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']), ['WEST']);
  t.deepEqual(dirReduc(['NORTH', 'WEST', 'SOUTH', 'EAST']), ['NORTH', 'WEST', 'SOUTH', 'EAST']);
  t.deepEqual(dirReduc(['NORTH', 'SOUTH', 'EAST', 'WEST', 'EAST', 'WEST']), []);
  t.end();
});
