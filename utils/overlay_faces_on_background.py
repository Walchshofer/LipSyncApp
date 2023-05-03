import os
import cv2
from tqdm import tqdm
from utils.settings_utilities import SettingUtilities

class OverlayFacesBG:
    def __init__(self, settings: SettingUtilities):
        self.settings = settings

    def overlay_faces_on_background(self, input_background, input_faces, face_masks_list, temp_dir, output_video):
        background_capture = cv2.VideoCapture(input_background)
        fps = int(background_capture.get(cv2.CAP_PROP_FPS))
        width = int(background_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(background_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        background_capture.release()

        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        temp_background_video = os.path.join(temp_dir, "temp_background.mp4")

        total_frames = sum([len(face_masks) for face_masks in face_masks_list])

        progress_bar = tqdm(total=total_frames, desc="Overlaying faces", ncols=100)

        for face_video, face_masks in zip(input_faces, zip(*face_masks_list)):
            input_background_capture = cv2.VideoCapture(input_background)
            temp_background_writer = cv2.VideoWriter(temp_background_video, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

            while True:
                success, frame = input_background_capture.read()
                if not success:
                    break
                temp_background_writer.write(frame)

            input_background_capture.release()
            temp_background_writer.release()

            temp_background_capture = cv2.VideoCapture(temp_background_video)
            output_writer = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

            face_capture = cv2.VideoCapture(face_video)

            for frame_number, face_mask in enumerate(face_masks):
                success, background_frame = temp_background_capture.read()
                if not success:
                    break

                success, face_frame = face_capture.read()
                if not success:
                    break

                resized_face = cv2.resize(face_frame, (face_mask.shape[1], face_mask.shape[0]))
                background_frame[np.where(face_mask != 0)] = resized_face[np.where(face_mask != 0)]
                output_writer.write(background_frame)

                progress_bar.update(1)

            face_capture.release()
            temp_background_capture.release()
            output_writer.release()
            input_background = output_video

        os.remove(temp_background_video)
        progress_bar.close()
        print("Faces overlaid on the background.")
