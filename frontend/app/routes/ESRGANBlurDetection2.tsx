import React, { useState } from 'react';
import { ESRGANBlurDetection2 } from './utils/ESRGANBlurDetection2';

const ESRGANBlurDetection: React.FC = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [videoSrc, setVideoSrc] = useState<string | null>(null);
  const [processedVideoSrc, setProcessedVideoSrc] = useState<string | null>(null);

  const esrganBlurDetection = new ESRGANBlurDetection2();

  const fileChangedHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      setSelectedFile(event.target.files[0]);
      setVideoSrc(URL.createObjectURL(event.target.files[0]));
    }
  };

  const uploadHandler = async () => {
    if (selectedFile) {
      const reader = new FileReader();
      reader.onloadend = async () => {
        const base64 = reader.result?.toString().split(',')[1];
        if (base64) {
          const response = await esrganBlurDetection.processVideo(base64);
          setProcessedVideoSrc(`data:video/mp4;base64,${response}`);
        }
      };
      reader.readAsDataURL(selectedFile);
    }
  };

  return (
    <div>
      <input type='file' onChange={fileChangedHandler} accept='video/*' />
      <button onClick={uploadHandler}>Upload</button>
      {videoSrc && <video src={videoSrc} controls />}
      {processedVideoSrc && <video src={processedVideoSrc} controls />}
    </div>
  );
};

export default ESRGANBlurDetection;


import axios from 'axios';
import { SettingsUtilities } from './SettingsUtilities';

export class ESRGANBlurDetection2 {
  private settings: SettingsUtilities;

  constructor() {
    this.settings = new SettingsUtilities();
  }

  async processVideo(base64: string): Promise<string> {
    const response = await axios.post(
      `${this.settings.get('api_base_url')}/process-video`,
      { video: base64 },
      { headers: { 'Content-Type': 'application/json' } }
    );

    return response.data.processedVideo;
  }
}
