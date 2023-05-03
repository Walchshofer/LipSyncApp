import React, { useEffect, useState } from "react";
import OverlayFacesBG from "./path/to/OverlayFacesBG";

const overlayFacesBG = new OverlayFacesBG();

const OverlayFacesOnBackground: React.FC = () => {
  const [status, setStatus] = useState("idle");
  const [progress, setProgress] = useState(0);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchSettings = async () => {
      setStatus("fetching");
      try {
        // Initialize OverlayFacesBG with settings from SettingsUtilities
        await overlayFacesBG.init();
      } catch (err) {
        setError(`Error initializing OverlayFacesBG: ${err.message}`);
      } finally {
        setStatus("idle");
      }
    };

    fetchSettings();
  }, []);

  const startOverlaying = async () => {
    setStatus("overlaying");
    try {
      await overlayFacesBG.start();
      setProgress(overlayFacesBG.getProgress());
      setError(overlayFacesBG.getError());
    } catch (err) {
      setError(`Error overlaying faces: ${err.message}`);
    } finally {
      setStatus("idle");
    }
  };

  useEffect(() => {
    if (status === "idle") {
      startOverlaying();
    }
  }, [status]);

  return (
    <div>
      <h2>Overlay Faces on Background</h2>
      {status === "overlaying" && (
        <>
          <p>Progress: {progress}%</p>
          <p>Status: {status}</p>
        </>
      )}
      {error && <p>Error: {error}</p>}
    </div>
  );
};

export default OverlayFacesOnBackground;
