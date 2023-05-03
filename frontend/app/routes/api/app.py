# settings_api.py
from flask import Flask, jsonify
from .......utils.settings_utilities import SettingUtilities

app = Flask(__name__)

settings = SettingUtilities(number_of_faces=5)

@app.route('/api/lipSync', methods=['POST'])
def lip_sync():
    # Add the code to run your Python script here

    # Return a JSON response
    return jsonify({"message": "Lip sync completed"})


@app.route('/api/settings', methods=['GET'])
def get_settings():
    face_image_paths = [settings.get_path(f"face_image_{i}_path") for i in range(settings.number_of_faces)]
    return jsonify({'face_image_paths': face_image_paths})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
