"""Fonctions utilitaires d'OptiGestion."""

from optigestion.utils.helpers import (
    formater_monnaie,
    formater_pourcentage,
    valider_nombre_positif,
)

__all__ = [
    "formater_monnaie",
    "formater_pourcentage",
    "valider_nombre_positif",
]
"""Modules fonctionnels d'OptiGestion."""

from optigestion.modules.input_module import importer_csv, exporter_csv, importer_json, exporter_json
from optigestion.modules.costing_module import calculer_cout_revient, calculer_marge_brute, calculer_taux_marge
from optigestion.modules.analysis_module import calculer_seuil_rentabilite, simuler_scenario, analyser_sensibilite
from optigestion.modules.storage_module import charger_donnees, sauvegarder_donnees

__all__ = [
    "importer_csv",
    "exporter_csv",
    "importer_json",
    "exporter_json",
    "calculer_cout_revient",
    "calculer_marge_brute",
    "calculer_taux_marge",
    "calculer_seuil_rentabilite",
    "simuler_scenario",
    "analyser_sensibilite",
    "charger_donnees",
    "sauvegarder_donnees",
]

