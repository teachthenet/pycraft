##### To Run

In a file browser, double click Minecraft Launcher.jar

![](http://teachthe.net/topclipbox/2016-03-03_14-23-00KXC3CT.png)

In the bottom left, decide upon and enter a username for yourself

![](http://teachthe.net/topclipbox/2016-03-03_14-23-20PLF8N2.png)

Also in the bottom left, select Release 1.8.8

![](http://teachthe.net/topclipbox/2016-03-03_14-21-47BAP7OT.png)

Click Install

![](http://teachthe.net/topclipbox/2016-03-03_14-24-41Z42XWT.png)

Once the game launches, select Multiplayer

![](http://teachthe.net/topclipbox/2016-03-03_14-25-17IJ9FWJ.png)

Then select Direct Connect

![](http://teachthe.net/topclipbox/2016-03-03_14-25-36Z7C2ZV.png)

Now you will need to enter the IP of the server.
- If you are using my server, type in 162.244.165.151:58331
- If you are running the server locally, type in 127.0.0.1
- If your instructor is running a server somewhere, they will provide you with the IP to type in.

![](http://teachthe.net/topclipbox/2016-03-03_14-25-53XIX7K9.png)

Now click Join Server!

![](http://teachthe.net/topclipbox/2016-03-03_14-27-3797QL8G.png)

Now open lesson1.py in your code editor and follow the comments in there to get started!

##### Minecraft API
- [pi version](http://www.stuffaboutcode.com/p/minecraft-api-reference.html) Has most of the basics of the python api
- [our version](https://github.com/zhuowei/RaspberryJuice) Has the additional things our python api supports, above and beyond the pi version
- [Minecraft block ids](http://minecraft-ids.grahamedgecombe.com/)
- [rcon commands](http://minecraft.gamepedia.com/Commands#execute)
- [tell raw details](http://www.minecraftforum.net/forums/minecraft-discussion/redstone-discussion-and/351959-1-8-raw-json-text-examples-for-tellraw-title-books)



##### Host your own server / run a server locally?
- You want to switch to [this repo](https://github.com/teachthenet/pycraft-server)


##### Notes
- Player location from the python api will not match the same retrieved from the server.
    This is because raspberryjuice calculates it from the spawn point, while the server calculates it from 0,0,0.
    To fix, run this as an admin:
    setworldspawn 0 0 0


##### Troubleshooting
- "Error - need to install JDK". To resolve this error, google "java se development kit". You'll then find something that looks like [this](http://teachthe.net/topclipbox/2016-02-28_01-29-305W6BTE.png) - download and run the appropriate one for your system.
- "Error - unidentified developer". To resolve this error on OSX, you need to click the apple in the top left of your screen, then System Preferences..., then Security & Privacy, then unlock in the bottom left, then (make sure the General tab is selected) under Allow apps downloaded from select Anywhere. It should look like [this](http://teachthe.net/topclipbox/2016-02-28_01-31-41VO1QVS.png).


