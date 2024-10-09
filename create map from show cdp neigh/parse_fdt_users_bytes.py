from pathlib import Path
file_path = Path("parse_ftd.txt")

file='Oct  7 07:56:47 10.88.18.2 %FTD-4-113019: Group = profile_ravpn_default,Username = alla,IP = 46.199.90.7,Session disconnected. Session Type: SSL,Duration: 0h:19m:17s,Bytes xmt: 16443192,Bytes rcv: 297694,Reason: User Requested'


with open(file_path,'r') as f:
        content=f.readlines()

        for line in content:
                
#print(file.split(','))
            split_file=line.split(',')
            timer=split_file[4]
            timer=timer.split(':')
            timer_h=timer[1].strip('h').lstrip('0') or '0'
            timer_m=timer[2].strip('m').lstrip('0') or '0'
            timer_s=timer[3].strip('s').lstrip('0') or '0'
            total_time=int(timer_h)*3600+int(timer_m)*60+int(timer_s)
            print(total_time)
            bw_r=round((int(split_file[6].split(':')[1].strip())/total_time)/1000,2)
            bw_tx=round((int(split_file[5].split(':')[1].strip())/total_time)/1000,2)
            bw_output=f'\nTotal time {total_time} sec, bw_rx={bw_r} kb/sec,bw_tx={bw_tx} kb/sec'
            print(split_file[1],split_file[2],split_file[4],bw_output)