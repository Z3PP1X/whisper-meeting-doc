import { Routes } from '@angular/router';
import { RegisterMeetingComponent } from './register-meeting/register-meeting.component';
import { AudioRecorderComponent } from './audio-recorder/audio-recorder.component';


export const routes: Routes = [
    {path: '', component: RegisterMeetingComponent},
    {path: 'audio-recorder/:sysId', component: AudioRecorderComponent}
];
