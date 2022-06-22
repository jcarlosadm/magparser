export class Filter {
    startDate : Date | null;
    endDate : Date | null;
    searchTerm : string;

    constructor(startDate:Date, endDate:Date, searchTerm:string){
        this.startDate = startDate;
        this.endDate = endDate;
        this.searchTerm = searchTerm;
    }
}