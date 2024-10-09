
trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999","switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}
trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}

def generate_trunk_config(intf_vlan_mapping,trunk_template):
    cmd_list=[]
    for int,vlan in intf_vlan_mapping.items():
        cmd_list.append(f'interface {int}')
        for cmd_sub in trunk_template:
            if 'allowed' in cmd_sub:
                vlan_str=','.join(str(v) for v in vlan)
                cmd_sub = cmd_sub + (f' {vlan_str}')
                cmd_list.append(cmd_sub)
            else:
                cmd_list.append(cmd_sub)
    return cmd_list

if __name__ == '__main__':
    conf_output= generate_trunk_config(trunk_config,trunk_mode_template)
    print(conf_output)