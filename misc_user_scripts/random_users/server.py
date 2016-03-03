# this file is intended to be edited by the user running the script.
#
# by editing this file you can easily change whether the scripts are run from the local machine
# that is, on the raspberry pi itself
# or from another computer on the network
#

# if you are running the scripts on the raspberry pi, then set address to 127.0.0.1
# 127.0.0.1 is a special address that means connect to the same machine I'm running this on
# so this is useful when you are runnning the script and minecraft on the same machine
address = "127.0.0.1"
# If you are running the scripts on a machine other than the raspberry pi, then put the rasberry pi's
# ip address here
#address = "192.168.1.100"

# If you are developing/testing against the RaspberyJuice Bukkit server, you may find that certain APIs are not
# implemented like GetBlockWithData.
# By setting the flag below to true or false, a script can use conditional logic on which features to use.
# the default is set to True meaning the server is running Minecraft PI or on a Rasperbby PI.

is_pi = True
#is_pi = False