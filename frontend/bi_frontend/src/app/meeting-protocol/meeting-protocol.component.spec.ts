import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MeetingProtocolComponent } from './meeting-protocol.component';

describe('MeetingProtocolComponent', () => {
  let component: MeetingProtocolComponent;
  let fixture: ComponentFixture<MeetingProtocolComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MeetingProtocolComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MeetingProtocolComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
