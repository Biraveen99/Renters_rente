from flask import Flask, render_template, request

app = Flask(__name__)

#startsiden
@app.route("/", methods=["GET", "POST"])
def kalkulator():
    if request.method == "POST":
        # Hent verdier fra siden vår. Basert på en fast formel
        initial_belop = float(request.form["initial_belop"])
        manedlig_bidrag = float(request.form["manedlig_bidrag"])
        tids_horisont = float(request.form["tids_horisont"])
        arlig_rente = float(request.form["arlig_rente"]) / 100
        n = 12  # Månedlig sammensetning

        # Beregn renters rente
        sluttbelop = initial_belop * (1 + arlig_rente / n) ** (n * tids_horisont)
        sluttbelop += manedlig_bidrag * (((1 + arlig_rente / n) ** (n * tids_horisont) - 1) / (arlig_rente / n))

        # Totalt beløp selv satt inn
        totalt_innsatt = initial_belop + (manedlig_bidrag * 12 * tids_horisont)

        # Gevinst
        gevinst = sluttbelop - totalt_innsatt

        return render_template("index.html", resultat=True, sluttbelop=sluttbelop, totalt_innsatt=totalt_innsatt, gevinst=gevinst)

    return render_template("index.html", resultat=False)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

