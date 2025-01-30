import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Fonction pour afficher le texte d'accueil
def show_accueil():
    content_label.config(text="Bienvenue dans l'application BTS SIO !\n\nLe BTS SIO (Services Informatiques aux Organisations) forme des techniciens spécialisés dans les systèmes informatiques. Deux options sont disponibles : SISR (réseaux et infrastructures) et SLAM (développement logiciel).")
    content_label.config(fg="#4CAF50", font=('Helvetica', 11))  # Texte plus petit pour accueil
    reset_quizz()  # Réinitialiser le quizz lorsqu'on revient à l'accueil
    content_label.pack(pady=40)  # Réafficher le texte d'accueil
    question_frame.pack_forget()  # Masquer le quizz
    result_label.pack_forget()  # Masquer le résultat du quizz
    nav_frame.pack(fill="x", pady=10)  # Afficher la barre de navigation

# Fonction pour l'option SISR
def show_sisr():
    content_label.config(text="**Option SISR (Solutions d'Infrastructure, Systèmes et Réseaux)**\n\nCette option se concentre sur l'infrastructure informatique, la gestion des réseaux et la sécurité des systèmes. Les étudiants formés dans cette spécialité acquièrent des compétences techniques pour maintenir, configurer et sécuriser des infrastructures informatiques complexes.\n\nLes domaines d'études incluent :\n- Administration des systèmes et des réseaux\n- Sécurité des systèmes d'information\n- Virtualisation\n- Gestion des bases de données\n- Cloud Computing\n\n**Métiers possibles :**\n- Technicien de maintenance informatique\n- Administrateur réseaux et systèmes\n- Ingénieur en sécurité informatique\n- Consultant en infrastructures IT")
    content_label.config(fg="#1976D2", font=('Helvetica', 11))  # Texte plus petit pour SISR
    reset_quizz()  # Réinitialiser le quizz lorsqu'on revient à l'option SISR
    content_label.pack(pady=40)  # Réafficher le texte
    question_frame.pack_forget()  # Masquer le quizz
    result_label.pack_forget()  # Masquer le résultat du quizz

# Fonction pour l'option SLAM
def show_slam():
    content_label.config(text="**Option SLAM (Solutions Logicielles et Applications Métiers)**\n\nCette option se concentre sur le développement d'applications et la gestion des logiciels au sein des organisations. Les étudiants y apprennent à concevoir et à développer des applications adaptées aux besoins spécifiques des entreprises, ainsi qu’à maintenir et mettre à jour des logiciels.\n\nLes domaines d'études incluent :\n- Développement d'applications (Java, Python, C#)\n- Conception de bases de données\n- Applications mobiles (Android, iOS)\n- Web et technologies front-end/back-end\n- Méthodes agiles de gestion de projet\n- Développement d'outils métiers\n\n**Métiers possibles :**\n- Développeur d'applications (web, mobile, logiciel)\n- Analyste programmeur\n- Chef de projet informatique\n- Développeur full-stack\n- Ingénieur d'études et développement")
    content_label.config(fg="#009688", font=('Helvetica', 11))  # Texte plus petit pour SLAM
    reset_quizz()  # Réinitialiser le quizz lorsqu'on revient à l'option SLAM
    content_label.pack(pady=40)  # Réafficher le texte
    question_frame.pack_forget()  # Masquer le quizz
    result_label.pack_forget()  # Masquer le résultat du quizz

# Fonction pour démarrer le quizz dans la même fenêtre
def start_quizz():
    global question_index, score
    question_index = 0
    score = 0
    content_label.pack_forget()  # Masquer le texte d'accueil quand le quizz commence
    show_question()  # Afficher la première question
    question_frame.pack(pady=20)  # Afficher le frame du quizz
    nav_frame.pack_forget()  # Masquer la barre de navigation

# Réinitialiser le quizz
def reset_quizz():
    for button in answer_buttons:
        button.pack_forget()  # Retirer les boutons de réponse s'ils sont affichés
    question_label.config(text="")  # Retirer la question
    result_label.pack_forget()  # Masquer le résultat du quizz
    content_label.pack(pady=40)  # Réafficher le texte d'accueil
    question_frame.pack_forget()  # Masquer le quizz
    nav_frame.pack(fill="x", pady=10)  # Afficher la barre de navigation

# Afficher une question
def show_question():
    global question_index
    if question_index < len(questions):
        q, options = questions[question_index]
        question_label.config(text=q)
        for i, option in enumerate(options):
            answer_buttons[i].config(text=option, command=lambda answer=option: check_answer(answer))
            answer_buttons[i].pack(fill='x', pady=5)
    else:
        result_label.config(text=f"Vous avez obtenu un score de {score}/{len(questions)}")
        result_label.pack(pady=20)  # Afficher le résultat du quizz
        question_frame.pack_forget()  # Masquer le quizz
        add_return_button()  # Ajouter le bouton "Retour à l'accueil"

# Ajouter le bouton "Retour à l'accueil" après le résultat
def add_return_button():
    global return_button
    return_button = tk.Button(content_frame, text="Retour à l'accueil", font=('Helvetica', 12), command=remove_return_button, width=20, bg="#D32F2F", fg="white", relief="flat")
    return_button.pack(pady=20)

# Supprimer le bouton "Retour à l'accueil" après qu'il a été cliqué
def remove_return_button():
    return_button.pack_forget()  # Enlever le bouton de l'écran
    show_accueil()  # Retourner à l'accueil

# Vérifier la réponse et passer à la question suivante
def check_answer(answer):
    global score, question_index
    correct_answers = [
        "Former des techniciens en informatique", 
        "SISR", 
        "Python", 
        "Gérer les infrastructures réseaux et serveurs", 
        "Connaissance des systèmes d'exploitation mobiles", 
        "JavaScript", 
        "Une base de données qui utilise des tables pour organiser les données", 
        "Analyser les besoins des utilisateurs et développer des solutions", 
        "Une pratique où le code est fréquemment intégré dans une branche principale", 
        "Git", 
        "Créer des machines virtuelles pour simuler plusieurs systèmes sur un seul matériel", 
        "SQL est basé sur des tables tandis que NoSQL utilise des documents ou des clés-valeurs", 
        "Un réseau privé virtuel qui sécurise la connexion à Internet"
    ]
    if answer == correct_answers[question_index]:
        score += 1
    question_index += 1
    show_question()

# Fenêtre principale
window = tk.Tk()
window.title("BTS SIO Informations")

# Modifier la taille de la fenêtre pour la rendre plus longue
window.geometry("400x800")  # Augmenter la hauteur de la fenêtre

# Charger l'image de fond depuis le même dossier
bg_image = Image.open("background.jpg")  # Assure-toi que l'image est bien dans le même dossier
bg_image = bg_image.resize((360, 800), Image.Resampling.LANCZOS)  # Redimensionner l'image pour qu'elle s'adapte
bg_photo = ImageTk.PhotoImage(bg_image)

# Créer un canvas avec un scrollbar pour permettre le défilement
canvas = tk.Canvas(window, width=360, height=800)  # Augmenter la hauteur du canvas
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.config(yscrollcommand=scrollbar.set)

# Créer un frame qui contiendra tout le contenu
content_frame = tk.Frame(canvas, bg="white")

# Ajouter le frame au canvas
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Appliquer l'image de fond sur le canvas
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Label d'affichage du contenu avec un style moderne et centré
content_label = tk.Label(content_frame, text="Chargement...", font=('Helvetica', 11, "bold"), wraplength=300, justify='center', bg="white", fg="#4CAF50")
content_label.pack(pady=40)

# Créer une barre de navigation sans fond vert derrière les boutons
nav_frame = tk.Frame(content_frame, bg="white")
nav_frame.pack(fill="x", pady=10)

button_sisr = tk.Button(nav_frame, text="Option SISR", font=('Helvetica', 12), command=show_sisr, width=20, bg="#1976D2", fg="white", relief="flat")
button_sisr.pack(side="top", padx=5, pady=5)

button_slam = tk.Button(nav_frame, text="Option SLAM", font=('Helvetica', 12), command=show_slam, width=20, bg="#009688", fg="white", relief="flat")
button_slam.pack(side="top", padx=5, pady=5)

button_quizz = tk.Button(nav_frame, text="Lancer le Quizz", font=('Helvetica', 12), command=start_quizz, width=20, bg="#0288D1", fg="white", relief="flat")
button_quizz.pack(side="top", padx=5, pady=5)

# Questions du quizz
questions = [
    ("Quel est le but principal du BTS SIO ?", ["Former des techniciens en informatique", "Former des développeurs web", "Former des gestionnaires de projet"]),
    ("Quelle est l'option qui concerne la gestion des réseaux ?", ["SISR", "SLAM", "Aucun"]),
    ("Quel langage est principalement utilisé dans l'option SLAM ?", ["Python", "HTML", "Excel"]),
    ("Quel est le rôle principal d'un administrateur systèmes et réseaux ?", ["Gérer les infrastructures réseaux et serveurs", "Développer des applications", "Former des utilisateurs"]),
    ("Quelles compétences sont nécessaires pour un développeur mobile ?", ["Connaissance des systèmes d'exploitation mobiles", "Connaissance des réseaux", "Savoir gérer des bases de données"]),
    ("Quel est le langage de programmation utilisé pour développer des applications web front-end ?", ["JavaScript", "Python", "C#"]),
    ("Qu'est-ce qu'une base de données relationnelle ?", ["Une base de données qui utilise des tables pour organiser les données", "Un fichier simple qui contient des informations", "Une base de données dans le cloud"]),
    ("Quel est le rôle d'un analyste programmeur ?", ["Analyser les besoins des utilisateurs et développer des solutions", "Former les employés à l'informatique", "Gérer les bases de données"]),
    ("Qu'est-ce que l'intégration continue en développement logiciel ?", ["Une pratique où le code est fréquemment intégré dans une branche principale", "Une étape de déploiement d'un logiciel", "Une forme de testing manuel"]),
    ("Quel est l'outil le plus couramment utilisé pour la gestion de version de code source ?", ["Git", "Jenkins", "Docker"]),
    ("En quoi consiste la virtualisation dans l'informatique ?", ["Créer des machines virtuelles pour simuler plusieurs systèmes sur un seul matériel", "Sécuriser les serveurs", "Créer des copies de sauvegarde d'un système"]),
    ("Quelle est la différence entre le SQL et le NoSQL ?", ["SQL est basé sur des tables tandis que NoSQL utilise des documents ou des clés-valeurs", "SQL est plus lent que NoSQL", "SQL est plus adapté aux applications mobiles"]),
    ("Qu'est-ce qu'un VPN et à quoi sert-il ?", ["Un réseau privé virtuel qui sécurise la connexion à Internet", "Un logiciel de gestion des serveurs", "Un protocole pour accéder aux réseaux locaux"]),
]

# Initialisation du score et de l'index de la question
score = 0
question_index = 0

# Frame et boutons pour le quizz
question_frame = tk.Frame(content_frame, bg="white")
question_label = tk.Label(question_frame, text="", font=('Arial', 10), wraplength=300, fg="#616161", bg="white")
question_label.pack(pady=10)

answer_buttons = []
for _ in range(3):
    button = tk.Button(question_frame, font=('Arial', 10), height=2, bg="#E3F2FD", fg="black")
    answer_buttons.append(button)

# Label pour afficher le résultat du quizz
result_label = tk.Label(content_frame, text="", font=('Helvetica', 14), fg="black", bg="white")

# Démarrer l'application
window.mainloop()
