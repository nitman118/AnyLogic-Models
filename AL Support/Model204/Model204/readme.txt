Hello Nitish,

Sorry for the delay in replying. 

1. Please use "network.getDistance( startPoint, endPoint)" method to calculate the distance between two points along the network. 

2. Unfortunately, the function "getNetworkNode()" doesn't work for moving agent. 
For the time being, only transporters in the new Material Handling Library have callbacks "On enter node" and "On exit node". However, to be able to use these callbacks for monitoring nodes, you need to create a fake agent that will seize the car-transporter  to move along the network.  
In order to implement your task without fake agent, you need to provide the car-agent with nodes of a route and move it from node to node. 
You will find both implementations in the attached example model.

I hope it will be helpful.


-----------------------------------------------------

I am facing issues in trying to figure out 2 things:

1. I am unable to calculate distances along networks…and unfortunately, this is a
huge deal for the feasibility of my project. - In the sample model ( a simple
adaptation), the distance to Jane is more than John, but finding distance from car
to Jane shows that the distance is actually lesser than the distance between car
and John. I understand the distance is being shown in absolute sense but I require
the distance along network.

2. I also need to monitor the node that the car is in so that on reaching a
particular node along the way, the car can do certain tasks - In the sample model,
I tried defining a statechart on main that checks the car's network node and if it
belongs inside the 'col_nodes', show that in editbox1, but it does not function
properly.

These 2 points are critical for the problem at hand. Could you please provide some
direction on how to correct these? and/or provide an example model that could be
of help?

Regards,
Nitish

