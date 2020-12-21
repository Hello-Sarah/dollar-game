
from random import randint
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

from strgy_class import *
# import numpy as np
class agent:
    def __init__(self,s,m,initial_wealth=1):
        self.strgies=[strgy(randint(0,2**(2**m)-1),initial_wealth,m) for i in range(s)]
        self.real_wealth=[initial_wealth]
        self.real_position=[0]   
        self.action=0
        self.agent_cash=[initial_wealth]
    def agent_act(self,input_binary_state,latest_price,t):
        # print(len(self.strgies),"2222222")
        decimal_state=to_decimal(input_binary_state)# example: 001 -> 1
        ## To find the best strgy
        if t==0:
            self.best_strgy=self.strgies[randint(0,len(self.strgies)-1)]
        if t!=0:
######## To find the best strgy(with most virtual wealth)                           begin
            self.best_virtual_wealth=-np.inf
            for strgy_index,this_strgy in enumerate(self.strgies):
                # print(strgy_index,this_strgy.response,this_strgy.virtual_wealth[-1],this_strgy.strgy_cash[-1],this_strgy.virtual_position[-1],t)
                if this_strgy.virtual_wealth>self.best_virtual_wealth:
                    self.best_virtual_wealth=this_strgy.virtual_wealth
                    self.best_strgy=this_strgy
                
            # print("best_virtual_wealth",self.best_strgy.virtual_wealth,self.best_strgy.response)
######## To find the best strgy(with most virtual wealth)                            end




        self.real_action=(-1)**(int(self.best_strgy.response[decimal_state])+1)
        self.action=deepcopy(self.real_action)
        # if input_binary_state=="0"*len(input_binary_state):
        #     # print("pertubation!!!!")
        #     if randint(0,10)>7:
        #         self.action=1
        # if input_binary_state=="1"*len(input_binary_state):
        #     if randint(0,10)>7:
        #         self.action=-1
        
######## if keep buying or selling, make action 0                                        begin
        if self.real_position[-1]==1 and self.action==1:
            self.action=0
        if self.real_position[-1]==-1 and self.action==-1:
            self.action=0
        # if self.real_position[-1]==1 and self.action==-1 or self.real_position[-1]==-1 and self.action==1:
            # print("change idea!!!!")
######## if keep buying or selling, make action 0                                     end
        
        
######## Use action to update cash and position                                        begin
        self.real_position.append(self.real_position[-1]+self.action)

######## Use action to update cash and position                                           end


######## make this agent's strgy act with input state.                                           begin
        for i in (self.strgies):
            i.strgy_act(input_binary_state)
######## make this agent's strgy act with inputr state.                                          end        


    def agent_update_wealth(self,updated_price,net_excess_demand):
######## After new price is calculated out, calculate the new wealth of each agent.
        self.agent_cash.append(self.agent_cash[-1]-self.action*updated_price)
        self.real_wealth.append(self.agent_cash[-1]+self.real_position[-1]*updated_price)
######## And each strgy
        for i in (self.strgies):
            i.strgy_update(net_excess_demand)