export interface Source {
  title: string;
  url: string;
}

export interface ChatResponse {
  answer: string;
  confidence: number;
  sources: Source[];
}

export interface ChatRequest {
  question: string;
}