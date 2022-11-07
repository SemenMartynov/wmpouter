import paramiko
import random
import concurrent.futures

####  config  ####
special_account = "admin"
special_port    = "443"
special_timeout = 90
workersnumber   = 64

#pkey = paramiko.Ed25519Key.from_private_key_file("./id_rsa")
pkey = paramiko.RSAKey.from_private_key_file("./id_rsa")
#### #### #### ####

host_list = []
for x in range(208, 223 + 1):
    for y in range(1, 256):
        host_list.append(f"37.157.{x}.{y}")     # 4096   15/03/12    Ucom LLC
for x in range(128, 255 + 1):
    for y in range(1, 256):
        host_list.append(f"5.77.{x}.{y}")       # 32768  13/06/12    Ucom LLC
for x in range(64, 127 + 1):
    for y in range(1, 256):
        host_list.append(f"37.186.{x}.{y}")     # 16384  20/03/12    GNC-Alfa CJSC
for x in range(64, 95 + 1):
    for y in range(1, 256):
        host_list.append(f"37.252.{x}.{y}")     # 8192   19/04/12    Ucom LLC
for x in range(0, 255 + 1):
    for y in range(1, 256):
        host_list.append(f"46.70.{x}.{y}")      # 131072 07/07/10    VEON Armenia CJSC
        host_list.append(f"46.71.{x}.{y}")      # 131072 07/07/10    VEON Armenia CJSC
        host_list.append(f"46.130.{x}.{y}")     # 65536  06/10/10    MTS Armenia CJSC
for x in range(192, 255 + 1):
    for y in range(1, 256):
        host_list.append(f"46.162.{x}.{y}")     # 16384  29/11/10    Ucom LLC
for x in range(128, 255 + 1):
    for y in range(1, 256):
        host_list.append(f"46.241.{x}.{y}")     # 32768  23/12/10    Ucom LLC
for x in range(0, 31 + 1):
    for y in range(1, 265):
        host_list.append(f"62.89.{x}.{y}")      # 8192   14/12/04    GNC-Alfa CJSC
for x in range(64, 79 + 1):
    for y in range(1, 256):
        host_list.append(f"78.109.{x}.{y}")     # 4096   04/07/07    GNC-Alfa CJSC
for x in range(224, 239 + 1):
    for y in range(1, 256):
        host_list.append(f"80.86.{x}.{y}")      # 4096   21/08/01    Netsys JV LLC
for x in range(0, 15 + 1):
    for y in range(1, 265):
        host_list.append(f"81.16.{x}.{y}")      # 4096   18/12/08    Ucom LLC
for x in range(208, 223 + 1):
    for y in range(1, 256):
        host_list.append(f"81.89.{x}.{y}")      # 4096   18/04/06    Crossnet LLC
for x in range(192, 207 + 1):
    for y in range(1, 256):
        host_list.append(f"82.199.{x}.{y}")     # 4096   10/09/12    Ucom LLC
for x in range(0, 63 + 1):
    for y in range(1, 265):
        host_list.append(f"83.139.{x}.{y}")     # 16384  18/08/04    MTS Armenia CJSC
for x in range(128, 191 + 1):
    for y in range(1, 256):
        host_list.append(f"87.241.{x}.{y}")     # 16384  07/07/05    VEON Armenia CJSC
for x in range(192, 207 + 1):
    for y in range(1, 256):
        host_list.append(f"89.249.{x}.{y}")     # 4096   20/11/06    LIR LLC
for x in range(32, 47 + 1):
    for y in range(1, 256):
        host_list.append(f"93.185.{x}.{y}")     # 4096   05/06/08    GNC-Alfa CJSC
for x in range(16, 31 + 1):
    for y in range(1, 256):
        host_list.append(f"94.228.{x}.{y}")     # 4096   23/09/08    Supercom LLC
for x in range(192, 207 + 1):
    for y in range(1, 256):
        host_list.append(f"95.140.{x}.{y}")     # 4096   20/03/09    MTS Armenia CJSC
for x in range(32, 47 + 1):
    for y in range(1, 256):
        host_list.append(f"109.75.{x}.{y}")     # 4096   17/11/09    Ucom LLC
for x in range(64, 95 + 1):
    for y in range(1, 256):
        host_list.append(f"141.136.{x}.{y}")    # 8192   29/06/11    Ucom LLC
for x in range(128, 191 + 1):
    for y in range(1, 256):
        host_list.append(f"178.72.{x}.{y}")     # 16384  10/03/10    Supercom LLC
for x in range(128, 191 + 1):
    for y in range(1, 256):
        host_list.append(f"178.78.{x}.{y}")     # 16384  27/04/10    Ucom LLC
for x in range(128, 255 + 1):
    for y in range(1, 256):
        host_list.append(f"178.160.{x}.{y}")    # 32768  22/01/10    VEON Armenia CJSC
for x in range(48, 63 + 1):
    for y in range(1, 256):
        host_list.append(f"178.219.{x}.{y}")    # 4096   21/05/10
for x in range(192, 255 + 1):
    for y in range(1, 256):
        host_list.append(f"188.115.{x}.{y}")    # 16384  25/05/09    Ucom LLC
for x in range(64, 95 + 1):
    for y in range(1, 256):
        host_list.append(f"195.250.{x}.{y}")    # 8192   10/03/97    GNC-Alfa CJSC
for x in range(224, 255 + 1):
    for y in range(1, 256):
        host_list.append(f"212.34.{x}.{y}")     # 8192   23/04/09    Ucom LLC
for x in range(192, 223 + 1):
    for y in range(1, 256):
        host_list.append(f"212.42.{x}.{y}")     # 8192   21/08/98    LIR LLC
for x in range(64, 95 + 1):
    for y in range(1, 256):
        host_list.append(f"212.73.{x}.{y}")     # 8192   01/02/99    VEON Armenia CJSC
for x in range(0, 15 + 1):
    for y in range(1, 265):
        host_list.append(f"217.76.{x}.{y}")     # 4096   01/05/09    MTS Armenia CJSC
for x in range(16, 31 + 1):
    for y in range(1, 256):
        host_list.append(f"217.113.{x}.{y}")    # 4096   24/06/02    LIR LLC
random.shuffle(host_list)

# Retrieve a single page and report the URL and contents
def check_host(host):
    print(f"Try to connect with {host}:{special_port}")
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    try:
        client.connect(host, username=special_account, pkey=pkey, port=special_port, timeout=special_timeout, banner_timeout=special_timeout)
        stdin , stdout, stderr = client.exec_command("hostname")
        f = open("report.txt", "w")
        f.write(f"{host} says {stdout.read()}")
        f.close()
        quit()
    except:
        print(f"Host {host}:{special_port} is not available")


# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=workersnumber) as executor:
    # Start the load operations and mark each future with its URL
    future_to_host = {executor.submit(check_host, host): host for host in host_list}
    for future in concurrent.futures.as_completed(future_to_host):
        future.result()


