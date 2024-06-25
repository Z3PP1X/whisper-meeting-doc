import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegisterMeetingComponent } from './register-meeting.component';

describe('RegisterMeetingComponent', () => {
  let component: RegisterMeetingComponent;
  let fixture: ComponentFixture<RegisterMeetingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RegisterMeetingComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RegisterMeetingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
