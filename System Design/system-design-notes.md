# System Design
When talking about good system design, there are three main general factors to consider. They are reliability, scalability, and maintainability.

### Reliability
Reliability simply refers to how fault tolerant a system is. Given x number of conditions or placed in y scenario, how well does the system hold up? 

##### Hardware Faults
Hardware faults are when problems occur with hardware systems. Maybe an ethernet connection becomes loose, a hard drive gives out, or even something more extreme and uncontrollable happens - a blackout that crashes a large number or all of an applications servers. Hardware faults occur very frequently, and is hard to predict/prevent. The best way to deal with hardware faults is to use software and hardware redundancy techniques to ensure that the loss of one or more devices doesn't cause the entire system to go down.

##### Software Errors
Software errors are bugs in code that can cause a chain reaction of failures in the whole system. There is really no good way to solve software errors other than thoroughly testing all code and processes, and tracking and monitoring behaviours of production software.

##### Human Errors
A huge pain point in software systems - this could be inaccuracies in manual entry of data, or anything that involves human interactions. Humans are known to make mistakes. Try to decouple important processes from human interaction. The more automation the better.
 
It is important to note that reliability does not simply mean "does my application crash if something unexpected happens". A lot of the times the application may not crash, but it yields a result that the end user does not expect - in a situation like that the system is still considered to be unreliable! A system must also be prone to attacks and general end user mistakes. Reliability in application design is dependant on the help and input of many others in the company, such as UX designers and operations teams.

### Scalability
Scalability in system design refers to how reliable a system is when there is a drastic increase in load. The load of an application is comprised of it's load parameters. These can be factors like requests per second, number of reads/writes to a DB, number of concurrent processes, amount of data, etc. The main way to measure the scalability of a software is to analyze it's perfomance when one or more of it's load factors are increased. Performance, like load, can be composed of many things, such as average request speeds.

Dealing with load usually comes with scaling the system by adding more hardware resources (e.g. vertical scaling by increasing the specs of one machine, or horizontal scaling where workload is distributed among an array of machines), or by fine tuning software to be more efficient. Software must be designed correctly for it to properly scale.

### Maintainability
This is pretty self explanatory - after the initial creation and design of the software, how easy is it to adapt to new changes in application code or changes in product requirement or changes in third party software. It also refers to how easy it is for new engineers to understand the codebase and system design and how easy it is to operate. Most of maintainability can be solved through proper documentation and developing flexible, modular code/features.

Keep these factors in mind when designing your systems - I will be constantly referring back to these in the analysis of which software choices to use.
