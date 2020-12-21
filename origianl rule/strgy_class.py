from bin_dec import *

class strgy:
    def __init__(self,n,agent_memory,T):
        self.response=to_inverse_binary(agent_memory,n) 
        self.virtual_wealth=0
        self.virtual_position=0
        self.action=0
    def strgy_act(self,input_binary_state):# use input state, refresh virtual_wealth and position
        decimal_state=to_decimal(input_binary_state)# example: 001 -> 1
        self.last_action=self.action
        self.action=(-1)**(int(self.response[decimal_state])+1) #example: (-1)^1=-1, (-1)^2=1


    def strgy_update(self, excess_demand):
        # print(self.last_action,self.action,excess_demand)
        self.virtual_wealth+=self.last_action*excess_demand/1000