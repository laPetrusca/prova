from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def homepage():
    return "Ciao, questa è l'homepage della tua IA!"

@app.get("/ciao")
def ciao():
    return "sono nel path ciao"

@app.get("/world")
def hello():
    return "Hello, World!"

@app.get("/lingua")
def stampa(testo):
    from langdetect import detect

    #testo = "Ciao, sto parlando in italiano"
    lingua = detect(testo)

    print(f"La lingua rilevata è: {lingua}")
    
    return f"La lingua rilevata è: {lingua}"




