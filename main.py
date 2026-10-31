"""
Maya 2 Native GGUF - Production Inference Pipeline
Demonstrates 3 real-world speech workflows:
1. Multilingual Code-Switching Customer Bot
2. Cross-Lingual Zero-Shot Podcast Dubber
3. High-Speed Live Multilingual Sports & Tech Commentary
"""

import os
import subprocess
from pathlib import Path

# Paths configuration
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"
INPUTS_DIR = BASE_DIR / "inputs"
OUTPUTS_DIR = BASE_DIR / "outputs"

BACKBONE_GGUF = MODELS_DIR / "Maya2-Native-Q4_K_M.gguf"
MMPROJ_GGUF = MODELS_DIR / "mmproj-Maya2-Native-Q8_0.gguf"

# Platform-aware binary path (Windows: llama-tts.exe / Linux: llama-tts)
_bin_candidates = [
    BASE_DIR / "ROCmFPX" / "build" / "bin" / "llama-tts.exe",
    BASE_DIR / "ROCmFPX" / "build" / "bin" / "Release" / "llama-tts.exe",
    BASE_DIR / "ROCmFPX" / "build" / "bin" / "llama-tts",
    Path("llama-tts"),
]
BINARY_PATH = next((p for p in _bin_candidates if p.exists()), _bin_candidates[0])

# Inputs configuration

TASK1_INPUT_TEXT = (
    "Hello! Let me check that right away for you. Haan ji, aapka order number 9842 dispatch ho chuka hai "
    "aur aaj shaam 6 baje tak deliver ho jayega. Anything else I can assist you with today?"
)


VOICE_REF_AUDIO = INPUTS_DIR / "reference_clip_8s.wav"
VOICE_REF_TRANSCRIPT = (
    "Running locally, agents usually lock up your graphic card and freeze your computer screen while waiting for answers."
)

TASK2_INPUT_HINDI = "टेक होराइजन में आपका स्वागत है। आज हम रियल-टाइम न्यूरल ऑडियो नेटवर्क की चर्चा कर रहे हैं।"
TASK2_INPUT_MARATHI = "टेक होरायझन मध्ये आपले स्वागत आहे. आज आपण रियल-टाइम न्यूरल ऑडिओ तंत्रज्ञानाचा आढावा घेत आहोत."

# Task 3: 1-Click High-Speed Multilingual Live Sports/Tech Commentary (Single Generation Pass)
TASK3_COMMENTARY_TEXT = (
    "What an incredible finish! Last ball pe four runs needed, bowler runs in, aur ye utha ke maara mid-wicket ke upar! "
    "Absolute madness here at the stadium, ball goes soaring into the crowd for an unbelievable victory!"
)


def run_maya2_tts(
    text: str,
    voice: str = None,
    lang: str = "hi",
    output_wav: Path = OUTPUTS_DIR / "out.wav",
    ref_audio: Path = None,
    ref_transcript: str = None,
    gpu_layers: int = 99,
    seed: int = 42,
) -> Path:
    """Executes the native C++ llama-tts binary directly via subprocess."""
    formatted_prompt = f"{{{voice}}}: {text}" if voice else text
    output_wav.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        str(BINARY_PATH),
        "-m", str(BACKBONE_GGUF),
        "-mm", str(MMPROJ_GGUF),
        "-ngl", str(gpu_layers),
        "--tts-lang", lang,
        "-p", formatted_prompt,
        "-s", str(seed),
        "--output", str(output_wav),
    ]

    # Optional zero-shot voice cloning parameters when cloning from source audio
    if ref_audio and ref_audio.exists():
        cmd.extend(["--ref-audio", str(ref_audio)])
        if ref_transcript:
            cmd.extend(["--ref-text", ref_transcript])

    voice_label = voice if voice else f"Cloned ({ref_audio.name if ref_audio else 'Zero-Shot'})"
    print(f"[Maya2 Engine] Generating audio with voice={voice_label}, lang={lang}...")
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print(f"[Maya2 Engine] Saved output to: {output_wav}")
    return output_wav


def task1_codeswitch_customer_bot():
    """Workflow 1: Multilingual Code-Switching Customer Support Bot."""
    print("\n--- Workflow 1: Multilingual Code-Switching Customer Bot ---")
    output_wav = OUTPUTS_DIR / "task1_support_codeswitch.wav"
    run_maya2_tts(text=TASK1_INPUT_TEXT, voice="Ahana", lang="hi", output_wav=output_wav)
    print(f"[Workflow 1] Output ready: {output_wav}")


def task2_podcast_voice_dubber():
    """Workflow 2: Cross-Lingual Zero-Shot Podcast Dubbing Studio."""
    print("\n--- Workflow 2: Cross-Lingual Podcast Voice Dubber ---")
    hi_wav = OUTPUTS_DIR / "task2_podcast_hindi.wav"
    mr_wav = OUTPUTS_DIR / "task2_podcast_marathi.wav"

    # In dubbing mode, no preset voice tag is passed because the model clones directly from the reference audio clip
    run_maya2_tts(
        text=TASK2_INPUT_HINDI,
        lang="hi",
        output_wav=hi_wav,
        ref_audio=VOICE_REF_AUDIO,
        ref_transcript=VOICE_REF_TRANSCRIPT,
    )
    run_maya2_tts(
        text=TASK2_INPUT_MARATHI,
        lang="mr",
        output_wav=mr_wav,
        ref_audio=VOICE_REF_AUDIO,
        ref_transcript=VOICE_REF_TRANSCRIPT,
    )
    print(f"[Workflow 2] Outputs ready: {hi_wav}, {mr_wav}")


def task3_live_commentary():
    """
    Workflow 3: High-Speed Live Multilingual Sports & Tech Commentary.
    Tests Maya 2's high-tempo cadence, energy, and rapid code-switching in a single 1-click pass.
    """
    print("\n--- Workflow 3: High-Speed Live Commentary (Single 1-Click Pass) ---")
    commentary_wav = OUTPUTS_DIR / "task3_fast_live_commentary.wav"
    run_maya2_tts(
        text=TASK3_COMMENTARY_TEXT,
        voice="Ritvik",
        lang="hi",
        output_wav=commentary_wav,
    )
    print(f"[Workflow 3] Live commentary deliverable ready: {commentary_wav}")


def main():
    print("=" * 60)
    print("  Maya 2 Native GGUF Production Pipeline Execution")
    print("=" * 60)
    task1_codeswitch_customer_bot()
    task2_podcast_voice_dubber()
    task3_live_commentary()
    print("\nAll 3 voice output workflows completed successfully!")


if __name__ == "__main__":
    main()
