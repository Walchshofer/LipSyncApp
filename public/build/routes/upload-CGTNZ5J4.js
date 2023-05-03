import {
  __toESM,
  require_jsx_dev_runtime
} from "/build/_shared/chunk-EETRBLDB.js";

// app/routes/upload.jsx
var import_jsx_dev_runtime = __toESM(require_jsx_dev_runtime());
function UploadPage() {
  const [video, setVideo] = useState(null);
  const [audio, setAudio] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);
  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);
    const formData = new FormData();
    formData.append("video", video);
    formData.append("audio", audio);
    try {
      const response = await fetch("/api/upload", {
        method: "POST",
        body: formData
      });
      if (!response.ok) {
        const { error: error2 } = await response.json();
        throw new Error(error2);
      }
      const { result: result2 } = await response.json();
      setResult(result2);
    } catch (error2) {
      setError(error2.message);
    } finally {
      setLoading(false);
    }
  }
  return /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("main", { id: "content", children: [
    /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("h1", { children: "Upload your video and audio" }, void 0, false, {
      fileName: "app/routes/upload.jsx",
      lineNumber: 40,
      columnNumber: 9
    }, this),
    /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("p", { children: "Upload a video (.mp4) and an audio (.wav) and lipsync audio to the video" }, void 0, false, {
      fileName: "app/routes/upload.jsx",
      lineNumber: 41,
      columnNumber: 9
    }, this),
    /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("form", { onSubmit: handleSubmit, children: [
      /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("div", { children: [
        /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("label", { htmlFor: "video", children: "Video" }, void 0, false, {
          fileName: "app/routes/upload.jsx",
          lineNumber: 47,
          columnNumber: 13
        }, this),
        /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)(
          "input",
          {
            type: "file",
            id: "video",
            accept: "video/mp4",
            onChange: (e) => setVideo(e.target.files[0])
          },
          void 0,
          false,
          {
            fileName: "app/routes/upload.jsx",
            lineNumber: 48,
            columnNumber: 13
          },
          this
        )
      ] }, void 0, true, {
        fileName: "app/routes/upload.jsx",
        lineNumber: 46,
        columnNumber: 13
      }, this),
      /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("div", { children: [
        /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("label", { htmlFor: "audio", children: "Audio" }, void 0, false, {
          fileName: "app/routes/upload.jsx",
          lineNumber: 56,
          columnNumber: 13
        }, this),
        /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)(
          "input",
          {
            type: "file",
            id: "audio",
            accept: "audio/wav",
            onChange: (e) => setAudio(e.target.files[0])
          },
          void 0,
          false,
          {
            fileName: "app/routes/upload.jsx",
            lineNumber: 57,
            columnNumber: 13
          },
          this
        )
      ] }, void 0, true, {
        fileName: "app/routes/upload.jsx",
        lineNumber: 55,
        columnNumber: 13
      }, this),
      /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("button", { type: "submit", disabled: loading, children: loading ? "Loading..." : "Upload" }, void 0, false, {
        fileName: "app/routes/upload.jsx",
        lineNumber: 64,
        columnNumber: 13
      }, this)
    ] }, void 0, true, {
      fileName: "app/routes/upload.jsx",
      lineNumber: 45,
      columnNumber: 9
    }, this),
    error && /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("p", { className: "error", children: error }, void 0, false, {
      fileName: "app/routes/upload.jsx",
      lineNumber: 68,
      columnNumber: 19
    }, this),
    result && /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("div", { children: [
      /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("h2", { children: "Result" }, void 0, false, {
        fileName: "app/routes/upload.jsx",
        lineNumber: 71,
        columnNumber: 13
      }, this),
      /* @__PURE__ */ (0, import_jsx_dev_runtime.jsxDEV)("video", { controls: true, src: result }, void 0, false, {
        fileName: "app/routes/upload.jsx",
        lineNumber: 72,
        columnNumber: 13
      }, this)
    ] }, void 0, true, {
      fileName: "app/routes/upload.jsx",
      lineNumber: 70,
      columnNumber: 13
    }, this)
  ] }, void 0, true, {
    fileName: "app/routes/upload.jsx",
    lineNumber: 39,
    columnNumber: 9
  }, this);
}
export {
  UploadPage as default
};
//# sourceMappingURL=/build/routes/upload-CGTNZ5J4.js.map
