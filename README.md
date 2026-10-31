<div align="center">
  <a href="https://youtu.be/h8dUTg2kEB8">
    <img src="https://img.youtube.com/vi/h8dUTg2kEB8/0.jpg" alt="Maya 2 TTS: Real-Time Voice Cloning in 1.1GB! (80ms CPU AI)">
  </a>
  <h3>📺 <a href="https://youtu.be/h8dUTg2kEB8">Watch the full tutorial on YouTube</a></h3>
</div>

# Maya 2 Native GGUF: Real-Time Multilingual Indic TTS

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Model Size: 2.5B Parameters](https://img.shields.io/badge/Model_Size-2.5B_Parameters-emerald.svg)](https://huggingface.co/maya-research/maya2-native)
[![VoiceArena Hindi Rank: #2](https://img.shields.io/badge/VoiceArena_Hindi-#2_Real--Time-orange.svg)](https://huggingface.co/maya-research/maya2-native)
[![Local Footprint: 1.1GB (Q4_K_M)](https://img.shields.io/badge/Local_Footprint-1.1GB_GGUF-purple.svg)](https://huggingface.co/Harsha001/Maya2-Native-GGUF)

> *"Maya 2 Native is an open-weights 2.5B parameter streaming text-to-speech engine delivering authentic localized rhythm, native accents, and code-switching across 11 Indic languages and English with ultra-low 80ms streaming latency and zero-shot cross-lingual voice cloning."*

---

## 📊 Production Test Workflows

| Workflow | Capability Tested | Input Artifact | Expected Deliverable |
|---|---|---|---|
| Multilingual Code-Switching Customer Bot | Smoothly switching between Hindi and English mid-sentence without awkward pauses | Customer support message inquiring about an order dispatch | Natural sounding spoken voice response confirming delivery details |
| Cross-Lingual Zero-Shot Podcast Dubber | Cloning an English speaker's voice to speak fluent Indian languages | Short eight-second voice recording of an English host | Cloned speaker voice reading translated podcast excerpts in Hindi and Marathi |
| Real-Time Multilingual Live Commentary | Testing high-tempo excitement, natural breathing, and rapid language switching at match pace | Fast-paced sports broadcasting script mixing Hindi and English match phrases | Energetic single-file live broadcast commentary audio |

---

## ⚡ Quick Start (Windows PowerShell)

```powershell
# Step 1: Create virtual environment, install requirements & download balanced GGUF weights
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install huggingface_hub soundfile numpy

hf download Harsha001/Maya2-Native-GGUF Maya2-Native-Q4_K_M.gguf --local-dir models
hf download Harsha001/Maya2-Native-GGUF mmproj-Maya2-Native-Q8_0.gguf --local-dir models

# Step 2: Build the native C++ llama-tts binary (Vulkan/CUDA/CPU)
git clone https://github.com/HarshaVardhan3002/ROCmFPX
cd ROCmFPX
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --target llama-tts -j
cd ..
```

```powershell
# Step 2: Run Production Pipeline
python main.py
```

---

## 🛡️ Practical Use Cases

- 🛡️ **Automated Multilingual Contact Centers**: Deploy on-premise voice agents that effortlessly switch between Hindi, Tamil, and Indian English mid-sentence without cloud latency or third-party API billing.
- 🎙️ **Cross-Lingual Media & Podcast Dubbing**: Take a 10-second vocal reference from an English creator and automatically generate their natural vocal clone speaking fluent Hindi, Bengali, or Marathi.
- ⚡ **Low-Latency Conversational AI**: Connect local LLMs directly to Maya 2 Native for sub-100ms voice responses in desktop assistants, robotics, and interactive kiosks.
- 📚 **Dramatized Audiobook Narration**: Generate entire audiobooks with dozens of distinct, emotionally expressive regional voices without studio recording costs.

---

## 🚀 Future Feature Roadmap

- ⚡ **Real-Time WebSocket Audio Streaming Server**: Live bidirectional audio socket integration for instantaneous browser microphone conversational agents.
- 🌐 **Expanded 22 Scheduled Indian Languages**: Extended phoneme adaptation covering all official constitutional Indian languages and regional dialects.
- 🎛️ **Emotion and Prosody Modulation Sliders**: Granular controls for pitch variance, speaking speed, excitement level, and whispered delivery.
- 📱 **Mobile and Edge On-Device NPU Compilations**: Direct ONNX and Qualcomm QNN deployments for sub-watt smartphone speech synthesis.

---

<sub>**Search Tags**: Maya 2 Native, Maya 2, Maya TTS, Maya Research, voice cloning, local TTS, offline TTS, ElevenLabs alternative, ElevenLabs competitor, free voice cloning, zero shot cloning, Indian AI voice, Hindi TTS, Tamil TTS, Marathi TTS, streaming TTS, Qwen3 TTS, CPU voice cloning, open weights TTS, AI voice generator, AI voice synthesis, AI voice cloning, Edge tts</sub>
