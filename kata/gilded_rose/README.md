# Gilded Rose

![LeanDog Logo](assets/Gilded-Rose-Kata.png)

## Overview

The Gilded Rose Kata is a classic code kata for practicing refactoring skills. It involves a small inn with a prime location in a prominent city run by a friendly innkeeper named Allison. The inn sells only the finest goods, but unfortunately, the goods degrade in quality as they approach their sell-by date. Your task is to add a new feature to this existing system.

## Gilded Rose Requirements Specification

Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a prominent city run by a friendly innkeeper named Allison. We also buy and sell only the finest goods.

Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. We have a system in place that updates our inventory for us.

It was developed by a guy named Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that we can begin selling a new category of items. First an introduction to our system:

- All items have a SellIn value which denotes the number of days we have to sell the item.
- All items have a Quality value which denotes how valuable the item is.
- At the end of each day our system lowers both values for every item.

Pretty simple, right? Well this is where it gets interesting:

- Once the sell by date has passed, Quality degrades twice as fast.
- The Quality of an item is never negative.
- "Aged Brie" increases in Quality the older it gets.
- The Quality of an item is never more than 50, but "Sulfuras" is a legendary item and as such its Quality is always 80 and it never alters.
- "Backstage passes", like "Aged Brie", increases by one in Quality as its SellIn date approaches
  - Quality increases by 2 when there are 10 days or less
  - Quality increases by 3 when there are 5 days or less
  - Quality drops to 0 after the concert

We have recently signed a supplier of conjured items. This requires AN UPDATE to our system:

- "Conjured" items degrade in Quality twice as fast as normal items

Feel free to make any changes to the UpdateQuality method and add any new code as long as everything still works correctly. However, do not alter the Item class or Items property as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code ownership (you can make the UpdateQuality method and Items property static if you like, we'll cover for you.)

Just for clarification, an item can never have its Quality increase above 50.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/DEV3L/python-katas
cd python-katas/kata/gilded_rose
```

2. Setup a virtual environment with dependencies and activate it:

```bash
brew install hatch
hatch env create
hatch shell
```

2. Run the main script:

```bash
hatch run gilded_rose
```

## Testing

### Unit Tests

```bash
hatch run test
```

With coverage for Coverage Gutters:

```bash
hatch run test

Command + Shift + P => Coverage Gutters: Watch
```
