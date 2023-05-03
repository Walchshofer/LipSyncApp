// Path: lip-sync-app/app/routes/500.tsx
import { useLoaderData } from 'react-router-dom';

// Define an interface for the data shape
interface LoaderData {
  message: string;
}

export default function FiveHundred() {
  // Use type assertion to tell TypeScript the shape of the data object
  let data = useLoaderData() as LoaderData;
  return (
    <div>
      <h2>Yikes! Something went out of tune...</h2>
      <p>
        Our apologies, it seems our lip-sync performance hit a sour note.
        Our team is working hard to get back in harmony as soon as possible.
      </p>
      <p>
        While we fix things up, feel free to take the stage and try your luck on our{' '}
        <a href='/'>homepage</a>.
      </p>
      <p>{data.message}</p>
    </div>
  );
}

export function meta() {
  return {
    title: '500',
    description: 'This is the funny 500 page for LipSyncApp',
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
