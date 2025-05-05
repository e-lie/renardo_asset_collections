from pathlib import Path
import wave
import subprocess
import json
from collections import defaultdict

def get_audio_info(file_path: Path) -> tuple:
   """Get channels and sample rate using ffprobe"""
   cmd = [
       'ffprobe', '-v', 'quiet', '-print_format', 'json',
       '-show_streams', str(file_path)
   ]
   result = subprocess.run(cmd, capture_output=True, text=True)
   info = json.loads(result.stdout)
   if 'streams' in info:
       stream = info['streams'][0]
       return stream.get('channels', 0), int(stream.get('sample_rate', 0))
   return 0, 0

def analyze_audio_files(directory: Path):
   formats = defaultdict(int)
   channels = defaultdict(int)
   sample_rates = defaultdict(int)
   
   for audio_file in directory.rglob('*'):
       if not audio_file.is_file():
           continue
           
       ext = audio_file.suffix.lower()
       if ext in ['.wav', '.flac', '.ogg', '.mp3', '.aiff']:
           formats[ext] = formats[ext] + 1
           channels_count, sample_rate = get_audio_info(audio_file)
           channels[channels_count] += 1
           sample_rates[sample_rate] += 1
   
   print("File formats:")
   for fmt, count in formats.items():
       print(f"{fmt}: {count}")
       
   print("\nChannels:")
   for ch, count in channels.items():
       print(f"{ch} channels: {count}")
       
   print("\nSample rates:")
   for rate, count in sample_rates.items():
       print(f"{rate} Hz: {count}")

if __name__ == "__main__":
   analyze_audio_files(Path('../sample_packs'))