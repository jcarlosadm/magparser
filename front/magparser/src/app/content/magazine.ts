export class Magazine {
    title:string = "";
    category:string = "";
    date:string = "";
    img:string = "";
    post_url:string = "";
    language:string = "";
    pages:string = "";
    type:string = "";
    size:string = "";
    download_url:string = "";

    constructor(
        title:string,
        category:string,
        date:string,
        img:string,
        post_url:string,
        language:string,
        pages:string,
        type:string,
        size:string,
        download_url:string
    ){
        this.title = title;
        this.category = category;
        this.date = date;
        this.img = img;
        this.post_url = post_url;
        this.language = language;
        this.pages = pages;
        this.type = type;
        this.size = size;
        this.download_url = download_url;
    }
}