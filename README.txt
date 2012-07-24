
Pantry Bell
===========

I want to use Jenkins to 

* re-image a cloud server
* build my project
* deploy the project onto the minty fresh new cloud server
* profit !

but. 

I cannot find a way that seems to happen.  There are plugins 
for running jenkins slaves on cloud servers, which may or may not be the same thing.

so... Pantry Bell

When it rings the Butler will take action


How does it work
================

You put a configuration file into pantry bell (a job),
then call it.  Pantry bell will re-image the server, and when it 
restarts the server will call back to pantrybell and then pantrybell will trigger
a new Jenkins job - safe in the knowledge that the servers it needs are ready and waiting.






Future
======

Ideally I think this should be part of Jenkins, but I am not clear how.
Or possibly it is all done already and I should have read the docs more closely.

