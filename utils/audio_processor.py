import yt_dlp
from pydub import AudioSegment
import os

#saves downloaded videos into a local folder
DOWNLOAD_DIR = 'downloades'
os.makedirs(DOWNLOAD_DIR,exist_ok = True)

def download_youtube_audio(url : str)-> str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")    #if video name is "study", it will get converted to "study.wav"
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": True,  #removes dowmload logs
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace(".webm", ".wav").replace(".m4a", ".wav")
    return filename


#converts dual audio to mono audio, converts it into 16KHZ to use it in whisper
def convert_to_wav(input_path: str) -> str:
    """Convert any audio/video file to WAV format using pydub."""
    output_path = os.path.splitext(input_path)[0] + "_converted.wav"
    audio = AudioSegment.from_file(input_path)             #audiosegment ditects the file type
    audio = audio.set_channels(1).set_frame_rate(16000)    #16khz, turns into monoaudio
    audio.export(output_path, format="wav")                #saves
    return output_path


def chunk_audio(wav_path : str , chunk_minutes : int = 10) -> list:
    audio = AudioSegment.from_wav(wav_path)   #take the wav path
    chunk_ms = chunk_minutes * 60 * 1000      #chunks works into miliseconds

    chunks = []

    for i, start in enumerate(range(0,len(audio),chunk_ms)):      #run loop over the whole audio file with a step length of 10mins (600000 ms)
        chunk = audio[start : start + chunk_ms]                   #chunck of 10mis 
        chunk_path = f"{wav_path}_chunk_{i}.wav"                  #set the
        chunk.export(chunk_path , format = "wav")

        chunks.append(chunk_path)
    
    return chunks



def process_input(source: str) -> list:
    if source.startswith("http://") or source.startswith("https://"):         #downloads from sources
        print("Detected YouTube URL. Downloading audio...")
        wav_path = download_youtube_audio(source)                             #saves it into wav path
    else:
        print("Detected local file. Converting to WAV...")
        wav_path = convert_to_wav(source)                                     #for local file convert it into wav file

    print("Chunking audio...")
    chunks = chunk_audio(wav_path)                                            #chunking the audio
    print(f"Audio ready — {len(chunks)} chunk(s) created.")
    return chunks                                                             #return chunks