import ConfidenceBar from "./ConfidenceBar";
import type { ChatResponse } from "../types/chat";

interface Props {

    loading: boolean;

    response: ChatResponse | null;

}

export default function ChatWindow({
    loading,
    response,
}: Props) {

    return (

        <main className="flex-1 overflow-y-auto bg-slate-100 p-8">

            <div className="mx-auto w-full max-w-6xl">

                {!response && !loading && (

                    <div className="rounded-xl bg-white p-10 shadow">

                        <h2 className="mb-4 text-3xl font-bold">

                            👋 Welcome to the AI Documentation Assistant

                        </h2>

                        <p className="mb-6 text-gray-600">

                            Ask questions about your documentation and receive
                            grounded answers generated using Retrieval-Augmented
                            Generation (RAG) with source citations.

                        </p>

                        <div className="space-y-2">

                            <p className="font-semibold">

                                Try asking:

                            </p>

                            <ul className="list-disc space-y-2 pl-6 text-gray-700">

                                <li>
                                    What is Stripe?
                                </li>

                                <li>
                                    How do webhooks work?
                                </li>

                                <li>
                                    How do I test payments?
                                </li>

                            </ul>

                        </div>

                    </div>

                )}

                {loading && (

                    <div className="rounded-xl bg-white p-10 shadow">

                        <h2 className="mb-4 text-2xl font-bold">

                            Thinking...

                        </h2>

                        <p className="text-gray-600">

                            Searching documentation and generating an answer...

                        </p>

                    </div>

                )}

                {response && (

                    <div className="space-y-6">

                        <div className="rounded-xl bg-white p-8 shadow">

                            <h2 className="mb-4 text-2xl font-bold">

                                Answer

                            </h2>

                            <p className="whitespace-pre-wrap leading-8 text-gray-800">

                                {response.answer}

                            </p>

                        </div>

                        <div className="rounded-xl bg-white p-6 shadow">

                            <ConfidenceBar
                                confidence={response.confidence}
                            />

                        </div>

                        <div className="rounded-xl bg-white p-6 shadow">

                            <h2 className="mb-4 text-2xl font-bold">

                                Sources

                            </h2>

                            <div className="space-y-4">

                                {response.sources.map((source) => (

                                    <div
                                        key={source.url}
                                        className="rounded-lg border border-gray-200 p-4 hover:bg-gray-50"
                                    >

                                        <a
                                            href={source.url}
                                            target="_blank"
                                            rel="noreferrer"
                                            className="font-semibold text-blue-600 hover:underline"
                                        >

                                            {source.title}

                                        </a>

                                        <p className="mt-2 break-all text-sm text-gray-500">

                                            {source.url}

                                        </p>

                                    </div>

                                ))}

                            </div>

                        </div>

                    </div>

                )}

            </div>

        </main>

    );

}