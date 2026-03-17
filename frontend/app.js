let socket;
let recorder;

async function startStream() {

    socket = new WebSocket("ws://localhost:8000/ws/audio");

    const stream = await navigator.mediaDevices.getUserMedia({audio:true});

    recorder = new MediaRecorder(stream, {mimeType:"audio/webm"});

    recorder.ondataavailable = e => {
        if (socket.readyState === 1) {
            socket.send(e.data);
        }
    };

    recorder.start(250);

    socket.onmessage = event => {

        const data = JSON.parse(event.data);

        document.getElementById("transcription").innerText =
        "Você disse: " + data.transcription;

        document.getElementById("response").innerText =
        "Assistente: " + data.response;

        const audio = new Audio(data.voice);
        audio.play();
    };
}

function stopStream(){
    recorder.stop();
    socket.close();
}