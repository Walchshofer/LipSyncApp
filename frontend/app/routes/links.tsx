// Path: lip-sync-app/app/routes/links.tsx
import { useLoaderData } from 'react-router-dom';

// Define an interface for the data shape
interface LoaderData {
  message: string;
}

export default function Links() {
  // Use type assertion to tell TypeScript the shape of the data object
  let data = useLoaderData() as LoaderData;
  return (
    <div>
      <h2>Recommended Stock Video Sites</h2>
      <p>
        The LipSyncApp Team has curated a list of some of the best
        stock video sites. These sites offer a wide range of high-quality
        video footage for various purposes. We have also included our
        affiliate links, so you can support our project while
        finding the perfect video for your needs.
      </p>
      <ul>
        <li>
          <a href='https://www.shutterstock.com/affiliate' target='_blank' rel='noopener noreferrer'>
            Shutterstock
          </a>
        </li>
        <li>
          <a href='https://www.pond5.com/affiliate' target='_blank' rel='noopener noreferrer'>
            Pond5
          </a>
        </li>
        <li>
          <a href='https://www.storyblocks.com/affiliate' target='_blank' rel='noopener noreferrer'>
            Storyblocks
          </a>
        </li>
        <li>
          <a href='https://www.videvo.net/affiliate' target='_blank' rel='noopener noreferrer'>
            Videvo
          </a>
        </li>
      </ul>
      <p>{data.message}</p>
    </div>
  );
}

export function meta() {
  return {
    title: 'Links',
    description: 'Find recommended stock video sites and support LipSyncApp',
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
