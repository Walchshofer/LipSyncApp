# LipSync Web App README

The LipSync Web App is a beta version of a web application that allows users to create lip sync videos using a variety of audio and video sources. The app uses advanced machine learning algorithms to analyze the audio and video sources and generate a realistic lip sync video. The app is easy to use and requires no prior experience with video editing or machine learning.

The LipSync Web App is built using a REMIX frontend and a Python backend. The app is deployed on AWS servers to ensure fast and reliable performance.

Users can sign up for free to test the LipSync Web App until further notice. The app is still in beta version, so users may experience some bugs or glitches. However, the development team is working hard to fix any issues and improve the app's performance.

# Submodules used:
- LipSyncApp Main Repository: https://github.com/Walchshofer/LipSyncApp
- Wav2Lip: https://github.com/Walchshofer/Wav2Lip
- ESRGAN: https://github.com/Walchshofer/ESRGAN
- BlurDetection2: https://github.com/Walchshofer/BlurDetection2

These submodules are used to provide advanced machine learning algorithms for audio and video analysis and processing.


# How to deploy REMIX!

- [Remix Docs](https://remix.run/docs)

## Development

From your terminal:

```sh
npm run dev
```

This starts your app in development mode, rebuilding assets on file changes.

## Deployment

First, build your app for production:

```sh
npm run build
```

Then run the app in production mode:

```sh
npm start
```

Now you'll need to pick a host to deploy it to.

### DIY

If you're familiar with deploying node applications, the built-in Remix app server is production-ready.

Make sure to deploy the output of `remix build`

- `build/`
- `public/build/`

### Using a Template

When you ran `npx create-remix@latest` there were a few choices for hosting. You can run that again to create a new project, then copy over your `app/` folder to the new project that's pre-configured for your target server.

```sh
cd ..
# create a new project, and pick a pre-configured host
npx create-remix@latest
cd my-new-remix-app
# remove the new project's app (not the old one!)
rm -rf app
# copy your app over
cp -R ../my-old-remix-app/app app
```
