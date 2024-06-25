import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AudioRecorderComponent } from './audio-recorder/audio-recorder.component';
import { RegisterMeetingComponent } from './register-meeting/register-meeting.component';
import { provideHttpClient, withInterceptorsFromDi } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, AudioRecorderComponent, RegisterMeetingComponent],
  providers: [],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'bi_frontend';
}
