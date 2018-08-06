fork from 
https://github.com/floatec/attack-defense-CTF-demo


attack & defense CTF demo
==========================
this project contains a minimalistic attack and defense CTF setup with exectlly one service

Vulnbox
-------------------------
You have to generate challange by yourself.
I remove floatec's challange, or you can add it back.

Gameserver
---------------------------
The gameserver has three service to run.
One is `gameserver.py` to generate flag for each team.

Second one is `submitserver.py`, which open 9999 port to be a submittable server.

Third one is `scoreboard.py`, which open 9990 port to show a scoreboard for each team. 

How many teams join is base on `teams.list`.

You can add number of teams on your own.

You can define team name by yourself rather than IP.

The submitserver.py has a mechanism that each team can't send not only their own flag but also other team's flag two times in a round.

You can start next round by re-launch gameserver.py and scp flag again.

Aditionalls Scripts
---------------------------
the scoreboard.sh script is a small bash script that calls the scoreboard every 5 sec.


recommended setup
--------------------------

one way to set this all up is the following:
* setup 3 virtualbox machines with ubuntu server on it.
* move the gameserver scripts to your 1st VM.
* install requests via pip on your 1st VM
* set the network to host only network(don't forget that you can now only acces other VMs and your host in this mode, but not the internet. If you like to have internet just add another network device in your virtual machine with NAT)
* edit team.list.
* launch gameserver.py to generate flag.
* scp flag to each team.
* launch submitserver.py and scoreboard.py.
* you should be ready to go now
    
