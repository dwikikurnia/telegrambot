import paramiko
import time
import pandas as pd

# Input Data
command = input('Masukkan Command: ')
siteid = input('Masukkan Site ID: ').upper()
user = "dwiki"
passwd = "poring@123"
ipaddr = "10.37.2.188"

# Load Data IP IOAM
df = pd.read_excel("D:\Backup Desember 2019\My Telkomsel\RTPO Tembilahan\DLD Migrasi\IP OAM RBS Desember 2020.xlsx")

# Connect to SSH Client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ipaddr, username=user, password=passwd, port=22, timeout=60)

# Define Input Command
def input_command(self):
    stdin, stdout, stderr = ssh_client.exec_command(self, timeout=60)
    stdin.channel.shutdown_write()
    stdout = stdout.readlines()
    output = "".join(stdout)
    selective_output = str(output.find(command))
    print(output[int(selective_output):])


try:
    # Define NE ID (3G or 4G)
    if "3" in command:
        siteid = siteid + "W"
    else:
        siteid = siteid + "M"

    # Define IP OAM
    df_siteid = df[df["site_name"].str.contains(siteid)]
    ipoam = df_siteid["ip_oam"].values[0]

    # Main Program
    if command == "alt3":
        command = "active alarms"
        input_command("/home/udo/moshell_19/moshell/moshell -v username=rbs,password=rbs %s 'lt all;alt'" %ipoam)

    elif command == "alt4":
        command = "Collecting Alarms"
        input_command("/home/udo/moshell_19/moshell/moshell -v username=rbs,password=rbs %s 'lt all;alt'" %ipoam)

    elif command == "tra3":
        command = "hget radio"
        input_command("/home/udo/moshell_19/moshell/moshell -v username=rbs,password=rbs %s 'lt all;hget radio'" %ipoam)

    elif command == "tra4":
        command = "ue print -admitted"
        input_command("/home/udo/moshell_19/moshell/moshell -v username=rbs,password=rbs %s 'lt all;ue print -admitted'" %ipoam)

    elif command == "cab3":
        command = "cabx"
        input_command("/home/udo/moshell_19/moshell/moshell -v username=rbs,password=rbs %s 'lt all;cabx'" %ipoam)

    elif command == "cab4":
        command = "RadioNode"
        input_command("/home/udo/moshell_19/moshell/moshell -v username=rbs,password=rbs %s 'lt all;cabx'" %ipoam)

    elif command == "thp":
        command = "Date"
        input_command("/home/udo/moshell_19/moshell/moshell -v username=rbs,password=rbs %s 'lt all;pmr -r 206 -m 3 | grep -e Int_DlThroughput_kbps -e Int_UlThroughput_kbps'" %ipoam)

    elif command == "prb":
        command = "Date"
        input_command("/home/udo/moshell_19/moshell/moshell -v username=rbs,password=rbs %s 'lt all;pmr -r 206 -m 3 | grep -e Res_DlPrbPercUsage -e Res_UlPrbPercUsage'" %ipoam)

    elif command == "ping":
        command = "PING"
        input_command("ping %s -c 5" %ipoam)

    else:
        print("\nCommand Not Found!!")

except:
    print("\nSite ID Not Found!!")

finally:
    print("\nProgram Executed :)")

# Close SSH Client
ssh_client.close()