import os
import shutil
import subprocess
from SettingsUtilities import SettingsUtilities

class LipSync:
    def __init__(self):
        # Initialize paths and variables from SettingsUtility
        self.SettingsUtility = SettingsUtilities()
        self.wav2lip_path = self.SettingsUtility.get_wav2lip_path()
        self.wav2lip_checkpoint_wav2lip_path = self.SettingsUtility.get_wav2lip_checkpoint_wav2lip_path()
        self.wav2lip_checkpoint_wav2lip_gan_path = self.SettingsUtility.get_wav2lip_checkpoint_wav2lip_gan_path()

    
    @staticmethod
    def get_audio_settings(index):
        SettingsUtility = SettingsUtilities()
        return SettingsUtility.get_audio_settings(index)

    @staticmethod
    def lip_sync_video(face_video_path, audio_path, output_video_path, no_smooth, resize_factor, face_det_batch_size, wav2lip_batch_size):
        SettingsUtility = SettingsUtilities()
        wav2lip_path = SettingsUtility.get_wav2lip_path()
        wav2lip_checkpoint_wav2lip_path = SettingsUtility.get_wav2lip_checkpoint_wav2lip_path()
        wav2lip_checkpoint_wav2lip_gan_path = SettingsUtility.get_wav2lip_checkpoint_wav2lip_gan_path()

        checkpoint_path = (
            wav2lip_checkpoint_wav2lip_path
            if SettingsUtility.get_wav2lip_preset() == "Fast"
            else wav2lip_checkpoint_wav2lip_gan_path
        )

        process = subprocess.Popen(
            [
                "python",
                f"{wav2lip_path}inference.py",
                "--checkpoint_path",
                checkpoint_path,
                "--face",
                face_video_path,
                "--audio",
                audio_path,
                "--outfile",
                output_video_path,
                "--no_smooth",
                str(no_smooth),
                "--resize_factor",
                str(resize_factor),
                "--face_det_batch_size",
                str(face_det_batch_size),
                "--wav2lip_batch_size",
                str(wav2lip_batch_size),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print("Error occurred during lip-sync:")
            print(stderr.decode("utf-8"))
        else:
            print("Lip-sync process completed successfully:")
            print(stdout.decode("utf-8"))

        return output_video_path

    @staticmethod
    def lip_sync_face_video(index):
        SettingsUtility = SettingsUtilities()
        audio_setting = LipSync.get_audio_settings(index)
        video_path = f"{SettingsUtility.get_face_video_root_path()}output_face_{index + 1}.mp4"

        if audio_setting == "process_audio":
            audio_path = SettingsUtility.get_adjusted_audio_path()
        elif audio_setting == "silent_audio":
            audio_path = SettingsUtility.get_silent_audio_path()
        else:  # "do_not_process"
            audio_path = None
        output_path = f"{SettingsUtility.get_overlay_files_root_path()}output_face{index + 1}_lipsync.mp4"

        # Set advanced settings
        no_smooth =  SettingsUtility.get_no_smooth_value()
        resize_factor = SettingsUtility.get_resize_factor_value() 
        face_det_batch_size = SettingsUtility.get_face_det_batch_size_value()
        wav2lip_batch_size = SettingsUtility.get_wav2lip_batch_size_value()

        if audio_path is not None:
            LipSync.lip_sync_video(
                video_path,
                audio_path,
                output_path,
                no_smooth,
                resize_factor,
                face_det_batch_size,
                wav2lip_batch_size,
            )
        else:
            shutil.copy(video_path, output_path)

        return output_path

if __name__ == '__main__':
    lipsync = LipSync()