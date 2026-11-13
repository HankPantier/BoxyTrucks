# Voiceover (Hank, Nov 13, 2026)

"I like B best - please use that any time we use a voice."

- Voice: Piper TTS `en_US-joe-medium` (voice B). Settings: `--length-scale 1.0 --noise-scale 0.8 --noise-w-scale 1.0`.
- Install: `pip install --break-system-packages piper-tts`, then download the model (60 MB, not kept in git):
  `curl -sSL -o en_US-joe-medium.onnx https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx`
  (the .onnx.json config is in this folder).
- Script style: conversational, like talking someone through it in the garage ("So this is...", "Honestly?").
  Facts only from the site data. The voice talks about "Hank's G 500", never speaks as Hank.
