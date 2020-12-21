from agent_class import *
class agent_world:
    
    def __init__(self, N=101,memory=5, n_strategy=5,T=1000,world_initial_wealth=5):
        self.num_agents=N
        self.memory_length = memory
        self.agents=[agent(s=n_strategy,m=self.memory_length,initial_wealth=world_initial_wealth) for n in range(N)] # intialize
        self.T=T
        self.initial_price=1
        # self.all_state="0"*memory # all_state, consist of "-1" or "1", initialize to "000"
        self.all_state="010"
        self.all_price=[1] # initialize price to 1
        self.mm_cash=[0]
        self.mm_smt=[10]
        self.mm_wealth=[0]
    def agent_world_run(self,silent=0):
        for time in range(self.T):
#### When t-1/2, agents make decision, and modify position, cash.
            self.current_state=self.all_state[-self.memory_length:]
    ######## Count the excess_demand            begin
            sum_position=0
            excess_demand=0
            real_ex_de=0
            for i in self.agents:
                i.agent_act(self.current_state,latest_price=self.all_price[-1],t=time)
                excess_demand+=i.action
                real_ex_de+=i.real_action
                sum_position+=i.real_position[-1]
    ######## Count the excess_demand            end
 
#### time =t-1/2        End

            if silent==0:
                print("t=",time,"input_state=",self.current_state)
                print("price=",self.all_price[-1],"real_ex_de=",real_ex_de,"excess demand=",excess_demand,"S_m(t)=",self.mm_smt[-1],"sum_position",sum_position,"mm_wealth=",self.mm_wealth[-1],"mm_cash:",self.mm_cash[-1])
#### time =  t  append new state, the matket maker 
            net_excess_demand=excess_demand-self.mm_smt[-1]

            if net_excess_demand<0:
                self.all_state=self.all_state+'0'
            if net_excess_demand>=0:
                self.all_state=self.all_state+'1'
            
            #算价格时使用的是加到上一时刻（t-1）的smt
            # self.all_price.append(np.exp(np.log(self.all_price[-1])+(net_excess_demand)/1000))# 新的价格，算出来，算是t时刻的价格
            self.all_price.append(np.exp(np.log(self.all_price[-1])+(excess_demand-self.mm_smt[-1])/1000))# 新的价格，算出来，算是t时刻的价格
            self.mm_cash.append(self.mm_cash[-1]+excess_demand*self.all_price[-1])# t时刻剩下的cash,用t-1时的价格扣钱  
            self.mm_wealth.append(self.mm_cash[-1]+(self.mm_smt[-1]*self.all_price[-1]))# 最新的财富，是cash加smt乘t时刻价格
            # mm_silent=1
            # if mm_silent==0:
            #     if excess_demand>0:
            #         print("sell at",self.all_price[-1])
            #     if excess_demand<0:
            #         print("buy at",self.all_price[-1])

            self.mm_smt.append(self.mm_smt[-1]-excess_demand) # 下一时刻的 s_m_t 

            # self.mm_wealth.append(self.mm_cash[-1]+(self.mm_smt[-2]*self.all_price[-1]))# 最新的财富，是cash加smt乘t时刻价格
            
            for i in self.agents:
                
                i.agent_update_wealth(self.all_price[-1],excess_demand)
