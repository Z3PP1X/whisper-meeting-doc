import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-meeting-protocol',
  templateUrl: './meeting-protocol.component.html',
  styleUrls: ['./meeting-protocol.component.css']
})
export class MeetingProtocolComponent implements OnInit {
  id: number = 0;
  meetingProtocolHtml: string = '';

  constructor(private route: ActivatedRoute, private apiService: ApiService) { }

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    this.fetchGeneratedProtocol(this.id);
  }

  fetchGeneratedProtocol(id: number) {
    this.apiService.getMeetingProtocolById(id).subscribe({
      next: response => {
        console.log('Meeting protocol fetched:', response);
        this.meetingProtocolHtml = response.content.html;
      },
      error: error => {
        console.error('Error fetching meeting protocol:', error);
      }
    });
  }
}
