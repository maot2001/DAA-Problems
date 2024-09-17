from gen import gen_examples
from test import *
from tester import *
import networkx as nx
import matplotlib.pyplot as plt
from ullman import perm_constructor,isomorph


examples = gen_examples(500)
flag=True
for i in examples:
    print(f'\nmatrix A:\n{i[0]}')
    print(f'\nmatrix B:\n{i[1]}')

    if(isomorph(i[0],i[1],perm_constructor(i[0],i[1]))!=are_graphs_isomorphic_matrix(i[0],i[1])):
        print("Wrong Anwser")
        flag=False
        break
    
if(flag):
    print("Accepted")
