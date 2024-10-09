from pathlib import Path

file_path = Path("/Users/andrey/Desktop/pylabbook/py_exercises_from_natenka_book/wds-acc-sw-1.txt")

def parse_cdp_neighbors(command_output):
    device_name=command_output.strip().split("#")[0]
 
    content=command_output.split('\n')
    result_dict={}
    for i in content:
        if i.strip() and  "Eth" in i or 'Gig' in i:
            i=i.split()
            interf_loc=str(i[1])+str(i[2])
            interf_remote=str(i[-2])+str(i[-1])
            list_key=(device_name,interf_loc)
            list_value=(i[0],interf_remote)
            result_dict[list_key]=list_value
#            striped_cont+=i+'\n'
    
    return result_dict


if __name__ == "__main__":
    with open(file_path, 'r') as f:
        print(parse_cdp_neighbors(f.read()))
