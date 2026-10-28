from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()


ROADMAPS={
    "yapay_zeka":[
        "Python Temelleri",
        "Veri Analizi",
        "Makine Ogrenmesi",
        "Model Degerlendirme",
        "Mini Projeler"
    ],
    "derin_ogrenme":[
        "Python ve Numpy",
        "Yapay sinir Aglari",
        "CNN",
        "RNN ve LSTM",
        "Derin Ogrenme Projeleri"
    ],
    "nlp": [
    "Metin Ön İşleme",
    "Word Embedding",
    "RNN ve LSTM ile NLP",
    "Transformer",
    "RAG ve Chatbot Projeleri"
    ]
}

class RoadmapRequest(BaseModel):
    alan:str

@app.get("/")
def home():
    return{
        "message":"Backend Calisiyor"
    }

@app.post("/roadmap")
def get_roadmap(data:RoadmapRequest):
    secim =data.alan.lower()

    if secim not in ROADMAPS:
        return {
            "error":"gecersiz secim "
        }

    return{
        "alan":secim,
        "adimlar":ROADMAPS[secim]
    }





















