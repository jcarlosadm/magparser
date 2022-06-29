import { Component, OnInit } from '@angular/core';
import { MagazineService } from '../main-content/magazine-service.service';
import { Filter } from './filter';

@Component({
  selector: 'controls',
  templateUrl: './controls.component.html',
  styleUrls: ['./controls.component.css']
})
export class ControlsComponent implements OnInit {

  topics:any = {};
  selectedTopic:string = 'All';
  startDate:Date | null = null;
  endDate:Date | null = null;
  searchTerm:string = "";
  filter:Filter;

  constructor(private magService:MagazineService) {
    this.filter = new Filter(this.startDate, this.endDate, this.searchTerm);
  }

  ngOnInit(): void {
    this.getTopics();
  }

  getTopics() {
    this.magService.getTopics()
    .subscribe((data:string[]) => {
      this.topics = data;
      if (Object.keys(this.topics).length > 0){
        this.selectedTopic = Object.keys(this.topics)[0];
      } else {
        this.selectedTopic = "All";
      }
    });
  }

  setStartDate(date:Date | null){
    if ((date != null && this.startDate != null && date.toISOString() != 
        this.startDate.toISOString()) || (date != null && this.startDate == null) ||
        (date == null && this.startDate != null)){
      this.startDate = date;
      this.getTopics();
    }
  }

  setEndDate(date:Date | null) {
    if ((date != null && this.endDate != null && date.toISOString() !=
         this.endDate.toISOString()) || (date != null && this.endDate == null) ||
         (date == null && this.endDate != null)){
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
