##### To Run
Decide on a username you want to use.

Double click Minecraft_Launcher.jar, choose Release 1.8.7
```
- In the bottom left, type in your chosen username.
- In the bottom left, choose Release 1.8.7
- If the button in the bottom middle says "Install", click it.
- Now click the button in the bottom middle that says Play.
- Click Multiplayer.
- Click Direct Connect.
- Type in "162.244.165.151:58331" and hit connect
```

Now open lesson1.py in your favorite code editor and follow the comments in there to get started!

##### Minecraft API
- [pi version](http://www.stuffaboutcode.com/p/minecraft-api-reference.html) Has most of the basics of the python api
- [our version](https://github.com/zhuowei/RaspberryJuice) Has the additional things our python api supports, above and beyond the pi version
- [Minecraft block ids](http://minecraft-ids.grahamedgecombe.com/)
- [rcon commands](http://minecraft.gamepedia.com/Commands#execute)
- [tell raw details](http://www.minecraftforum.net/forums/minecraft-discussion/redstone-discussion-and/351959-1-8-raw-json-text-examples-for-tellraw-title-books)



##### Host your own server / run a server locally?
- You want to switch to [this branch](https://github.com/emeth-/pycraft/tree/local-server)


##### Notes
- Player location from the python api will not match the same retrieved from the server.
    This is because raspberryjuice calculates it from the spawn point, while the server calculates it from 0,0,0.
    To fix, run this as an admin:
    setworldspawn 0 0 0


##### Troubleshooting
- "Error - need to install JDK". To resolve this error, google "java se development kit". You'll then find something that looks like [this](http://teachthe.net/topclipbox/2016-02-28_01-29-305W6BTE.png) - download and run the appropriate one for your system.
- "Error - unidentified developer". To resolve this error on OSX, you need to click the apple in the top left of your screen, then System Preferences..., then Security & Privacy, then unlock in the bottom left, then (make sure the General tab is selected) under Allow apps downloaded from select Anywhere. It should look like [this](http://teachthe.net/topclipbox/2016-02-28_01-31-41VO1QVS.png).


