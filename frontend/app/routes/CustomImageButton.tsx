import { useState } from 'react';
import CustomImageButton from '../components/CustomImageButton';

const YourParentComponent: React.FC = () => {
  const number_of_faces = 5; // Set the number_of_faces as needed

  // State to store the face images list
  const [faceImages, setFaceImages] = useState<string[]>(Array.from({length: number_of_faces}, (_, i) => `/path/to/face_${i + 1}.png`));

  // State to store the selected face index
  const [selectedFaceIndex, setSelectedFaceIndex] = useState<number>(-1);

  // Function to handle face button click
  const onFaceButtonClick = (index: number) => {
    console.log(`Face button ${index + 1} clicked`);
    setSelectedFaceIndex(index);
  };

  // Function to handle the lip-sync process
  const onStartLipSync = () => {
    if (selectedFaceIndex >= 0) {
      console.log(`Starting lip-sync process for face ${selectedFaceIndex + 1}`);
      // Your lip-sync logic here
    } else {
      console.log('No face selected for lip-sync.');
    }
  };

  return (
    <div>
      {faceImages.map((imageSrc, index) => (
        <CustomImageButton
          key={index}
          imageSrc={imageSrc}
          onClick={() => onFaceButtonClick(index)}
          altText={`Face ${index + 1}`}
        />
      ))}
      <button onClick={onStartLipSync}>Start LipSync</button>
    </div>
  );
};

export default YourParentComponent;
