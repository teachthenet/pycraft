## TeachCraft 

A series of lessons used to teach middle school and high school kids the fundamentals of programming!

Using Python, each of the lessons will teach the kids new concepts, going through while loops, if statements, for loops,  algorithms, function calls, and the like.

The entire process is collaborative - students are able to see each other's progress as they are all in the same multiplayer server together. Indeed, one of the later lessons constructs a magical system the students can use to battle each other, invoking spells they prepared in code!

All that is needed to get started is downloading the code in this repo and installing java on your system (full instructions in the [setup guide](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/setup.md)).

I have a server up and running with the python api open - all the lessons default to pointing to my server's IP. If you'd like privacy, or if my server is down due to being DOS'ed (easily achievable through it's open python api), you may want to [setup your own server](https://github.com/teachthenet/TeachCraft-Server). If you note my server is down, feel free to open an issue here to inform me to restart it.

My Minecraft server is located at
```
199.96.85.3:25570
```

### Lessons & Setup

[Initial Setup](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/setup.md): Get minecraft running, get connected to the server.

[Lesson 1](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_1.md): Teleport your character to a point you define in code.

[Lesson 2](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_2.md): Make a path of something (flowers, lava, fire) follow behind you while you walk. 

[Lesson 3](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_3.md): Give your character the ability to walk on water (by turning water below your character into ice).

[Lesson 4](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_4.md): Create a building

[Lesson 5](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_5.md): Create a pyramid

[Lesson 6](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_6.md): Use an algorithm to construct the pyramid by analyzing the pattern you discovered in lesson 5!

[Lesson 7](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_7.md): Create a magic system that listens to Minecraft chat, and executes your pre-defined spells!

### Examples / Additional Follow-up

[Import Images to Minecraft](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson8/lesson8.py): Learn how to import an image into minecraft pixel art using Python Imaging Library.

[Build a mini-game: Lavatrap](http://www.stuffaboutcode.com/2015/09/minecraft-game-tutorial-lavatrap-pycon.html) [Link 2](https://docs.google.com/document/d/19YVesJJFS6cg4Ndep7F-TS02CpS0qpN1hlSlv6mgISQ/edit) [Solution](https://github.com/martinohanlon/minecraft-lavatrap/blob/master/lavatrap.py)

[Build An Moving Clock](https://github.com/martinohanlon/minecraft-clock/blob/master/minecraft-clock.py)

[Minecraft Star Wars Animated](https://github.com/martinohanlon/minecraft-starwars)

### Want to host your own server / run a server locally?
- You want to switch to [this repo](https://github.com/teachthenet/TeachCraft-Server)

### Minecraft Docs
- [pi version](http://www.stuffaboutcode.com/p/minecraft-api-reference.html) Has most of the basics of the python api
- [our version](https://github.com/zhuowei/RaspberryJuice) Has the additional things our python api supports, above and beyond the pi version
- [Minecraft block ids](http://minecraft-ids.grahamedgecombe.com/)

### Notes
- Player location from the python api will not match the same retrieved from the server.
    This is because raspberryjuice calculates it from the spawn point, while the server calculates it from 0,0,0.
    To fix, run this as an admin:
    setworldspawn 0 0 0

