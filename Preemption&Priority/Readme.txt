
Preemption is making an agent leave the queue if the queue is full...
If the queue is defined as FIFO, a new agent will always be preempted if the queue is full.
you can't use preemption with a LIFO queue... 
if the queue is defined as priority based, you have to define a variable in your agent that describes its priority... and in agent priority you can use agent.priority to define what agent will be preempted (the example i created for you)
same thing with agent comparison.. you can do something like agent1.priority>agent2.priority

That's all the magic there is to it.