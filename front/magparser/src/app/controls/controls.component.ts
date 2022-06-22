import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'controls',
  templateUrl: './controls.component.html',
  styleUrls: ['./controls.component.css']
})
export class ControlsComponent implements OnInit {

  topics:string[];
  selectedTopic:string;
  startDate:Date;
  endDate:Date;
  searchTerm:string = "";

  constructor() {
    this.topics =  ['All','Science', 'Computer'];
    
    if (this.topics.length > 0)
      this.selectedTopic = this.topics[0];
    else
      this.selectedTopic = '';
    
    this.startDate = new Date();
    this.startDate.setDate(this.startDate.getDate() - 5);

    this.endDate = new Date();
  }

  ngOnInit(): void {
  }

  setStartDate(date:Date | null){
    if (date != null){
      this.startDate = date;
    }
  }

  setEndDate(date:Date | null) {
    if (date != null){
      this.endDate = date;
    }
  }

  setTopic(value:string | null) {
    if (value != null) {
      this.selectedTopic = value;
    }
  }
}
