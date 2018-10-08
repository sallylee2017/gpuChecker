# gpuChecker
Get all the free gpu IDs on CSE GPU servers.


## Updates

- Add servers' gpu information.

## Testing platform
- Ubuntu 16.04
- Python 3.6

## Dependency
- paramiko (Using ```$ pip install paramiko``` to install it)

## Install

- Set up the config.json 
	
    Just modify the 'configExample.json' file, and save it as 'config.json'.
    ```
    {
  "userName": "XXXX",
  "passwd": "*************",
  "memoryThreshold": "512"
	}
    ```

- ```$ sudo ./install.sh```



## Use
Just using 'gpuChecker' command in the terminal, then you would get something like this:

```
[*] Server: gpu1, 4*TITAN V, Available gpus (ID): [0, 1, 2, 3]
[*] Server: gpu2, 4*TITAN V, Available gpus (ID): [0, 2]
[*] Server: gpu3, 4*TITAN V, Available gpus (ID): [0]
[*] Server: gpu4, 4*TITAN V, Available gpus (ID): []
[*] Server: gpu5, 4*TITAN V, Available gpus (ID): []
[*] Server: gpu6, 4*TITAN V, Available gpus (ID): []
[*] Server: gpu7, 8*TITAN X, Available gpus (ID): []
[*] Server: gpu8, 8*TITAN X, Available gpus (ID): []
[*] Server: gpu9, 8*TITAN X, Available gpus (ID): []
[*] Server: gpu10, 4*TITAN X, Available gpus (ID): [2, 3]
[*] Server: gpu11, 4*TITAN X, Available gpus (ID): []
[*] Server: gpu12, 4*TITAN X, Available gpus (ID): [2, 3]
[*] Server: gpu13, 4*TITAN X, Available gpus (ID): []
[*] Server: gpu14, 4*TITAN X, Available gpus (ID): [2]
[*] Server: gpu15, 4*TITAN X, Available gpus (ID): []
[*] Server: gpu16, 4*TITAN X, Available gpus (ID): [2]
[*] Server: gpu17, 4*1080TI, Available gpus (ID): []
[*] Server: gpu18, 4*1080TI, Available gpus (ID): []
[*] Server: gpu19, 4*1080TI, Available gpus (ID): [1, 3]
[*] Server: gpu20, 4*1080TI, Available gpus (ID): []
[*] Server: gpu21, 4*1080TI, Available gpus (ID): []
[*] Server: gpu22, 4*TITAN V, Available gpus (ID): []
[*] Server: gpu23, 4*TITAN V, Available gpus (ID): []
[*] Server: gpu24, 4*TITAN V, Available gpus (ID): []
[*] Server: gpu25, 4*TITAN V, Available gpus (ID): []
[*] Server: gpu26, 4*TITAN V, Available gpus (ID): []
[*] Server: gpu27, 4*TITAN V, Available gpus (ID): [2]
[*] Server: gpu28, 4*TITAN XP, Available gpus (ID): []
[*] Server: gpu29, 4*TITAN XP, Available gpus (ID): [2]
[*] Server: gpu30, 4*TITAN XP, Available gpus (ID): [2, 3]
[*] Server: gpu31, 4*TITAN XP, Available gpus (ID): []

```

## Uinstall

```$ sudo ./uninstall.sh```


## TODO

- [ ] Check how many gpus your are using.
- [ ] Submit jobs automaticly when ther are gpus avilable.
