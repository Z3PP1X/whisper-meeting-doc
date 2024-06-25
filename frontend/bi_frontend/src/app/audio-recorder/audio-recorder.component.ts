import { Component } from '@angular/core';

@Component({
  selector: 'app-audio-recorder',
  standalone: true,
  imports: [],
  templateUrl: './audio-recorder.component.html',
  styleUrl: './audio-recorder.component.css'
})
export class AudioRecorderComponent {

  private mediaRecorder: any; 
  private audioChunks: any = [] = [];

  startRecording() {

    navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      this.mediaRecorder = new MediaRecorder(stream);
      this.mediaRecorder.start();

      this.mediaRecorder.addEventListener("dataavailable", (event: any) => {
        this.audioChunks.push(event.data);
      });

      this.mediaRecorder.addEventListener("stop", () => {
        const audioBlob = new Blob(this.audioChunks, { type: 'audio/wav' });
        const audioUrl = URL.createObjectURL(audioBlob);
        const audio = new Audio(audioUrl);
        audio.play();

        this.saveAudio(audioBlob);
      });
    });
  }
stopRecording() {
  this.mediaRecorder.stop();
}

saveAudio(blob: Blob) {
  const a = document.createElement('a');
  const url = URL.createObjectURL(blob);
  a.href = url;
  a.download = 'audio.wav';
  a.click();
  URL.revokeObjectURL(url);
}
}
