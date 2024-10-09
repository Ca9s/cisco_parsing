intf={"FastEthernet0/12": 10,\
 "FastEthernet0/14": 11,\
 "FastEthernet0/16": 17}

access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

def generate_access_config(intf_vlan_mapping, access_template):
    zoom=[]
    for key, value in intf_vlan_mapping.items():
        zoom.append(f'interface {key}')
        for item in  access_template:
            if item.endswith('access vlan'):
                item = item + (f' {value}')
                zoom.append(item)
            else:
                zoom.append(item)
    return '\n'.join(zoom)

if __name__ == "__main__":
    config_output = generate_access_config(intf, access_mode_template)
    print(config_output)