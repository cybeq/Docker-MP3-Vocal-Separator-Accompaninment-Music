FROM python:3.8-slim-buster


RUN apt-get update && apt-get install -y wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
bash Miniconda3-latest-Linux-x86_64.sh -bfp /usr/local && \
rm Miniconda3-latest-Linux-x86_64.sh && \
ln -s /usr/local/bin/conda /usr/local/bin/conda.bat && \
conda config --system --prepend channels conda-forge && \
conda install -y ffmpeg libsndfile && \
conda clean -afy && \
pip install spleeter && \
pip install -U Flask
RUN pip install --upgrade click
RUN pip install --upgrade typer


WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .




CMD ["python", "app.py"]