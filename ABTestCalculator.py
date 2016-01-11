# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 23:28:31 2016

@author: Minas
"""

def t_test_calculator(x1,dx, clevel):
#initial conversion rate in %, difference in %, desired confidence in %
#This is for a two tailed test...
   from scipy.stats import norm
   from sympy.solvers import solve
   from sympy import Symbol
   
   slevel=(1-clevel/100.0)/2.0;#Significance level for two tailed /2
   z=norm.ppf(1-slevel);
   x1new=x1/100.0;
   dxnew=dx/100.0;
   x2new=dxnew+x1new;#assuming x2>x1
   A=x1new+x2new;
   B=x1new**2+x2new**2;
   C=x2new-x1new;
   n=Symbol('n');
   solution=solve(A-((n-2)/(n-1))*B-n*C**2/z**2,n);
   print solution;
   simplesolution=z**2*(A-B)/C**2;
   print simplesolution;


if __name__ == "__main__":
    t_test_calculator(5,1, 95)
    

