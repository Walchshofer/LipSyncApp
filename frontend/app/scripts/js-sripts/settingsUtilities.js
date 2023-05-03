const { PythonShell } = require("python-shell");

class SettingsUtilities {
  static async processFiles(inputVideoPath, inputAudioPath) {
    const options = {
      mode: "text",
      pythonOptions: ["-u"], // get print results in real-time
      scriptPath: "./path/to/your/python/code", // set the path to your Python code
      args: [inputVideoPath, inputAudioPath],
    };

    return new Promise((resolve, reject) => {
      PythonShell.run("settings_utilities.py", options, (err, results) => {
        if (err) {
          reject(err);
        } else {
          resolve(results);
        }
      });
    });
  }
}

module.exports = SettingsUtilities;
