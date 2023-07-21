from flask import Flask, render_template


app = Flask(__name__)

# Ovo predstavlja rutu u koju ulazimo

# Dodajemo neke podatke

postovi = [
    {
        "autor": "Nenad Bojanic",
        "naslov": "Blog Post 1",
        "content": "Prvi post content",
        "datum_objave": "Jul 21, 2023"
    },
    {
        "autor": "Goran Predragovic",
        "naslov": "Blog Post 2",
        "content": "Drugi post content",
        "datum_objave": "Jul 21, 2023"
    }
]


@app.route("/")
def hello():
    return render_template("layout.html", postovi=postovi, title="Pocetna Stranica")


@app.route("/about")
def about():
    return render_template("layout.html", postovi=postovi, title="About stranica")


if __name__ == "__main__":
    app.run(debug=True)
