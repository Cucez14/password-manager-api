# Použijeme oficiálny Python image
FROM python:3.11-slim

# Nastavíme pracovný adresár v kontajneri
WORKDIR /app

# Skopírujeme súbory projektu
COPY . .

# Nainštalujeme Python knižnice
RUN pip install --no-cache-dir -r requirements.txt

# Otvoríme port (pre lokálny beh)
EXPOSE 8000

# Príkaz na spustenie API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
 
