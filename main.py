import yt_dlp as youtube_dl
from moviepy import VideoFileClip, AudioFileClip
import os

def download_video_and_audio(link: str, output_path: str):
    video_file = f"{output_path}video.mp4"
    audio_file = f"{output_path}audio.mp3"

    # Configuração para baixar apenas o vídeo
    video_opts = {
        'outtmpl': video_file,
        'format': 'bestvideo',
    }

    # Configuração para baixar apenas o áudio
    audio_opts = {
        'outtmpl': audio_file,
        'format': 'bestaudio',
    }

    # Baixar vídeo
    try:
        with youtube_dl.YoutubeDL(video_opts) as ydl:
            ydl.download([link])
        print("Vídeo baixado com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar vídeo: {e}")

    # Baixar áudio
    try:
        with youtube_dl.YoutubeDL(audio_opts) as ydl:
            ydl.download([link])
        print("Áudio baixado com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar áudio: {e}")

    return video_file, audio_file

def combine_video_and_audio(video_file: str, audio_file: str, output_file: str):
    try:
        video_clip = VideoFileClip(video_file)
        audio_clip = AudioFileClip(audio_file)

        # Ajuste o áudio para o vídeo
        video_clip.audio = audio_clip

        # Salve o arquivo combinado
        video_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

        print(f"Vídeo final salvo em {output_file}")
    except Exception as e:
        print(f"Erro ao combinar vídeo e áudio: {e}")

def remove_extra_files(video_file: str, audio_file: str):
    try:
        os.remove(video_file)
        os.remove(audio_file)
    except Exception as e:
        print(f"Erro ao remover arquivos extras: {e}")

def main():
    link = input("Digite o link do vídeo: ").strip()
    output_path = input("Digite o caminho para salvar (d/D para Downloads): ").strip()

    if output_path == "d" or output_path == "D":
        output_path = "C:/Downloads/"

    video_file, audio_file = download_video_and_audio(link, output_path)

    output_file = f"{output_path}video_final.mp4"
    combine_video_and_audio(video_file, audio_file, output_file)
    remove_extra_files(video_file, audio_file)

if __name__ == "__main__":
    main()
