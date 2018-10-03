import re
import json
from concurrent import futures
import paramiko


def setupConnect(userName, passwd, server=21):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("gpu%s.cse.cuhk.edu.hk" % server, 22, userName, passwd)
    return ssh


def getRemoteAvilGpus(ssh, threshold=512):
    nvidia_cmd = 'nvidia-smi -q -d MEMORY'
    stdin, stdout, stderr = ssh.exec_command(nvidia_cmd)
    output = stdout.read().decode('utf-8')
    used_mem = parse_free_memory(output)
    avail_gpu = []
    for i, v in enumerate(used_mem):
        if v < threshold:
            avail_gpu.append(i)
    return avail_gpu


def parse_free_memory(output):
    patc = re.compile(r"Used\s+:\s+(\d+)\s+MiB")
    mo = patc.findall(output)
    assert (len(mo) % 2) == 0, "Cannot determine GPU numbers"
    return [int(a) for a in mo[::2]]

def getServerInfo(serverID):
    serverInfos = ['4*TITAN V',     #1
                    '4*TITAN V',    #2
                    '4*TITAN V',    #3
                    '4*TITAN V',    #4
                    '4*TITAN V',    #5
                    '4*TITAN V',    #6

                    '8*TITAN X',    #7
                    '8*TITAN X',    #8
                    '8*TITAN X',    #9

                    '4*TITAN X',    #10
                    '4*TITAN X',    #11
                    '4*TITAN X',    #12
                    '4*TITAN X',    #13
                    '4*TITAN X',    #14
                    '4*TITAN X',    #15
                    '4*TITAN X',    #16

                    '4*1080TI',     #17
                    '4*1080TI',     #18
                    '4*1080TI',     #19
                    '4*1080TI',     #20
                    '4*1080TI',     #21

                    '4*TITAN V',    #22
                    '4*TITAN V',    #23
                    '4*TITAN V',    #24
                    '4*TITAN V',    #25
                    '4*TITAN V',    #26
                    '4*TITAN V',    #27

                    '4*TITAN XP',   #28
                    '4*TITAN XP',   #29
                    '4*TITAN XP',   #30
                    '4*TITAN XP'    #31
                ]
    return serverInfos[serverID - 1]


if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)


    def checkGpuServer(server=1):
        try:
            sshConnection = setupConnect(config['userName'], config['passwd'], server=server)
            res = getRemoteAvilGpus(sshConnection, int(config['memoryThreshold']))
            sshConnection.close()
        except Exception as e:
            print(e)
            return None
        return '[*] Server: gpu%s, %s, Available gpus (ID): %s' % (server, getServerInfo(server), res)


    with futures.ProcessPoolExecutor(max_workers=31) as pool:
        for avalRes in pool.map(checkGpuServer, range(1, 32)):
            print(avalRes)
