# Information
This repository contains solutions in python3 (or in CPP in emergencies) of the practice challenges published by the TCS Code Vita contest 2020.
Note: the problem statement was removed fro the source.
## Summary
The following items show the results on every tried challenge:

* Problem A (Swayamvar): Presentation error
* Problem B (Digit Pairs): Wrong answer on private cases
* Problem C (DoleOutCadbury): Accepted!
  * DoleOutCadburyV1.py and DoleOutCadbury.cpp: are the same code but in python requires more time. In cpp it worked.
* Problem D (Petrol Pump): Presentation error
  This challenge involves the partition problem (NP-hard problem).
  * petrolpump_v0.py uses the Karmarkar_Karp Heuristic (approximate solutions). But it fails in the second example. (In fact, it also contains other kinds of heuristics to the partition problem, but those fail in the second example).
  * petrolpump_v1.py uses the Complete Karmarkar_Karp algorithm (exact solution). But it fails due to time (TLE).
  * petrolPum.cpp is similar to petrolpump_v1.py (i.e. uses the Complete Karmarkar_Karp algorithm). And it succeded!
* Problem E (Grooving Monkeys): Wrong answer on private cases.
* Problem F (Death Battle): Accepted!

### Note
Presentation error means that it is correct, but in a different "format" than required. Usually due to the line break.

Wrong answer on private cases means that it passed the public cases but not the private ones. Maybe because the statement was misunderstood.

## About the problems
You can check the statement of every problem at the official web site.
https://practice.tcscodevita.com/
Note: the problem statement was removed fro the source.

## Important tips about the contest
* Avoid using non standard characters such as é, ñ, etc in your code. Even in the comments.
* Seems that c++ code is preferred over than python, because our python code that got TLE worked fine in c++.
