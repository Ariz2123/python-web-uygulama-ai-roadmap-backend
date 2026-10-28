1)on hazirlak
    python
    vs code
    git
    github hesabi
    docker desktop:

2) backend repo
    ai/roadmap-backend/
        -main.py #endpoint tanimlama
        -requirements.txt
        -Dockerfile
        -.dockerignore
        -.gitignore
        -README.MD

3)Backend kodlari ve lokal calistirma
    pip install -requirements.txt
    uvicorn main:app --reload

4) Backend dockerfile ve docker ile lokalde calistirma
    docker build -t ai-roadmap-backend .
    docker run -p 8000:8000 ai-roadmap-backend
5)github push
    repo:python-web-uygulama-ai-roadmap-backend

6)Render cloud deploy






