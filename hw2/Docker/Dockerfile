FROM ubuntu:latest

ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    texlive \
    texlive-latex-extra \
    texlive-fonts-recommended \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/
RUN pip3 install -i https://test.pypi.org/simple/ --no-cache-dir -r /tmp/requirements.txt

WORKDIR /usr/src/app
COPY . .

# Generate PDF
CMD ["python3", "generate_pdf.py"]

