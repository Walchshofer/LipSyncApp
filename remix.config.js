import * as LipSyncApp from './app/routes/LipSyncApp';
import * as About from './app/routes/about';  
import * as Upload from './app/routes/upload';
import * as Links from './app/routes/links'; 
import * as NotFound from './app/routes/404';  
import * as ServerError from './app/routes/500';   

/** @type {import('@remix-run/dev').AppConfig } */
export default {
  routes(loader) { 
    loader.addRoute('/about', About);
    loader.addRoute('/upload', Upload);
    loader.addRoute('/links', Links); 
    loader.addRoute('/404', NotFound);
    loader.addRoute('/500', ServerError); 
    loader.addRoute('/*', LipSyncApp);
  },
  ignoredRouteFiles: ["**/.*"],
  // appDirectory: "app",
  // assetsBuildDirectory: "public/build",
  // serverBuildPath: "build/index.js",
  // publicPath: "/build/", 
  future: {
    v2_errorBoundary: true,
    v2_meta: true,
    v2_normalizeFormMethod: true,
    v2_routeConvention: true, 
  }
}