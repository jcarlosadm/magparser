import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Magazine } from '../content/magazine';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class MagazineService {

  private readonly api = environment.api;

  constructor(private http: HttpClient) {}

  getMags(searchObj:any) {
    return {
      mags: [
        new Magazine("mag1" + searchObj.selectedTopic), 
        new Magazine("mag2" + searchObj.selectedTopic)
      ],
      hasNextPage: true
    };
  }

  getTopics() {
    return this.http.get<string[]>(`${this.api}/api/get_topics`);
  }
}
