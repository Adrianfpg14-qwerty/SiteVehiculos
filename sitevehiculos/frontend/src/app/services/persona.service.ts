import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PersonaI } from '../models/persona';

@Injectable({
  providedIn: 'root',
})
export class PersonaService {
  api_uri_django = 'http://localhost:8000';
  base_path = `${this.api_uri_django}/personas/`;

  constructor(private http: HttpClient) {}

  getAllPersona(): Observable<{ personas: PersonaI[] }> {
    return this.http.get<{ personas: PersonaI[] }>(this.base_path);
  }

  getOnePersona(id: number): Observable<{ persona: PersonaI[] }> {
    return this.http.get<{ persona: PersonaI[] }>(`${this.base_path}${id}`);
  }

  createPersona(data: any): Observable<PersonaI> {
    return this.http.post<PersonaI>(this.base_path, data);
  }

  updatePersona(id: number, data: any): Observable<PersonaI> {
    console.log(id, data);
    return this.http.put<PersonaI>(`${this.base_path}${id}`, data);
  }

  deletePersona(id: number): Observable<PersonaI> {
    return this.http.delete<PersonaI>(`${this.base_path}${id}`);
  }
}
