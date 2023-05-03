# esrgan_blurdetection2.py

# ... other imports ...
import base64
from utils.esrgan_blurdetection2 import ESRGANBlurDetection2
from moviepy.editor import VideoFileClip

# ... app and process_image function ...

@app.route('/process-video', methods=['POST'])
def process_video():
    data = request.get_json(force=True)
    video_base64 = data['video']
    video_data = base64.b64decode(video_base64)

    with open("temp_input.mp4", "wb") as f:
        f.write(video_data)

    input_clip = VideoFileClip("temp_input.mp4")

    def process_frame(frame):
        img_np, _, _ = process_image(Image.fromarray(frame))
        return img_np

    processed_clip = input_clip.fl_image(process_frame)
    processed_clip.write_videofile("temp_output.mp4")

    with open("temp_output.mp4", "rb") as f:
        processed_video_base64
