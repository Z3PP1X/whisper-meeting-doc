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
  isRecording: boolean = false;

  constructor(private route: ActivatedRoute, private apiService: ApiService) { }

  ngOnInit(): void {
    this.sysId = this.route.snapshot.paramMap.get('sysId')!;
    console.log('Received sys_id:', this.sysId);
  }

  toggleRecording() {
    if (this.isRecording) {
      this.stopRecording();
    } else {
      this.startRecording();
    }
  }

  startRecording() {
    this.audioChunks = [];
    navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      this.mediaRecorder = new MediaRecorder(stream);
      this.mediaRecorder.start();
      this.isRecording = true;

      this.mediaRecorder.addEventListener("dataavailable", (event: any) => {
        this.audioChunks.push(event.data);
      });

      this.mediaRecorder.addEventListener("stop", () => {
        const audioBlob = new Blob(this.audioChunks, { type: 'audio/wav' });
        const audioUrl = URL.createObjectURL(audioBlob);
        const audio = new Audio(audioUrl);
        audio.play();

        this.saveAudio(audioBlob);
        this.isRecording = false;
      });
    });
  }

  stopRecording() {
    if (this.mediaRecorder && this.isRecording) {
      this.mediaRecorder.stop();
      this.isRecording = false;
    }
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

  generateRecord() {

    const formData = new FormData();
    formData.append('content', JSON.stringify({ "text": "Meeting protocol content placeholder" }));


    this.apiService.createMeetingProtocol(formData).subscribe({
      next: response => {
        console.log('Meeting protocol is being generated...', response);
      },
      error: error => {
        console.error('Error generating meeting protocol:', error);
      }
    });
  }
}
