import { Component, Input, OnInit } from '@angular/core';
import { Magazine } from './magazine';

@Component({
  selector: 'magazine',
  templateUrl: './content.component.html',
  styleUrls: ['./content.component.css']
})
export class ContentComponent implements OnInit {

  @Input() magazine:Magazine|null = null;

  constructor() { }

  ngOnInit(): void {
  }

}
