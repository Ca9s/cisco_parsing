from pathlib import Path

file_path = Path("config_sw2.txt")
"""
def get_int_vlan_map(config_filename):
    
    with open(file_path,'r') as f:
        content = f.readlines()
        access_ports={}
        trunk_ports={}
        xtr=''
        for line in content:
            if 'FastEthernet' in line:
                xtr=line.split()[-1]
            elif 'switchport mode access' in line:
                access_ports[xtr]=1
            elif 'access vlan' in line:
                line=line.split()
                access_ports[xtr]=line[-1]
            elif 'trunk allowed vlan' in line:
                vlan_id=line.split()[-1].split(',')
                vlan_intls=[int(v) for v in vlan_id]
                trunk_ports[xtr] = vlan_intls

 #       for one, second in access_ports.items():
 #           print(one,second)
 #       for one, second in trunk_ports.items():
 #           print(one,second)
    return access_ports, trunk_ports


if __name__ == '__main__':
    file_path = Path("config_sw2.txt")
    conf_output= get_int_vlan_map(file_path)
    print(conf_output)
"""

def get_int_vlan_map(config_filename):
    
    with open(config_filename,'r') as f:
        content = f.readlines()
        access_ports={}
        trunk_ports={}
        xtr=''
        for line in content:
            if 'FastEthernet' in line:
                xtr=line.split()[-1]
            elif 'switchport mode access' in line:
                access_ports[xtr]=1
            elif 'access vlan' in line:
                line=line.split()
                                    #pass integer of vlan into key:value<=, later the same in the trunk template
                access_ports[xtr]=int(line[-1])
            elif 'trunk allowed vlan' in line:
                vlan_id=line.split()[-1].split(',')
                vlan_intls=[int(v) for v in vlan_id]
                trunk_ports[xtr] = vlan_intls

    return access_ports, trunk_ports
if __name__ == '__main__':
    file_path = Path("config_sw2.txt")
    conf_output= get_int_vlan_map(file_path)
    print(conf_output)