from flask import Flask, render_template, redirect, request, url_for, abort, flash,session
app = Flask(__name__)

taches = [
{"id": 1, "titre": "Réviser les décorateurs",
"priorite": "haute", "terminee": False},
{"id": 2, "titre": "Installer Flask",
"priorite": "normale", "terminee": True},
{"id": 3, "titre": "Lire la doc Jinja2",
"priorite": "basse", "terminee": False},
{"id": 4, "titre": "<b>Important</b>", "priorite": "haute", "terminee": False}
]

app.secret_key = "ff08421a3d051a261e88bafef84d310fe40451acd18812bf7e42ef354bb4f480"

# Acceuil
@app.route('/')
def index():
    filtre = request.args.get("filtre")
    if filtre is None:
        filtre = session.get("filtre", "toutes")
    session["filtre"]=filtre
    if filtre == "actives":
        taches_filtrees = [t for t in taches if not t["terminee"]]
    elif filtre == "terminees":
        taches_filtrees = [t for t in taches if t["terminee"]]
    else:
        taches_filtrees = taches
    return render_template("taches.html", taches=taches_filtrees, filtre_actif=filtre)

# tache par id
@app.route('/taches/<int:id>')
def tache(id):
    for t in taches:
        if t['id']==id:
            return t['titre']
    return abort(404)

# Ajout de nouveau tache
@app.route("/taches/ajouter", methods=["GET", "POST"])
def ajouter():
    if request.method == "POST":
        titre = request.form.get("titre", "").strip()
        priorite = request.form.get("priorite", "normale")
        nouvel_id = max((t["id"] for t in taches), default=0) + 1
        erreurs = []
        if not titre:
            erreurs.append("Le titre est obligatoire.")
        elif len(titre) > 80:
            erreurs.append("Le titre ne doit pas dépasser 80 caractères.")
        if priorite not in ('basse', 'normale', 'haute'):
           erreurs.append("Priorité invalide.")
        if erreurs:
            return render_template('ajouter.html', erreurs=erreurs, titre=titre, priorite=priorite)
        taches.append({"id": nouvel_id, "titre": titre, "priorite": priorite, "terminee": False})
        flash("Tache ajoutee")
        return redirect(url_for("index"))
    return render_template("ajouter.html")

# tache terminer
@app.post('/taches/<int:id>/terminer')
def terminer(id):
    for t in taches:
        if t["id"]== id:
            t["terminee"]=True
            flash("Tache a jours")
    return redirect(url_for("index", filtre=session.get("filtre", "toutes")))

# supprimer tache
@app.post('/taches/<int:id>/supprimer')
def supprimer(id):
    i= None
    for ix, t in enumerate(taches):
        if t["id"]==id:
            i = ix
    if i is not None:
        del taches[i]
        flash("Suppression OK")
    else :
        flash("erreur")
    return redirect(url_for("index", filtre=session.get("filtre", "toutes")))

# 404 perso
@app.errorhandler(404)
def pageKO(e):
    return render_template("404.html"), 404 # pour envoyer 404 au lieu de 200

# api/tache
@app.route('/api/taches')
def api_taches():
    return taches
