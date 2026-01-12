"""Mon API FastAPI de démonstration.

Ce module expose une API simple servant de support pédagogique
pour montrer l'intégration FastAPI + Sphinx (autodoc).
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="API Tutoriel Sphinx",
    description="Une API simple pour démontrer la documentation automatique.",
    version="1.0.0",
)


class MaClasse(BaseModel):
    """Modèle de données principal.

    Représente un message texte envoyé à l'API.
    """

    text: str = Field(..., example="Bonjour Sphinx")


@app.get("/", summary="Endpoint racine")
def root():
    """Endpoint principal de l'API.

    Returns
    -------
    dict
        Message de bienvenue.
    """
    return {"message": "Hello World"}


@app.post("/echo", response_model=MaClasse, summary="Renvoyer le texte")
def echo(data: MaClasse):
    """Retourne le texte envoyé par l'utilisateur.

    Parameters
    ----------
    data : MaClasse
        Objet contenant le texte à renvoyer.

    Returns
    -------
    MaClasse
        Le même texte que celui reçu.
    """
    return data


@app.get("/health", summary="Vérification de l'état de l'API")
def healthcheck():
    """Indique si l'API est fonctionnelle.

    Returns
    -------
    dict
        Statut de l'API.
    """
    return {"status": "ok"}