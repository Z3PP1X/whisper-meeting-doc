import { Routes } from '@angular/router';
import { RegisterMeetingComponent } from './register-meeting/register-meeting.component';
import { AudioRecorderComponent } from './audio-recorder/audio-recorder.component';
import { MeetingProtocolComponent } from './meeting-protocol/meeting-protocol.component';


export const routes: Routes = [
    {path: '', component: RegisterMeetingComponent},
    {path: 'audio-recorder/:sysId', component: AudioRecorderComponent},
    {path: 'meeting-protocol/:id', component: MeetingProtocolComponent}
];
