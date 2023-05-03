// Path: lip-sync-app/app/routes/404.tsx
import { useLoaderData } from 'react-router-dom';

// Define an interface for the data shape
interface LoaderData {
  message: string;
}

export default function FourOhFour() {
  // Use type assertion to tell TypeScript the shape of the data object
  let data = useLoaderData() as LoaderData;
  return (
    <div>
      <h2>Oops! This page is out of sync...</h2>
      <p>
        It looks like the page you're searching for has missed its cue.
        But don't worry, our expert lip-sync artists are on the case!
      </p>
      <p>
        In the meantime, why not head back to our{' '}
        <a href='/'>homepage</a> and give it another try?
      </p>
      <p>{data.message}</p>
    </div>
  );
}

export function meta() {
  return {
    title: '404',
    description: 'This is the funny 404 page for LipSyncApp',
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
