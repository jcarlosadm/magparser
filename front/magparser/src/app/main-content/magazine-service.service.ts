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
    let params = new HttpParams();
    params = params.set('selectedTopic', searchObj.selectedTopic);
    params = params.set('startDate', searchObj.startDate);
    params = params.set('endDate', searchObj.endDate);
    params = params.set('searchTerm', searchObj.searchTerm);
    params = params.set('currentPage', searchObj.currentPage);
    params = params.set('maxContentPerPage', searchObj.maxContentPerPage);

    return this.http.get<Magazine[]>(`${this.api}/api/get_mags`, { params : params });
  }

  getTopics() {
    return this.http.get<string[]>(`${this.api}/api/get_topics`);
  }
}
