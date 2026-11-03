(() => {
  const playPath = "M8 5.14v13.72L19.5 12 8 5.14z";
  const pausePath = "M6 5h4v14H6V5zm8 0h4v14h-4V5z";

  window.wireStemPlayer = function wireStemPlayer(audio, playBtn, icon) {
    function sync() {
      const on = !audio.paused;
      playBtn.classList.toggle("playing", on);
      playBtn.setAttribute("aria-label", on ? "Pause" : "Play");
      const path = icon.querySelector("path");
      if (path) path.setAttribute("d", on ? pausePath : playPath);
    }

    audio.addEventListener("play", sync);
    audio.addEventListener("pause", sync);
    sync();

    playBtn.addEventListener("click", () => {
      if (audio.paused) audio.play().catch(() => {});
      else audio.pause();
    });

    document.addEventListener("keydown", (e) => {
      if (e.code !== "Space") return;
      if (["INPUT", "TEXTAREA", "BUTTON"].includes(e.target.tagName)) return;
      e.preventDefault();
      if (audio.paused) audio.play().catch(() => {});
      else audio.pause();
    });

    try {
      const channel = new BroadcastChannel("layers-stems");
      channel.addEventListener("message", (event) => {
        if (event.data === "play" && audio.paused) {
          audio.play().catch(() => {});
        }
      });
    } catch {
      /* file:// tabs cannot always share a channel */
    }

    window.playStem = () => audio.play().catch(() => {});
  };
})();
