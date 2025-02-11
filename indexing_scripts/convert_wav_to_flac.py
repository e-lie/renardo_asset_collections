from pathlib import Path
import subprocess
import sys

def convert_to_flac(directory: Path):
    for wav_file in directory.rglob("*.wav"):
        flac_file = wav_file.with_suffix(".flac")
        subprocess.run([
            "ffmpeg", "-i", str(wav_file),
            "-c:a", "flac",
            str(flac_file)
        ])
        wav_file.unlink()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert.py <directory>")
        sys.exit(1)
    directory = Path(sys.argv[1])
    convert_to_flac(directory)