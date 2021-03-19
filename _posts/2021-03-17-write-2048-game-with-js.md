---
layout: post
date: 2021-03-17 16:00:00 +08:00
title:  "Write 2048 Game with Javascript"
---

There is [2048 Game](https://github.com/gabrielecirulli/2048) written by javascript on the Github. The game on the github supports keyboard on PC and touch on mobile devices. 

After browsing [source code](https://github.com/gabrielecirulli/2048/tree/master/js), let's see how to represent the game.  

The game is composed of grid of size 4x4(default size), which is represented by class `Grid`. Grid comprises 16(=4x4) cells, each is represented as class `Tile`. 

When game is on, we need to listen on keyboard events or touch events from users. Thus, class `KeyboardInputManager` is used to monitor all events from users.  

After everything is set, we need to display(paint) the layout on the page, which is handled by class `HTMLActuator`, animated by `window.requestAnimationFrame`.  

In addition, we use class `LocalStorageManager` to store game state.  

Finally, we put all above classes together, use class `GameManager` to keep the game progress smoothly. The key logic of game is handled by `GameManager.move`.  

Note: `*_polyfill.js` files are used for compatibility.

![](/images/2048.jpg)  
*Figure*: <u>Game Structure</u>
