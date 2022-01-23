### Setup

### NOTE: THE REAL-TIME VOICE CLONING ALGORITHM IS NOT MADE BY US BUT BY https://github.com/CorentinJ. THE PROJECT IS MEANT TO BE A FUN LITTLE PRANK WITH FRIENDS BY MIMICKING THERE VOICE IN A VOICE CHAT.

### 1. Install Requirements

**Python 3.6 or 3.7** is needed to run the toolbox.

* Install [PyTorch](https://pytorch.org/get-started/locally/) (>=1.0.1).
* Install [ffmpeg](https://ffmpeg.org/download.html#get-packages).
* Run the following to install remaining packages:
    `pip install -r requirements.txt`
    `cmd < install.txt` (for Windows machines)

### 2. Download Pretrained Models
Download the latest [here](https://github.com/CorentinJ/Real-Time-Voice-Cloning/wiki/Pretrained-models).

### 3. (Optional) Test Configuration
Before you download any dataset, you can begin by testing your configuration with:

`python demo_cli.py`

If all tests pass, you're good to go.

### 4. Launch the Toolbox
Launch the program with the following command:

`python demo_toolbox.py --no_mp3_support`  

depending on whether you downloaded any datasets. If you are running an X-server or if you have the error `Aborted (core dumped)`, see [this issue](https://github.com/CorentinJ/Real-Time-Voice-Cloning/issues/11#issuecomment-504733590).

### 5. Additional Programs

To create samples from Discord, we recommend using Craig.chat (https://craig.chat/home/)
From downloading recordings through Craig, you can select WAV files to use as datasets for vocoding.

The user should use VoiceMeeter (VoiceMeeter Tutorial.pdf found in program files) in order to connect Mimicu to other programs to which the user would like to feed audio. VoiceMeeter serves as a Virtual Audio Device which other programs can use as an input device.
