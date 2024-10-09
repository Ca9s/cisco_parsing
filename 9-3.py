from pathlib import Path

file_path = Path("config_sw1.txt")

def get_int_vlan_map(config_filename):
    
    with open(file_path,'r') as f:
        content = f.readlines()
        access_ports={}
        trunk_ports={}
        xtr=''
        for line in content:
            if 'FastEthernet' in line:
                xtr=line.split()[-1]
            elif 'access vlan' in line:
                line=line.split()
                                 #there a integer of vlan is passed to key:value<= 
                access_ports[xtr]=int(line[-1])
            elif 'trunk allowed vlan' in line:
                vlan_id=line.split()[-1].split(',')
                                #there a integer of vlan is passed to key:value<= 
                vlan_intls=[int(v) for v in vlan_id]
                trunk_ports[xtr] = vlan_intls


    return access_ports, trunk_ports


if __name__ == '__main__':
    file_path = Path("config_sw1.txt")
    conf_output= get_int_vlan_map(file_path)
    print(conf_output)
