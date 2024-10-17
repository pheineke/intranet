from flask import redirect, url_for, request, render_template, session, flash, blueprints

bp = blueprints.Blueprint('home', __name__)

@bp.route('/')
def index():
    USER = "admin"
    greeting_ = f"Oh hi {USER}"

    protokolle_notready_ = 0
    protokolle_ready_ = 0
    rechnungen_von_user = 0.30
    finanzanträge_offen = 0
    return render_template("home.html", 
                           greeting = greeting_,
                           protokolle_notready  =   f"Nicht bereit: {protokolle_notready_}", 
                           protokolle_ready     =   f"Bereit zur Abstimmung: {protokolle_ready_}",
                           rechnungen           =   f"{rechnungen_von_user:.2f} €",
                           finanzanträge        =   f"Offen: {finanzanträge_offen}"
                           )