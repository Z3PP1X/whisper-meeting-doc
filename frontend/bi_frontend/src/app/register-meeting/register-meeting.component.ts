import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register-meeting',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  providers: [ApiService],
  templateUrl: './register-meeting.component.html',
  styleUrls: ['./register-meeting.component.css']
})
export class RegisterMeetingComponent {

  meetingForm: FormGroup;

  constructor(private fb: FormBuilder, private apiService: ApiService, private router: Router) {
    this.meetingForm = this.fb.group({
      attendees: ['', Validators.required],
      meeting_date: ['', Validators.required],
      meeting_topic: ['', Validators.required],
      meeting_start_time: ['', Validators.required],
      meeting_end_time: ['', Validators.required],
      duration: ['']
    });
  }

  calculateDuration(startTime: string, endTime: string): string {
    const start = new Date(startTime).getTime();
    const end = new Date(endTime).getTime();
    const duration = end - start;
    const hours = Math.floor(duration / 3600000);
    const minutes = Math.floor((duration % 3600000) / 60000);
    return `PT${hours}H${minutes}M`;
  }

  onSubmit() {
      if (this.meetingForm.valid) {
        const formValue = this.meetingForm.value;
        const duration = this.calculateDuration(formValue.meeting_start_time, formValue.meeting_end_time);
        console.log("Form is valid. Creating Meeting Call...")
  
        const meetingCallPayload = {
          attendees: formValue.attendees.split(',').map((email: string) => email.trim()),
          meeting_date: formValue.meeting_date,
          meeting_topic: formValue.meeting_topic,
          meeting_start_time: formValue.meeting_start_time,
          meeting_end_time: formValue.meeting_end_time,
          duration: duration
        };
  
        this.apiService.createMeetingCall(meetingCallPayload).subscribe({
          next: (response) => {
            console.log('Meeting Call created:', response);
            const sysId = response.sys_id;
            console.log('Meeting Call sys_id:', sysId);
            this.router.navigate(['/audio-recorder', sysId]);
          },
          error: (error) => {
            console.error('Error creating Meeting Call:', error);
          }
        });
      }
    }
  }
