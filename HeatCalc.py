# figure out temperature drop

timesteps_per_hour = 1000
timestep_size_seconds = 3600/timesteps_per_hour
house_volume_cubft = 60000
cubic_feet_per_degree = 55
heat_loss_const = 80000/40


outdoor_temp = 30
indoor_temp = 70

for t in range(int(timesteps_per_hour)):
    heat_loss = heat_loss_const * (indoor_temp - outdoor_temp) * (1/timesteps_per_hour)
    degree_loss = heat_loss  * (cubic_feet_per_degree/house_volume_cubft)
    indoor_temp = indoor_temp - degree_loss

print(indoor_temp)
