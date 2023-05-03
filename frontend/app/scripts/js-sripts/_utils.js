// app/routes/_utils.js
import { createRequestHandler } from "@remix-run/express";
import multer from "multer";

export function createApiRoute(handler) {
  const storage = multer.diskStorage({
    destination: (req, file, cb) => {
      cb(null, "./uploads");
    },
    filename: (req, file, cb) => {
      cb(null, file.originalname);
    },
  });

  return createRequestHandler({
    getParams: () => ({}),
    loader: async ({ request, context }) => {
      const form = new FormData();
      request.body.pipe(form);

      const videoFile = form.get("input_video");
      const audioFile = form.get("input_audio");

      if (!videoFile || !audioFile) {
        return new Response("Please upload both .mp4 and .wav files.", {
          status: 400,
        });
      }

      // Call your SettingsUtility methods here to process the uploaded files
      await context.processFiles(videoFile.path, audioFile.path);

      return handler({ request, context });
    },
    action: multer({ storage }).fields([
      { name: "input_video" },
      { name: "input_audio" },
    ]),
  });
}
