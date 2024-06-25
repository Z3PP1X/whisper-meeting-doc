import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiURL = environment.apiUrl;

  constructor(private http: HttpClient) { }

  // MeetingCall endpoints
  getMeetingCalls(): Observable<any> {
    return this.http.get(`${this.apiURL}meetingcall/`);
  }

  createMeetingCall(data: any): Observable<any> {
    return this.http.post(`${this.apiURL}meetingcall/`, data);
  }

  getMeetingCallById(id: number): Observable<any> {
    return this.http.get(`${this.apiURL}meetingcall/${id}/`);
  }

  updateMeetingCall(id: number, data: any): Observable<any> {
    return this.http.put(`${this.apiURL}meetingcall/${id}/`, data);
  }

  deleteMeetingCall(id: number): Observable<any> {
    return this.http.delete(`${this.apiURL}meetingcall/${id}/`);
  }

  // MeetingProtocol endpoints
  getMeetingProtocols(): Observable<any> {
    return this.http.get(`${this.apiURL}meetingprotocol/`);
  }

  createMeetingProtocol(data: any): Observable<any> {
    return this.http.post(`${this.apiURL}meetingprotocol/`, data);
  }

  getMeetingProtocolById(id: number): Observable<any> {
    return this.http.get(`${this.apiURL}meetingprotocol/${id}/`);
  }

  updateMeetingProtocol(id: number, data: any): Observable<any> {
    return this.http.put(`${this.apiURL}meetingprotocol/${id}/`, data);
  }

  deleteMeetingProtocol(id: number): Observable<any> {
    return this.http.delete(`${this.apiURL}meetingprotocol/${id}/`);
  }

  // CallRecord endpoints
  getCallRecords(): Observable<any> {
    return this.http.get(`${this.apiURL}callrecord/`);
  }

  createCallRecord(data: any): Observable<any> {
    return this.http.post(`${this.apiURL}callrecord/`, data);
  }

  getCallRecordById(id: number): Observable<any> {
    return this.http.get(`${this.apiURL}callrecord/${id}/`);
  }

  updateCallRecord(id: number, data: any): Observable<any> {
    return this.http.put(`${this.apiURL}callrecord/${id}/`, data);
  }

  deleteCallRecord(id: number): Observable<any> {
    return this.http.delete(`${this.apiURL}callrecord/${id}/`);
  }
}
