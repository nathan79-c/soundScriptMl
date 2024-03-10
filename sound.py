from pydub import AudioSegment
from pydub.utils import make_chunks
import os

def split_audio(input_file, output_folder):
    # Chargement du fichier audio
    audio = AudioSegment.from_mp3(input_file)

    # Durée d'un segment (4 secondes)
    segment_length_ms = 4000

    # Création du dossier de sortie s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Découpe de l'audio en segments de 4 secondes
    chunks = make_chunks(audio, segment_length_ms)

    # Sauvegarde des segments
    for i, chunk in enumerate(chunks):
        chunk_name = os.path.join(output_folder, f"segment_{i+1}.wav")
        chunk.export(chunk_name, format="wav")

    print(f"{len(chunks)} segments créés avec succès.")

# Appel de la fonction avec le fichier audio en paramètre
input_audio_file = "chemin/vers/votre/audio.mp3"
output_folder = "chemin/vers/dossier/sortie"
split_audio(input_audio_file, output_folder)


