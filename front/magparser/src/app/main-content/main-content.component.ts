import { Component, Input, OnInit } from '@angular/core';
import { Magazine } from '../content/magazine';

@Component({
  selector: 'page-content',
  templateUrl: './main-content.component.html',
  styleUrls: ['./main-content.component.css']
})
export class MainContentComponent implements OnInit {

  @Input() selectedTopic:string = "";
  @Input() startDate:Date|null = null;
  @Input() endDate:Date|null = null;
  @Input() searchTerm:string|null = null;

  magazines:Magazine[];
  currentPage:Number = 1;
  hasNextPage:Boolean = false;
  maxContentPerPage:Number = 10;

  constructor() {
    // run service to get mags
    this.magazines = [new Magazine("mag1"), new Magazine("mag2")];
  }

  ngOnInit(): void {
  }

}
