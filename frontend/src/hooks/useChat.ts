import { useState } from "react";
import api from "../api/client";
import type {
    ChatRequest,
    ChatResponse,
} from "../types/chat";

export function useChat() {

    const [loading, setLoading] = useState(false);

    const [response, setResponse] =
        useState<ChatResponse | null>(null);

    async function ask(question: string) {

        setLoading(true);

        try {

            const payload: ChatRequest = {
                question,
            };

            const res = await api.post<ChatResponse>(
                "/chat",
                payload,
            );

            setResponse(res.data);

        } finally {

            setLoading(false);

        }
    }

    return {
        ask,
        loading,
        response,
    };
}