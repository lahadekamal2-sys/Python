seconde_saisie = int(input("Saisissez les secondes : "))

# Conversions en secondes
SEC_PAR_MIN = 60
SEC_PAR_HEURE = 3600
SEC_PAR_JOUR = 86400
SEC_PAR_MOIS = 2592000
SEC_PAR_AN = 31536000

# 1. Années
annees = seconde_saisie // SEC_PAR_AN
reste = seconde_saisie % SEC_PAR_AN

# 2. Mois
mois = reste // SEC_PAR_MOIS
reste = reste % SEC_PAR_MOIS

# 3. Jours
jours = reste // SEC_PAR_JOUR
reste = reste % SEC_PAR_JOUR

# 4. Heures
heures = reste // SEC_PAR_HEURE
reste = reste % SEC_PAR_HEURE

# 5. Minutes
minutes = reste // SEC_PAR_MIN

# 6. Secondes restantes
secondes = reste % SEC_PAR_MIN

# Affichage propre avec f-string
print(f"{annees} ans, {mois} mois, {jours} jours, {heures} h, {minutes} min, {secondes} s")


