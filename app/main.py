import socket  # Importe la bibliothèque socket pour gérer les connexions réseau


def main():
    # Affiche un message de log pour vérifier que le programme est en cours d'exécution
    print("Les logs de votre programme apparaîtront ici !")

    # Crée un socket de serveur sur "localhost" (l'ordinateur local) au port 4221
    # reuse_port=True permet de réutiliser le port si le programme est relancé
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    # Attend qu'un client se connecte au serveur
    # Cette ligne bloque l'exécution du programme jusqu'à ce qu'une connexion soit établie
    server_socket.accept()


# Vérifie si le script est exécuté directement (pas importé comme module)
if __name__ == "__main__":
    main()  # Appelle la fonction principale pour lancer le serveur
