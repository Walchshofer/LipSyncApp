import os
import cv2
import numpy as np
import face_recognition
from moviepy.editor import ImageClip
from tqdm import tqdm

class SplitFacesBG:

    @staticmethod
    def create_face_mask(frame, face_location, frame_number, face_index):
        top, right, bottom, left = face_location
        height, width, _ = frame.shape

        padding_width = int((right - left) * 0.8)
        padding_height = int((bottom - top) * 0.8)

        left = max(0, left - padding_width)
        top = max(0, top - padding_height)
        right = min(width, right + padding_width)
        bottom = min(height, bottom + padding_height)

        face_mask = np.zeros((height, width), dtype=np.uint8)
        face_mask[top:bottom, left:right] = 255

        return face_mask

    @staticmethod
    def interpolate_face_position(face_locations):
        x_coords = [loc[1] + (loc[3] - loc[1]) // 2 for loc in face_locations]
        y_coords = [loc[0] + (loc[2] - loc[0]) // 2 for loc in face_locations]
        new_x = int(sum(x_coords) / len(x_coords))
        new_y = int(sum(y_coords) / len(y_coords))
        return new_x, new_y

    @staticmethod
    def save_face_image(input_frame, face_location, face_index, output_folder):
        top, right, bottom, left = face_location
        face_image = input_frame[top:bottom, left:right]
        face_image = cv2.resize(face_image, (400, 255))
        cv2.imwrite(os.path.join(output_folder, f"face_{face_index + 1}.png"), face_image)

    @staticmethod
    def separate_faces_and_background(input_video, output_background_path, face_image_path_template, face_image_root_path):

        video_capture = cv2.VideoCapture(input_video)
        fps = int(video_capture.get(cv2.CAP_PROP_FPS))
        width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

        success, frame = video_capture.read()
        if not success:
            raise Exception("Could not read the input video.")

        # Define face_locations after reading the first frame from the video
        face_locations = face_recognition.face_locations(frame)

        background_writer = cv2.VideoWriter(output_background_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))
        # Create a video writer for each face
        face_writers = [cv2.VideoWriter(f"{output_face_video_path_template.format(i=i + 1)}", cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)) for i in range(len(face_locations))]
        
        if not success:
            raise Exception("Could not read the input video.")

        frame_number = 0
        face_locations = face_recognition.face_locations(frame)
        face_trackers = {i: cv2.TrackerKCF_create() for i in range(len(face_locations))}

        for i, face_location in enumerate(face_locations):
            top, right, bottom, left = face_location
            tracker = face_trackers[i]
            tracker.init(frame, (left, top, right - left, bottom - top))

             # Save the first frame of each face as an image
            SplitFacesBG.save_face_image(frame, face_location, i, output_face_images_folder_path)

        face_positions_list = []
        face_masks_list = []

        with tqdm(total=total_frames, desc="Processing frames") as progress_bar:
            while success:
                success, frame = video_capture.read()
                if not success:
                    break

                frame_number += 1

                updated_face_locations = []

                for i, tracker in face_trackers.items():
                    success, bbox = tracker.update(frame)
                    if success:
                        x, y, w, h = [int(v) for v in bbox]
                        updated_face_locations.append((y, x + w, y + h, x))
                    else:
                        x, y = SplitFacesBG.interpolate_face_position(face_locations[i])
                        updated_face_locations.append((y - h // 2, x + w // 2, y + h // 2, x - w // 2))

                face_positions_list.append(updated_face_locations)

                background_frame = frame.copy()

                current_frame_face_masks = []
                for i, face_location in enumerate(updated_face_locations):
                    face_mask = SplitFacesBG.create_face_mask(frame, face_location, frame_number, i)
                    current_frame_face_masks.append(face_mask)

                    face_frame = frame.copy()
                    face_frame[np.where(face_mask == 0)] = 0
                    background_frame[np.where(face_mask != 0)] = 0
                    face_writers[i].write(face_frame)

                face_masks_list.append(current_frame_face_masks)
                background_writer.write(background_frame)
                progress_bar.update(1)

        video_capture.release()
        background_writer.release()
        for face_writer in face_writers:
            face_writer.release()

        print("Finished processing input video.")
        return face_positions_list, face_masks_list

