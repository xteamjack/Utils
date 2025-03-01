# pip install torch torchvision torchaudio -f https://download.pytorch.org/whl/cu61/torch_stable.html
# Install pytorch locally - (check for compatible ver) https://pytorch.org/get-started/locally/
# pip install nvidia-ml-py3
# pip install pynvml

import torch
print('CUDA available?  ', torch.cuda.is_available())

print('Cuda: ', torch.version.cuda)


x = torch.rand(5, 3)
print(x)


import nvidia_smi

_GPU = False
_NUMBER_OF_GPU = 0

def _check_gpu():
    global _GPU
    global _NUMBER_OF_GPU
    nvidia_smi.nvmlInit()
    _NUMBER_OF_GPU = nvidia_smi.nvmlDeviceGetCount()
    if _NUMBER_OF_GPU > 0:
        _GPU = True

def _print_gpu_usage(detailed=False):

    if not detailed:
        for i in range(_NUMBER_OF_GPU):
            handle = nvidia_smi.nvmlDeviceGetHandleByIndex(i)
            info = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
            print(f'GPU-{i}: GPU-Memory: {_bytes_to_megabytes(info.used)}/{_bytes_to_megabytes(info.total)} MB')

def _bytes_to_megabytes(bytes):
    return round((bytes/1024)/1024,2)

if __name__ == '__main__':
    print('Checking for Nvidia GPU\n')
    _check_gpu()
    if _GPU:
        _print_gpu_usage()
    else:
        print("No GPU found.")
