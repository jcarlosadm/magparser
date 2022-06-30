import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'pagination',
  templateUrl: './pagination.component.html',
  styleUrls: ['./pagination.component.css']
})
export class PaginationComponent {

  @Input() currentPage:number = 1;
  @Input() hasNext:Boolean = false;
  @Output() pageChanged = new EventEmitter();

  constructor() { }

  increment(){
    this.currentPage++;
    this.pageChanged.emit({currentPage:this.currentPage});
  }

  decrement(){
    this.currentPage--;
    this.pageChanged.emit({currentPage:this.currentPage});
  }
}
