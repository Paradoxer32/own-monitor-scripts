#!/usr/bin/env python3

from subprocess import check_output
from psutil import cpu_percent

addr = '8.8.8.8'

power = "upower -i /org/freedesktop/UPower/devices/battery_BAT0"
audio = "amixer sget Master"
network = f"ping -c 1 {addr}"

power_out = check_output(power.split(' ')).decode('utf-8')
audio_out = check_output(audio.split(' ')).decode('utf-8')
try:
    network_out = check_output(network.split(' ')).decode('utf-8')
except:
    pass

power_status = [i for i in power_out.split('\n') if 'percentage' in i][0].replace('    percentage:          ', '')
audio_status = [i for i in audio_out.split('\n') if '[' in i][0]
try:
    network_status = "󰖩 " + str(int(float([i for i in network_out.split('\n') if '64 bytes' in i][0].split(' ')[-2].replace('time=', ''))))
except:
   network_status = "󱚼" 

audio_perc = [i for i in audio_status.split(' ') if '%' in i][0]
audio_perc = audio_perc.replace('[', '')
audio_perc = audio_perc.replace(']', '')

audio_tog = ""
if '[off]' in audio_status:
    audio_tog = ""

elif '[on]' in audio_status:
    audio_tog = ""

cpu_status = str(cpu_percent()) + "%" 

print(f" {cpu_status} {network_status} {audio_tog} {audio_perc} 󰁹 {power_status}")
