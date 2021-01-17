from system import System
import numpy as np
import json

with open('../json/system_list.json') as json_file:
    sys_list = json.load(json_file)

# loop over system data
print("Export data to json")

for id,sys_data in enumerate(sys_list):
    print("-> process system {}".format(id))
    sys = System(sys_data["order"],sys_data["type"],sys_data["params"])

    # plot
    plot = sys_data["plot"]
    type = plot["type"]
    params = plot.get("params")
    data = sys.plot(type,params)
    
    #export json
    filename ="../json/data_{}.json".format(id)
    with open(filename, 'w') as outfile:
            json.dump(data, outfile)
