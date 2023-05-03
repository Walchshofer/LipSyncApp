import Index from '../_index';
import UploadPage from '../upload';
import { createApiRoute } from './_utils';

const routes = [
  {
    path: '',
    method: 'get',
    loader: Index,
  },
  {
    path: 'upload',
    method: 'get',
    loader: UploadPage,
  },
  {
    path: 'api/upload',
    method: 'post',
    handler: createApiRoute(async ({ request, context }) => {
      return new Response('Files uploaded and processed successfully.');
    }),
  },
];

export default routes;
