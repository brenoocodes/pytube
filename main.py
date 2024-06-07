import os
import customtkinter as ctk
from pytube import Playlist, YouTube
from tkinter import messagebox

def select_folder():
    folder = ctk.filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

def download_videos():
    playlist_url = url_entry.get()
    save_path = folder_path.get()

    if not playlist_url or not save_path:
        messagebox.showerror("Erro", "URL da playlist e pasta de destino são obrigatórios")
        return

    error_videos = []

    try:
        playlist = Playlist(playlist_url)
        video_count = len(playlist.video_urls)
        
        confirm = messagebox.askyesno("Confirmar Download", f"A playlist contém {video_count} vídeos. Deseja continuar?")
        
        if confirm:
            for i, video_url in enumerate(playlist.video_urls, start=1):
                try:
                    yt = YouTube(video_url)
                    stream = yt.streams.filter(only_audio=True).first()

                   
                    title = yt.title.replace("/", " ").replace("\\", " ").replace(":", " ").replace("*", " ").replace("?", " ").replace("\"", " ").replace("<", " ").replace(">", " ").replace("|", " ")
                    author = yt.author.replace("/", " ").replace("\\", " ").replace(":", " ").replace("*", " ").replace("?", " ").replace("\"", " ").replace("<", " ").replace(">", " ").replace("|", " ")

                    nome_video = f"{title} - {author}"
                    
                    downloaded_file = stream.download(output_path=save_path, filename=nome_video)
                    
                    base, ext = os.path.splitext(downloaded_file)
                    mp3_file = base + '.mp3'
                    
                    if os.path.exists(mp3_file):
                        os.remove(mp3_file)
                    os.rename(downloaded_file, mp3_file)
                    
                    # Atualiza a interface
                    status_label.configure(text=f"Baixando: {i}/{video_count}")
                    last_download_label.configure(text=f"Última vídeo: {title}")
                    app.update()
                except Exception as e:
                    error_videos.append(yt.title)
                    print(f"Erro ao baixar {yt.title}: {e}")

            if error_videos:
                messagebox.showinfo("Erro", f"Alguns vídeos não puderam ser baixados devido a restrições de privacidade ou idade:\n{', '.join(error_videos)}")
            else:
                messagebox.showinfo("Sucesso", f"Download concluído! {video_count} vídeos baixados como MP3.")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao baixar a playlist: {e}")

# Inicializa o CustomTkinter
ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Downloader de Playlists do YouTube")
app.geometry("800x450") 

url_label = ctk.CTkLabel(app, text="URL da Playlist do YouTube:")
url_label.pack(pady=10, padx=10)

url_entry = ctk.CTkEntry(app, width=400)
url_entry.pack(pady=10, padx=10)

folder_path = ctk.StringVar()
folder_button = ctk.CTkButton(app, text="Selecionar Pasta", command=select_folder)
folder_button.pack(pady=10, padx=10)

folder_label = ctk.CTkLabel(app, textvariable=folder_path)
folder_label.pack(pady=10, padx=10)

download_button = ctk.CTkButton(app, text="Baixar Vídeos", command=download_videos)
download_button.pack(pady=10, padx=10)

status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=10, padx=10)

last_download_label = ctk.CTkLabel(app, text="")
last_download_label.pack(pady=10, padx=10)

app.mainloop()
