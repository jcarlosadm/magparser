import { Component, OnInit } from '@angular/core';
import { Filter } from './filter';

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
  filter:Filter;

  constructor() {
    this.topics =  ['All','Science', 'Computer'];
    
    if (this.topics.length > 0)
      this.selectedTopic = this.topics[0];
    else
      this.selectedTopic = '';
    
    this.startDate = new Date();
    this.startDate.setDate(this.startDate.getDate() - 5);

    this.endDate = new Date();

    this.filter = new Filter(this.startDate, this.endDate, this.searchTerm);
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

  setFilter() {
    this.filter.startDate = this.startDate;
    this.filter.endDate = this.endDate;
    this.filter.searchTerm = this.searchTerm;
  }
}
