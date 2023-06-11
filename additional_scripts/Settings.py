import os


class SettingUtilities:
    DEFAULT_LOCAL_PROJECT_PATH = "/home/patrick_wsl/AI_Projects/WebApps/LipSyncApp"

    def __init__(self, number_of_faces=1):
        self.number_of_faces = number_of_faces
        self.local_project_path = self.DEFAULT_LOCAL_PROJECT_PATH
        self._initialize_paths()

    def _initialize_paths(self):
        self.repos_path = os.path.join(self.local_project_path, "repos")
        self.work_data_path = os.path.join(self.local_project_path, "work_data")
        self.input_folder_path = os.path.join(self.work_data_path, "input_files")
        self.output_folder_path = os.path.join(self.work_data_path, "output_files")
        self.temp_folder_path = os.path.join(self.work_data_path, "temp_files")
        self.face_images_folder_path = os.path.join(self.temp_folder_path, "face_images")
        self.input_video_path = os.path.join(self.input_folder_path, "input_video.mp4")
        self.video_folder_path = os.path.join(self.temp_folder_path, "video")
        self.face_video_folder_path = os.path.join(self.video_folder_path, "face_videos")
        self.adjusted_video_folder_path = os.path.join(self.video_folder_path, "adjusted_video")
        self.adjusted_input_video_folder_path = self.input_video_path
        self.adjusted_video_output_folder_path = os.path.join(self.adjusted_video_folder_path, "output")
        self.adjusted_face_video_input_path = os.path.join(self.adjusted_input_video_folder_path, "input_video.mp4")
        self.adjusted_face_video_output_path = os.path.join(self.adjusted_video_output_folder_path, "video.mp4")
        self.split_video_folder_path = os.path.join(self.face_video_folder_path, "split_videos")
        self.split_video_input_folder_path = self.adjusted_video_output_folder_path
        self.split_video_output_folder_path = os.path.join(self.split_video_folder_path, "output")
        self.split_video_input_video_path = os.path.join(self.split_video_input_folder_path, "video.mp4")
        self.wav2lip_video_folder_path = os.path.join(self.face_video_folder_path, "wav2lip_videos")
        self.wav2lip_input_video_folder_path = self.split_video_folder_path
        self.wav2lip_output_video_folder_path = os.path.join(self.wav2lip_video_folder_path, "wav2lip_output")
        self.wav2lip_path = os.path.join(self.repos_path, "Wav2Lip")
        self.wav2lip_checkpoints_path = os.path.join(self.wav2lip_path, "checkpoints")
        self.wav2lip_checkpoint_wav2lip_name = "wav2lip.pth"
        self.wav2lip_checkpoint_wav2lip_gan_name = "wav2lip_gan.pth"
        self.wav2lip_checkpoint_wav2lip_path = os.path.join(self.wav2lip_checkpoints_path, self.wav2lip_checkpoint_wav2lip_name)
        self.wav2lip_checkpoint_wav2lip_gan_path = os.path.join(self.wav2lip_checkpoints_path, self.wav2lip_checkpoint_wav2lip_gan_name)
        self.overlay_video_folder_path = os.path.join(self.face_video_folder_path, "overlay_videos")
        self.overlay_input_video_folder_path = self.wav2lip_output_video_folder_path
        self.overlay_output_video_folder_path = os.path.join(self.overlay_video_folder_path, "output")
        self.blurdetection2_path = os.path.join(self.repos_path, "BlurDetection2")
        self.blurdetection2_video_folder_path = os.path.join(self.face_video_folder_path, "blurdetection2_videos")
        self.blurdetection2_input_video_path = self.overlay_output_video_folder_path
        self.blurdetection2_output_video_folder_path = os.path.join(self.blurdetection2_video_folder_path, "output")
        self.blurdetection2_model_name = "model.pth"
        self.blurdetection2_model_folder_path = os.path.join(self.blurdetection2_path, "models")
        self.blurdetection2_model_path = os.path.join(self.blurdetection2_model_folder_path, self.blurdetection2_model_name)
        self.esrgan_path = os.path.join(self.repos_path, "ESRGAN")
        self.esrgan_inhagcutils_path = os.path.join(self.esrgan_path, "inhagcutils.ipynb")
        self.esrgan_video_folder_path = os.path.join(self.face_video_folder_path, "esrgan_videos")
        self.esrgan_input_video_folder_path = self.blurdetection2_output_video_folder_path
        self.esrgan_output_video_dir_path = self.output_folder_path
        self.esrgan_model_name = "RRDB_ESRGAN_x4.pth"
        self.esrgan_model_dejpeg_name = "RRDB_ESRGAN_x4_dejpeg.pth"
        self.esrgan_dejpeg_dir_path = os.path.join(self.temp_folder_path, "ESRGAN", "dejpeg")
        self.esrgan_tmp_dir_path = os.path.join(self.temp_folder_path, "ESRGAN", "tmp")
        self.esrgan_mask_dir_path = os.path.join(self.temp_folder_path, "ESRGAN", "tmp", "mask")
        self.esrgan_upscaled_dir_path = os.path.join(self.temp_folder_path, "ESRGAN", "upscaled")
        self.esrgan_models_dir_path = os.path.join(self.esrgan_path, "models")
        self.esrgan_model_path = os.path.join(self.esrgan_models_dir_path, self.esrgan_model_name)
        self.esrgan_model_dejpeg_path = os.path.join(self.esrgan_models_dir_path, self.esrgan_model_dejpeg_name)
        self.input_audio_path = os.path.join(self.input_folder_path, "input_audio.wav")
        self.audio_folder_path = os.path.join(self.temp_folder_path, "audio")
        self.silent_audio_folder_path = os.path.join(self.audio_folder_path, "silent")
        self.adjusted_audio_folder_path = os.path.join(self.audio_folder_path, "adjusted")
        self.wav2lip_input_silent_audio_path = os.path.join(self.silent_audio_folder_path, "silent_audio_lipsync.wav")
        self.wav2lip_input_audio_path = os.path.join(self.adjusted_audio_folder_path, "adjusted_audio.wav")
        self.esrgan_audio_folder_path = os.path.join(self.esrgan_path, "audio")

    def create_directories(self):
        directories = [
            self.work_data_path,
            self.input_folder_path,
            self.output_folder_path,
            self.temp_folder_path,
            self.face_images_folder_path,
            self.video_folder_path,
            self.face_video_folder_path,
            self.adjusted_video_folder_path,
            self.adjusted_input_video_folder_path,
            self.adjusted_video_output_folder_path,
            self.split_video_folder_path,
            self.split_video_input_folder_path,
            self.split_video_output_folder_path,
            self.wav2lip_video_folder_path,
            self.wav2lip_input_video_folder_path,
            self.wav2lip_output_video_folder_path,
            self.overlay_video_folder_path,
            self.overlay_input_video_folder_path,
            self.overlay_output_video_folder_path,
            self.blurdetection2_video_folder_path,
            self.blurdetection2_input_video_path,
            self.blurdetection2_output_video_folder_path,
            self.esrgan_video_folder_path,
            self.esrgan_input_video_folder_path,
            self.esrgan_output_video_dir_path,
            self.esrgan_dejpeg_dir_path,
            self.esrgan_tmp_dir_path,
            self.esrgan_mask_dir_path,
            self.esrgan_upscaled_dir_path,
            self.audio_folder_path,
            self.silent_audio_folder_path,
            self.adjusted_audio_folder_path,
            self.esrgan_audio_folder_path,
        ]

        for directory in directories:
            os.makedirs(directory, exist_ok=True)

    def generate_dynamic_files(self):
        for i in range(self.number_of_faces):
            face_image_template = self.face_image_template_path.format(i=i)
            split_face_video_output_template = self.split_face_video_output_template_path.format(i=i)
            wav2lip_input_video_template = self.wav2lip_input_video_template_path.format(i=i)
            wav2lip_output_video_template = self.wav2lip_output_video_template_path.format(i=i)
            overlay_input_video_template = self.overlay_input_video_template_path.format(i=i)

            setattr(self, f"face_image_{i}_path", face_image_template)
            setattr(self, f"split_face_video_output_{i}_path", split_face_video_output_template)
            setattr(self, f"wav2lip_input_video_{i}_path", wav2lip_input_video_template)
            setattr(self, f"wav2lip_output_video_{i}_path", wav2lip_output_video_template)
            setattr(self, f"overlay_input_video_{i}_path", overlay_input_video_template)

    def update_path(self, attribute_name, new_value):
        if hasattr(self, attribute_name):
            setattr(self, attribute_name, new_value)
        else:
            raise AttributeError(f"No attribute named {attribute_name} found")

    def reset_to_default(self, attribute_name):
        if attribute_name in self.default_paths:
            setattr(self, attribute_name, self.default_paths[attribute_name])
        else:
            raise AttributeError(f"No attribute named {attribute_name} found in the default paths")

    def set_paths(self, **kwargs):
        for attribute_name, new_value in kwargs.items():
            self.update_path(attribute_name, new_value)

    def get_path(self, attribute_name):
        if hasattr(self, attribute_name):
            return getattr(self, attribute_name)
        else:
            raise AttributeError(f"No attribute named {attribute_name} found")


if __name__ == "__main__":
    settings = SettingUtilities()
    settings.create_directories()
    settings.generate_dynamic_files()
    settings.update_path("input_folder_path", "new_input_folder_path")
    settings.reset_to_default("input_folder_path")
    settings.set_paths(input_folder_path="new_input_folder_path", output_folder_path="new_output_folder_path")
    settings.get_path("input_folder_path")
