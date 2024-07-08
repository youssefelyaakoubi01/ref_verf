import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthComponent } from './auth/auth.component';
import { HeaderComponent } from './header/header.component';
import { AffaireComponent } from './affaire/affaire.component';
import { HomeComponent } from './home/home.component';
import { VerifyAffComponent } from './verify-aff/verify-aff.component';
import { ChatLlmComponent } from './chat-llm/chat-llm.component';


const routes: Routes = [
  { path: 'auth', component: AuthComponent },
  { path: 'home', component: HomeComponent },
  { path: 'createAff', component: AffaireComponent },
  { path: 'verifyAff', component: VerifyAffComponent },
  { path: 'chatllm', component: ChatLlmComponent },
  
 
 

  // Ajoutez d'autres routes ici si nécessaire
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
