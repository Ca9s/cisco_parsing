from pathlib import Path

file_path = Path("/Users/andrey/Desktop/pylabbook/py_exercises_from_natenka_book/wds-acc-sw-1.txt")

def parse_cdp_neighbors(command_output):
    # Get the device name from the first part of the output (before '#')
    device_name = command_output.strip().split("#")[0]

    content = command_output.split('\n')  # Split output into lines
    result_dict = {}

    for line in content:
        if line.strip() and "Gig" in line or "Twe" in line:  # Adjust to catch both Gig and Twe interfaces
            line_parts = line.split()
            local_interface = f"{line_parts[1]} {line_parts[2]}"  # Local interface (e.g., "Gig 0/19")
            remote_device = line_parts[0]  # Remote device name (e.g., "ldn-imp02")
            remote_interface = f"{line_parts[-2]} {line_parts[-1]}"  # Remote interface (e.g., "eth 0")

            # Create tuple for the local device and interface as the key
            list_key = (device_name, local_interface)
            # Create tuple for the remote device and interface as the value
            list_value = (remote_device, remote_interface)

            # Add entry to result dictionary
            result_dict[list_key] = list_value

    return result_dict


if __name__ == "__main__":
    with open(file_path, 'r') as f:
        print(parse_cdp_neighbors(f.read()))
