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


def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    zoom=[]
    for key, value in intf_vlan_mapping.items():
        zoom.append(f'interface {key}')
#       ingest psecurity dic 
        if psecurity is not None:
            for item in psecurity:
                zoom.append(item)
#       ingest access_config dic
        for item in  access_template:
            if item.endswith('access vlan'):
                item = item + (f' {value}')
                zoom.append(item)
            else:
                zoom.append(item)
    return '\n'.join(zoom)

if __name__ == "__main__":
    config_output = generate_access_config(intf, access_mode_template,port_security_template)
    print(config_output)