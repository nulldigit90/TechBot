# The TechBot Project

This is an ircbot I will be working on. It support loading modules/plugins. 

It is written in Python 3.4.3 and is being tested on Arch Linux 4.1.5-1-ARCH.

There is no official documentation on it yet, but code comments and doc-strings should tell you anything
you need to know.


###Progress
SSL has been fixed, using Queues and Selector now. Examples have been updated in the adons.

No more issue with zombie processes. I have added a snippit to remove or '.join()' finished
multiprocesses that had been started as 'addons'.

Fixed spelling, adon has been chaged to addons as per everyone pointing it out lol.

Logging has been added, you can log all, or filter phrases or words. This is done in the irc.config file
usign CSV. Look at the config file for an example.

##Issues
~~I need to develope a better way to handle sending things via sendIrc(). Maybe force nick and chan to be used
or at least addressed in the addons?~~

###TO-DO
 - Start adding channel op things such as flood control and user logs (diff with host mask and last seen kinda things).
 - Timed things, such as random or certian points, post an update for something.
 - Random (current) links to hacking and securrity related stuff. Maybe a .hot command to grab links from security blogs.
 - EZ related things, like recent posts or stats or something.
 - See a word or phrase someone said and link to an article, or respond with something?
 - User input?
