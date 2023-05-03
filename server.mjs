import '@babel/register';
import path from 'path';
import express from 'express';
import { createRequestHandler } from '@remix-run/express';
import { Link } from '@remix-run/react';
import Index from './app/routes/_index.jsx';
import UploadPage from './app/routes/api/upload.jsx';

function createApiRoute(handler) {
  return async function (req, res) {
    try {
      const response = await handler({ request: req });
      res.status(200).json(response);
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
  };
}

const app = express();

app.all(
  '*',
  createRequestHandler({
    getLoadContext() {
      // Whatever you return here will be passed as `context` to your loaders.
    },
    // Explicitly set the routesPath
    routes: [
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
          return { message: 'Files uploaded and processed successfully.' };
        }),
      },
    ],
    Link,
    routesPath: path.resolve(process.cwd(), 'app/routes'),
  })
);

export default app;
