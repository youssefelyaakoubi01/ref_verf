import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { LlmService } from '../services/llm.service';
import { Message } from '../models/message';

@Component({
  selector: 'app-chat-llm',
  templateUrl: './chat-llm.component.html',
  styleUrls: ['./chat-llm.component.css'],
})
export class ChatLlmComponent implements OnInit {
  chat_form!: FormGroup;
  response!: any;
  questionStatus: boolean = false;
  messages: Message[] = [
    {
      question: 'Bonjour',
      answer: 'Bonjour! comment peux-je vous aider?',
    },
  ];

  constructor(
    private formBuilder: FormBuilder,
    private chatservice: LlmService
  ) {}

  ngOnInit(): void {
    this.chat_form = this.formBuilder.group({
      question:  ['',[Validators.required, Validators.minLength(15)]],
      llm_type: ['', Validators.required],
      language: ['', Validators.required],
    });
  }

  ask_chatbot() {
    const question = this.chat_form.value.question;
    this.questionStatus = true;
    if (this.chat_form.value.llm_type == '1' && this.chat_form.value.language == 'fr' ) {
      this.chatservice
        .Askllm(question)
        .subscribe((response) => {
          if (response) {
            this.questionStatus = false;
            const nouveauMessage: Message = {
              question: question,
              answer: response,
            };
            this.chat_form.reset();
            this.messages.push(nouveauMessage);
          }
        });
    } else if (this.chat_form.value.llm_type == '2'  ) {
      const contexte =
        'Question:' +
        this.chat_form.value.question +
        '\n \n Conversation précedente:' +
       JSON.stringify(this.messages);
      console.log(contexte);
      
      this.chatservice.chatllm(contexte).subscribe((response) => {
        if (response) {
          this.questionStatus = false;
          const nouveauMessage: Message = {
            question: question,
            answer: response,
          };
          
          this.messages.push(nouveauMessage);
          this.chat_form.reset({ 'question':''});
          
        }
      });
    }
    else if (this.chat_form.value.language == 'ar' && this.chat_form.value.llm_type == 1){
      this.chatservice
        .chatllm_ar(question)
        .subscribe((response) => {
          if (response) {
            this.questionStatus = false;
            const nouveauMessage: Message = {
              question: question,
              answer: response,
            };
            this.chat_form.reset();
            this.messages.push(nouveauMessage);
          }
        });

    }
  }
  clearConversation(){
    this.messages.splice(0, this.messages.length)
  }
}
