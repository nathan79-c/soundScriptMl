import os
import pandas as pd
import random

def list_files(directory):
    files_info = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.abspath(os.path.join(root, file))
            files_info.append({"path": file_path, "name": file})
    return files_info

def generate_random_equipment():
    equipments = ['Samsung A20e', 'Dell Latitude']
    return random.choice(equipments)

def update_excel_with_files_info(excel_file, files_info):
    # Lire le fichier Excel
    df = pd.read_excel(excel_file)

    # Récupérer le dernier identifiant dans la colonne "identifiant"
    last_id = df['identifiant'].max() if not df.empty else 0

    # Récupérer les nouveaux chemins absolus des fichiers
    new_emplacements = [f"Path: {file_info['path']}" for file_info in files_info]

    # Incrémenter automatiquement les identifiants
    new_ids = list(range(last_id + 1, last_id + 1 + len(files_info)))

    # Générer aléatoirement les équipements
    new_equipments = [generate_random_equipment() for _ in range(len(files_info))]

    # Ajouter les nouvelles informations au DataFrame
    new_data = {
        'identifiant': new_ids,
        'emplacement': new_emplacements,
        'equipement': new_equipments
    }

    new_df = pd.DataFrame(new_data)

    # Ajouter les nouvelles données au DataFrame existant
    df = pd.concat([df, new_df], ignore_index=True)

    # Écrire le DataFrame mis à jour dans le fichier Excel
    df.to_excel(excel_file, index=False)

    print(f"Le fichier Excel a été mis à jour avec les informations sur les fichiers.")

if __name__ == "__main__":
    directory = input("Entrez le chemin du dossier à parcourir : ")

    # Récupérer les informations sur les fichiers
    files_info = list_files(directory)

    # Lire le fichier Excel et mettre à jour avec les informations sur les fichiers
    excel_file = input("Entrez le chemin du fichier Excel : ")
    update_excel_with_files_info(excel_file, files_info)
