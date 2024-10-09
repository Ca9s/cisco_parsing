intf={"FastEthernet0/12": 10,\
 "FastEthernet0/14": 11,\
 "FastEthernet0/16": 17}

access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]
port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"]


def generate_access_config(intf_vlan_mapping, *templates):
    zoom=[]
    for key, value in intf_vlan_mapping.items():
        zoom.append(f'interface {key}')
#       ingest psecurity dic 
        for template in templates:
            for item in template:
                if item.endswith('access vlan'):
                    item = item + (f' {value}')
                    zoom.append(item)
                else:
                    zoom.append(item)
    return '\n'.join(zoom)

if __name__ == "__main__":
    config_output = generate_access_config(intf,port_security_template, access_mode_template)
    print(config_output)