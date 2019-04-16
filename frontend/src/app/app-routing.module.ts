import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';

import { RegLoginComponent } from './reg-login/reg-login.component'
import { UpdateApplicantProfileComponent } from './update-applicant-profile/update-applicant-profile.component';
import { PostjobComponent } from './postjob/postjob.component';



const routes: Routes = [
  { path: '', component: RegLoginComponent },
  { path: 'update_applicant_profile', component: UpdateApplicantProfileComponent },
  { path: 'postjob', component: PostjobComponent },
];

@NgModule({

  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {


 }
