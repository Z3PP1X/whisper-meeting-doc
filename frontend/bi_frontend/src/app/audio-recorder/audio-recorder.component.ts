import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-audio-recorder',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './audio-recorder.component.html',
  styleUrls: ['./audio-recorder.component.css']
})
export class AudioRecorderComponent implements OnInit {
  private mediaRecorder: any;
  private audioChunks: any[] = [];
  sysId: string = '';

  constructor(private route: ActivatedRoute, private apiService: ApiService) { }

  ngOnInit(): void {
    this.sysId = this.route.snapshot.paramMap.get('sysId')!;
    console.log('Received sys_id:', this.sysId);
  }

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
    const formData = new FormData();
    formData.append('payload', blob, 'audio.wav');
    formData.append('timestamp', JSON.stringify({ start: new Date().toISOString() }));
    formData.append('call_id', 'example-call-id');  
    formData.append('caller_id', 'example-caller-id');
    formData.append('transcription', 'Auto-generated transcription placeholder');


    this.apiService.createCallRecord(formData).subscribe({
      next: response => {
        console.log('Call record created:', response);
      },
      error: error => {
        console.error('Error creating call record:', error);
      }
    });
  }
}
