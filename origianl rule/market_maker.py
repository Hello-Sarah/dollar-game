import matplotlib.pyplot as plt
from world_class import *

time_mm_weadlth_pos=0
simu_time=10

sim_world=[agent_world(N=101,memory=3,n_strategy=5,T=500,world_initial_wealth=5) for i in range(simu_time)]

for index,world in enumerate(sim_world):
    print(index)
    world.agent_world_run(silent=0)


    
plt.figure()
for world in sim_world:
    plt.plot(world.all_price)
plt.title("price_change")

plt.figure()
for world in sim_world:
    plt.plot(world.mm_wealth)
plt.title("mm_wealth")
plt.show()




# for tt in range(simu_time):
#     print(tt)
#     sim=agent_world(N=101,memory=3,n_strategy=5,T=500,world_initial_wealth=5)
#     sim.agent_world_run(silent=1)
#     # plt.plot((sim.all_price))
#     # plt.plot(sim.mm_wealth)
#     if sim.mm_wealth[-1]>0:
#         time_mm_weadlth_pos+=1
# print(time_mm_weadlth_pos/simu_time)
# plt.show()
