Features:
Behavior Detection: Detect student behaviors (e.g., attentive, distracted) using the YOLO model.
Image Input and Output: Users can upload classroom photos, and the system returns annotated images.
Behavior List: Displays detected behaviors and their confidence scores.
User-Friendly Interface: Built with Gradio, providing an intuitive web-based interface.
GPU Acceleration Support: Automatically utilizes GPU acceleration if CUDA is available.

(Dataset)
roboflow : https://app.roboflow.com/student-action-detection/studentactiondetection-hidrt/1
google drive : https://drive.google.com/file/d/1Heb2N4hRcJH2s9tLdpTzacSj0APbUDdD/view

 (Tech Stack)
Deep Learning Framework: YOLO 11n(You Only Look Once)
User Interface: Gradio
Image Processing: OpenCV
Programming Language: Python, pytorch
Hardware Support: Supports GPU (CUDA) and CPU

(Requirement)
accelerate==1.7.0
aiofiles==24.1.0
annotated-types==0.7.0
anyio==4.9.0
audioop-lts==0.2.1
blinker==1.9.0
certifi==2025.4.26
charset-normalizer==3.4.2
click==8.2.1
colorama==0.4.6
coloredlogs==15.0.1
diffusers==0.33.1
fastapi==0.115.12
ffmpy==0.5.0
filelock==3.18.0
Flask==3.1.1
flatbuffers==25.2.10
fsspec==2025.5.1
gradio==5.32.0
gradio_client==1.10.2
groovy==0.1.2
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
huggingface-hub==0.32.3
humanfriendly==10.0
idna==3.10
importlib_metadata==8.7.0
itsdangerous==2.2.0
Jinja2==3.1.6
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
mpmath==1.3.0
networkx==3.5
numpy==2.2.6
onnx==1.18.0
onnxruntime-gpu==1.22.0
orjson==3.10.18
packaging==25.0
pandas==2.2.3
pillow==11.2.1
protobuf==6.31.1
psutil==7.0.0
pydantic==2.11.5
pydantic_core==2.33.2
pydub==0.25.1
Pygments==2.19.1
pyreadline3==3.5.4
python-dateutil==2.9.0.post0
python-multipart==0.0.20
pytz==2025.2
PyYAML==6.0.2
regex==2024.11.6
requests==2.32.3
rich==14.0.0
ruff==0.11.12
safehttpx==0.1.6
safetensors==0.5.3
semantic-version==2.10.0
setuptools==80.9.0
shellingham==1.5.4
six==1.17.0
sniffio==1.3.1
starlette==0.46.2
sympy==1.14.0
tokenizers==0.21.1
tomlkit==0.13.2
torch==2.7.0+cu118
torchaudio==2.7.0+cu118
torchvision==0.22.0+cu118
tqdm==4.67.1
transformers==4.52.4
typer==0.16.0
typing-inspection==0.4.1
typing_extensions==4.13.2
tzdata==2025.2
urllib3==2.4.0
uvicorn==0.34.2
websockets==15.0.1
Werkzeug==3.1.3
zipp==3.22.0

 (Usage)
Install dependencies: pip install -r requirements.txt
Run the application: python app.py
Open your browser and visit http://127.0.0.1:7860.
Upload a classroom photo and view the detection results.

 (Use Cases)
Educational institutions can use it for classroom behavior analysis to help teachers understand student attentiveness.
Useful for studying student behavior patterns to improve teaching quality.

 (Future Improvements)
Support real-time video stream detection.
Add detection for more behavior categories.
Optimize model performance for higher accuracy.


<img src="train_batch0.jpg" alt="Logo"> 
<img src="train_batch1.jpg" alt="Logo">
<img src="train_batch2.jpg" alt="Logo">
image label








best pt: https://drive.google.com/file/d/1igBMpsj1FFjAECeJf9o_-CpahUIDlD5A/view?usp=sharing
