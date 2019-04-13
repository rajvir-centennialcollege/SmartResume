import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import {StepsModule} from 'primeng/steps';
import {MenuItem} from 'primeng/api';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule , StepsModule ,BrowserAnimationsModule ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
