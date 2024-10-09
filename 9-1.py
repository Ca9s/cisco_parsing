intf={"FastEthernet0/12": 10,\
 "FastEthernet0/14": 11,\
 "FastEthernet0/16": 17}

access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

def generate_access_config(intf, access_mode_template):
    for key, value in intf.items():
        config_intf=(f'interface {key}')
        print(config_intf)
        for item in access_mode_template:
            if item.endswith('access vlan'):
                item = item + (f' {value}')
                print(item)
            else:
                print(item)

if __name__ == '__main__':
    conf_output= generate_access_config(intf,access_mode_template)
    print(conf_output)