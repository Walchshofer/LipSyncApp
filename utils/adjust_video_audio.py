import os
import shutil
import subprocess
import numpy as np
import moviepy.editor as mp
from moviepy.audio.AudioClip import AudioArrayClip

class VideoAudioAdjustment:

    @staticmethod
    def create_silent_audio(duration, filepath, sample_rate=44100):
        audio_array = np.zeros((int(np.ceil(float(duration)) * sample_rate), 2), dtype=np.float32)
        silent_audio = AudioArrayClip(audio_array, fps=sample_rate)
        silent_audio.write_audiofile(filepath)

    @staticmethod
    def get_audio_codec(input_audio):
        command = f'ffprobe -v error -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 -select_streams a:0 "{input_audio}"'
        codec = subprocess.check_output(command, shell=True).decode('utf-8').strip()
        return codec

    @staticmethod
    def get_video_codec(input_video):
        command = f'ffprobe -v error -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 -select_streams v:0 "{input_video}"'
        codec = subprocess.check_output(command, shell=True).decode('utf-8').strip()
        return codec

    @staticmethod
    def convert_audio_to_aac(input_audio, output_audio):
        command = f'ffmpeg -i "{input_audio}" -c:a aac "{output_audio}"'
        subprocess.call(command, shell=True)

    @staticmethod
    def adjust_video_audio(input_video, input_audio, adjusted_video, adjusted_audio, silent_audio_path, adjusted_audio_aac, silent_audio_lipsync_path):
        # Load input video and audio
        video = mp.VideoFileClip(input_video)
        audio = mp.AudioFileClip(input_audio)

        # Get durations
        video_duration = video.duration
        audio_duration = audio.duration

        if video_duration > audio_duration:
            print(f"\nVideo duration is longer than the audio. I will add silence {video_duration - audio_duration:.2f} seconds at the end of your audio.\n")
            shutil.copy(input_video, adjusted_video)
            silent_audio_duration = video_duration - audio_duration
            VideoAudioAdjustment.create_silent_audio(silent_audio_duration, silent_audio_path)
            silent_audio = mp.AudioFileClip(silent_audio_path)
            audio_adjusted = mp.concatenate_audioclips([audio, silent_audio])
            audio_adjusted.write_audiofile(adjusted_audio)

        elif video_duration < audio_duration:
            print(f"\nVideo duration is shorter than the audio. I will adjust the speed of the video, by adding {audio_duration - video_duration:.2f} seconds to the duration of your video!\n")
            shutil.copy(input_audio, adjusted_audio)
            speed_factor = audio_duration / video_duration
            video_adjusted = video.fx(mp.vfx.speedx, speed_factor)
            video_adjusted.write_videofile(adjusted_video, audio=None)

        else:
            print("\nVideo duration = audio duration. I will just move the files to the right directory for further processing!\n")
            shutil.copy(input_video, adjusted_video)
            shutil.copy(input_audio, adjusted_audio)

        # Convert audio to aac
        VideoAudioAdjustment.convert_audio_to_aac(adjusted_audio, adjusted_audio_aac)

        # Create silent_audio_lipsync.wav with the same duration as adjusted_audio
        adjusted_audio_duration = mp.AudioFileClip(adjusted_audio).duration
        VideoAudioAdjustment.create_silent_audio(adjusted_audio_duration, silent_audio_lipsync_path)
