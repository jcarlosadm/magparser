import { Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { Magazine } from '../content/magazine';
import { MagazineService } from './magazine-service.service';

@Component({
  selector: 'page-content',
  templateUrl: './main-content.component.html',
  styleUrls: ['./main-content.component.css']
})
export class MainContentComponent implements OnChanges {
  @Input() selectedTopic:string = "";
  @Input() startDate:Date|null = null;
  @Input() endDate:Date|null = null;
  @Input() searchTerm:string|null = null;

  magazines:Magazine[] = [];
  currentPage:number = 1;
  hasNextPage:Boolean = false;
  maxContentPerPage:Number = 10;

  constructor(private magazineService:MagazineService) {
    this.getMags();
  }

  private createSearchObj(){
    return {
      selectedTopic: this.selectedTopic,
      startDate: this.startDate,
      endDate: this.endDate,
      searchTerm: this.searchTerm,
      currentPage: this.currentPage,
      maxContentPerPage: this.maxContentPerPage
    };
  }

  getMags(event:any = null){
    if (event != null){
      this.currentPage = event.currentPage;
    }

    var resultObj = this.magazineService.getMags(this.createSearchObj());
    this.magazines = resultObj.mags;
    this.hasNextPage = resultObj.hasNextPage;
  }

  ngOnChanges(changes: SimpleChanges): void {
    if ('selectedTopic' in changes || 'startDate' in changes ||
        'endDate' in changes || 'searchTerm' in changes){
      this.currentPage = 1;
      this.getMags();
    }
  }
}
