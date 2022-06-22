import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'pagination',
  templateUrl: './pagination.component.html',
  styleUrls: ['./pagination.component.css']
})
export class PaginationComponent implements OnInit {

  @Input() currentPage:Number = 1;
  @Input() hasNext:Boolean = false;

  constructor() { }

  ngOnInit(): void {
  }

}
