import { useState } from 'react';
import { } from 'react-router-dom';
import axios from 'axios';
import './index.css'; // Import the index.css file

export default function LipSyncApp() {
  const [mode, setMode] = useState('image');
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [imageSrc, setImageSrc] = useState<string | null>(null);
  const [videoSrc, setVideoSrc] = useState<string | null>(null);

  const handleModeChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setMode(e.target.value);
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setSelectedFile(e.target.files[0]);
      if (mode === 'image') {
        setImageSrc(URL.createObjectURL(e.target.files[0]));
      } else {
        setVideoSrc(URL.createObjectURL(e.target.files[0]));
      }
    }
  };

  const handleUpload = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);

      try {
        const response = await axios.post('/api/upload', formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
        });

        console.log(response.data);
      } catch (error) {
        console.error('An error occurred:', error);
      }
    }
  };

  const handleAdjustMp4Wav = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);
  
      try {
        const response = await axios.post('/api/adjust-mp4-wav', formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
        });
  
        console.log(response.data);
      } catch (error) {
        console.error('An error occurred:', error);
      }
    }
  };
  
 
  const handleSplitFacesFromBg = async () => {/* handleSplitFacesFromBg logic */};
  const handleLipSyncFaceVideo = async () => {/* handleLipSyncFaceVideo logic */};
  const handleBlurredDetection = async () => {/* handleBlurredDetection logic */};
  const handleUpscaleWithESRGAN = async () => {/* handleUpscaleWithESRGAN logic */};
  const handleDisplayAndDownloadMp4 = async () => {/* handleDisplayAndDownloadMp4 logic */};

  return (
    <main id='content'>
      {/* ... */}
      <div className='form-group'>
        <label htmlFor='mode'>Select Mode:</label>
        <select className='form-control' id='mode' name='mode' value={mode} onChange={handleModeChange}>
          <option value='image'>Upscale Image</option>
          <option value='video'>Lip Sync Video</option>
        </select>
      </div>

      {mode === 'image' && (
        <>
          <label htmlFor='image'>Select Image:</label>
          <input type='file' id='image' onChange={handleFileChange} accept='image/*' />
          {imageSrc && <img src={imageSrc} alt='Selected face' />}
        </>
      )}

      {mode === 'video' && (
        <>
          <label htmlFor='video'>Select Video:</label>
          <input type='file' id='video' onChange={handleFileChange} accept='video/*' />
          {videoSrc && (
            <video src={videoSrc} controls width='100%' />
          )}
        </>
      )}

      <button onClick={handleUpload}>Upload Files</button>
      <button onClick={handleAdjustMp4Wav}>Adjust MP4 and WAV</button>
      <button onClick={handleSplitFacesFromBg}>Split Faces From Background</button>
      <button onClick={handleLipSyncFaceVideo}>Lip Sync Face Video</button>
      <button onClick={handleBlurredDetection}>Blurred Detection</button>
      <button onClick={handleUpscaleWithESRGAN}>Upscale with ESRGAN</button>
      <button onClick={handleDisplayAndDownloadMp4}>Display and Download MP4</button>
    </main>
  );
}

export function meta() {
  return {
    title: 'LipSyncApp',
    description: 'Deepfake Videos with Lipsync for multiple faces',
  };
}

export function headers({ loaderHeaders }: { loaderHeaders: Headers }) {
  return {
    'Cache-Control': loaderHeaders.get('Cache-Control'),
  };
}

export function loader() {
  return { message: 'Hello from the loader!' };
}
