from pathlib import Path
import subprocess

def convert_to_ogg(directory: Path):
   for wav_file in directory.rglob("*.wav"):
       ogg_file = wav_file.with_suffix(".ogg")
       subprocess.run([
           "ffmpeg", "-i", str(wav_file),
           "-c:a", "libvorbis", "-qscale:a", "10",
           str(ogg_file)
       ])
       wav_file.unlink()

if __name__ == "__main__":
   directory = Path("../sample_packs")
   convert_to_ogg(directory)