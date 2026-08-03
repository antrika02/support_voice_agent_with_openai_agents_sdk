import { useState } from "react";

interface Props {
    onSend(question: string): void;
    loading: boolean;
}

export default function ChatInput({
    onSend,
    loading,
}: Props) {

    const [question, setQuestion] = useState("");

    function submit() {

        if (!question.trim()) return;

        onSend(question);

        setQuestion("");
    }

    return (

        <div className="border-t bg-white p-6">

            <div className="mx-auto flex max-w-4xl gap-4">

                <input
                    value={question}
                    onChange={(e) =>
                        setQuestion(e.target.value)
                    }
                    onKeyDown={(e) => {
                        if (e.key === "Enter") {
                            submit();
                        }
                    }}
                    placeholder="Ask a question..."
                    className="flex-1 rounded-lg border border-gray-300 p-4 focus:border-blue-500 focus:outline-none"
                />

                <button
                    onClick={submit}
                    disabled={loading}
                    className="rounded-lg bg-blue-600 px-6 py-3 text-white transition hover:bg-blue-700 disabled:opacity-50"
                >
                    {loading ? "Thinking..." : "Send"}
                </button>

            </div>

        </div>

    );

}