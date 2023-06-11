import os
import io
import PIL.Image
import sys

sys.path.append('/home/patrick_wsl/anaconda3/envs/LipSyncApp-py391/LipSyncApp/additional_scripts')
from Settings import SettingUtilities

# Install additional required packages
os.system('pip install opencv-python')
os.system('pip install opencv-python-headless')
os.system('pip install import-ipynb')
import import_ipynb
import cv2

def cv2_imshow(img):
    ret, encoded_img = cv2.imencode('.png', img)
    display(PIL.Image.open(io.BytesIO(encoded_img)))

def create_dirs(dirs):
    for dir in dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)

number_of_faces = 2
settings = SettingUtilities(number_of_faces)

sys.path.append(settings.sub_modules_path)

local_project_path = settings.get_path('local_project_path')
dir_tmp = settings.get_path('esrgan_tmp_dir_path')
dir_mask = settings.get_path('esrgan_mask_dir_path')
dir_input = settings.get_path('esrgan_input_video_folder_path')
dir_dejpeg = settings.get_path('esrgan_dejpeg_dir_path')
dir_upscaled = settings.get_path('esrgan_upscaled_dir_path')
dir_output = settings.get_path('esrgan_output_video_dir_path')
dir_models = settings.get_path('esrgan_models_dir_path')
print(dir_models)

create_dirs([dir_tmp, dir_mask, dir_input, dir_dejpeg, dir_upscaled, dir_output, dir_models])

if not os.path.exists(settings.get_path('lip_sync_app_path')):
    os.system(f'git clone https://github.com/Walchshofer/LipSyncApp.git {settings.get_path("lip_sync_app_path")}')
else:
    os.chdir(settings.get_path('lip_sync_app_path'))
    os.system('git pull')

os.chdir(settings.get_path('lip_sync_app_path'))
os.system('git submodule init')
os.system('git submodule update')
os.system('git submodule foreach git pull origin main')

os.chdir(settings.get_path('esrgan_path'))

from inhagcutils import *

from IPython.display import clear_output
import requests, gmic
from IPython.display import Image
from datetime import datetime

os.chdir(settings.get_path('esrgan_path'))
os.system('pip install -r requirements.txt')
os.system(f'wget \'https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspx?share=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA\' -O {settings.get_path("wav2lip_checkpoint_wav2lip_gan_path")}')
os.chdir(settings.get_path('lip_sync_app_path'))

os.system('pip install typer')
os.system('pip install rich')
os.system('pip install gmic')
os.system('pip install opencv-python-headless')
os.system('pip install opencv-contrib-python-headless')
os.system('pip install face_recognition')
os.system('pip install ffmpeg-python')

os.system('pip install torch torchvision torchaudio -f https://download.pytorch.org/whl/cu111/torch_stable.html')

os.system('pip install moviepy')
os.system('pip install tqdm')
os.system('pip install gdown')
os.system('pip install pydub')
os.system('pip install Pillow')

# Install torch, torchvision, and torchaudio with CUDA support (replace 'cu111' with your CUDA version)
os.system('pip install torch torchvision torchaudio -f https://download.pytorch.org/whl/cu111/torch_stable.html')

# Install the rest of the packages
os.system('pip install moviepy')
os.system('pip install tqdm')
os.system('pip install gdown')
os.system('pip install pydub')
os.system('pip install Pillow')

os.system('pip install -r requirements.txt')