# gpuChecker
Get all the free gpu IDs on CSE GPU servers.

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
[*] Server: gpu1, Available gpus (ID): []
[*] Server: gpu2, Available gpus (ID): [1, 2, 3]
[*] Server: gpu3, Available gpus (ID): [1, 2, 3]
[*] Server: gpu4, Available gpus (ID): []
[*] Server: gpu5, Available gpus (ID): [0, 1, 2, 3]
[*] Server: gpu6, Available gpus (ID): []
[*] Server: gpu7, Available gpus (ID): []
[*] Server: gpu8, Available gpus (ID): [2, 3, 4, 5, 7]
[*] Server: gpu9, Available gpus (ID): []
[*] Server: gpu10, Available gpus (ID): [0, 1, 2, 3]
[*] Server: gpu11, Available gpus (ID): [0, 1, 2, 3]
[*] Server: gpu12, Available gpus (ID): [1, 3]
[*] Server: gpu13, Available gpus (ID): [0, 1]
[*] Server: gpu14, Available gpus (ID): [0, 2, 3]
[*] Server: gpu15, Available gpus (ID): [3]
[*] Server: gpu16, Available gpus (ID): [3]
[*] Server: gpu17, Available gpus (ID): []
[*] Server: gpu18, Available gpus (ID): [3]
[*] Server: gpu19, Available gpus (ID): [0, 1, 3]
[*] Server: gpu20, Available gpus (ID): []
[*] Server: gpu21, Available gpus (ID): []
[*] Server: gpu22, Available gpus (ID): []
[*] Server: gpu23, Available gpus (ID): []
[*] Server: gpu24, Available gpus (ID): [0]
[*] Server: gpu25, Available gpus (ID): []
[*] Server: gpu26, Available gpus (ID): []
[*] Server: gpu27, Available gpus (ID): []
[*] Server: gpu28, Available gpus (ID): [2, 3]
[*] Server: gpu29, Available gpus (ID): [2, 3]
[*] Server: gpu30, Available gpus (ID): [0]
[*] Server: gpu31, Available gpus (ID): []

```

## Uinstall

```$ sudo ./uninstall.sh```