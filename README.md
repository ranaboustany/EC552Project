# EC552Project

Comp Syn Bio Project - Lujain Khusheim, Rana Boustany, Zakiah Tcheifa, and Angela Abrego Chavez

Researchers want to utilize natural protein production pathways in bacteria for the production of a specific protein that does not naturally occurs in the bacteria.

We aim to design a program that can identify the most suitable bacteria for the production of a specific protein based on minimizing the number of required mutations for the achievement of that sequence. 

The algorithm will prompt the user for DNA sequences from bacteria and target protein. Each DNA sequence will be then compared to each possible protein sequence until the DNA sequence with the smallest difference is found. Once the closest DNA sequence is found, the specific locations and types of mutations are outputted. A visual of the resulting protein is also outputted. 

User will need a python running platform and the ability to download python packages pandas and intertools. User will also need to download files AminoAcidDB.csv and bacteria_db_test.csv. These will be input in the algorithm along with the desired protein sequence (.txt file). The program will then work to deliver the possible DNA sequences (.csv file) and the output will be a Report (.csv file). The user will then be prompted if a detailed report (.csv) is desired and if so, will be downloaded as well. 
