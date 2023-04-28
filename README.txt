James Grime on twitter proposed this problem:
I have a set of dice with values: 0, 0, 0, 0, 2, 3. You roll the dice, add up the total, then roll that number of dice. And repeat. If I start with five dice, how long will the game last?
twitter link: https://twitter.com/jamesgrime/status/1651896236457246721

So I wrote a python program to simulate it.
you can call the rollDice function to play the game once, and takeAverage function to take average iterations of the amount of games you desire.

I ran a 1,000,000 game simulation and found the average to be 5.4858805141194855
