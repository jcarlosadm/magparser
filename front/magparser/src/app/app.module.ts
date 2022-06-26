import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ControlsComponent } from './controls/controls.component';
import { MainContentComponent } from './main-content/main-content.component';
import { PaginationComponent } from './pagination/pagination.component';
import { ContentComponent } from './content/content.component';
import { MagazineService } from './main-content/magazine-service.service';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    ControlsComponent,
    MainContentComponent,
    PaginationComponent,
    ContentComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [MagazineService],
  bootstrap: [AppComponent]
})
export class AppModule { }
