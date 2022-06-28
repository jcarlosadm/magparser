import { Component, OnInit } from '@angular/core';
import { MagazineService } from '../main-content/magazine-service.service';
import { Filter } from './filter';

@Component({
  selector: 'controls',
  templateUrl: './controls.component.html',
  styleUrls: ['./controls.component.css']
})
export class ControlsComponent implements OnInit {

  topics:string[] = [];
  selectedTopic:string = '';
  startDate:Date;
  endDate:Date;
  searchTerm:string = "";
  filter:Filter;

  constructor(private magService:MagazineService) {
    this.startDate = new Date();
    this.startDate.setDate(this.startDate.getDate() - 5);

    this.endDate = new Date();

    this.filter = new Filter(this.startDate, this.endDate, this.searchTerm);
  }

  ngOnInit(): void {
    this.getTopics();
  }

  getTopics() {
    this.magService.getTopics({
      startDate:this.startDate.toISOString().slice(0, 10), 
      endDate:this.endDate.toISOString().slice(0, 10)
    })
    .subscribe((data:string[]) => {
      this.topics = data;
      if (this.topics.length > 0){
        this.selectedTopic = this.topics[0];
      } else {
        this.selectedTopic = "";
      }
    });
  }

  setStartDate(date:Date | null){
    if (date != null && date.toISOString() != this.startDate.toISOString()){
      this.startDate = date;
      this.getTopics();
    }
  }

  setEndDate(date:Date | null) {
    if (date != null && date.toISOString() != this.endDate.toISOString()){
      this.endDate = date;
      this.getTopics();
    }
  }

  setTopic(value:string | null) {
    if (value != null) {
      this.selectedTopic = value;
      this.searchTerm = "";
      this.setFilter();
    }
  }

  setFilter() {
    this.filter.startDate = this.startDate;
    this.filter.endDate = this.endDate;
    this.filter.searchTerm = this.searchTerm;
  }
}
