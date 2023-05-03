// Path: lip-sync-app/app/routes/about.tsx
import { useLoaderData } from 'react-router-dom';

// Define an interface for the data shape
interface LoaderData {
  message: string;
}

export default function About() {
  // Use type assertion to tell TypeScript the shape of the data object
  let data = useLoaderData() as LoaderData;
  return (
    <div>
      <h2>About LipSyncApp</h2>
      <p>
        LipSyncApp is an innovative application that enables users to
        synchronize an audio track with a video by utilizing deepfake
        technology. By uploading a video (in .mp4 format) and an audio
        track (in .wav format), users can create lifelike lip-sync
        animations for multiple faces within the video.
      </p>
      <p>
        Our application is currently in the early beta stage, and we
        appreciate your feedback and support as we continue to improve
        its functionality and user experience.
      </p>
      <p>{data.message}</p>
    </div>
  );
}

export function meta() {
  return {
    title: 'About',
    description: 'Learn more about the LipSyncApp',
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
