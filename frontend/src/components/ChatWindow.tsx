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

        <main className="flex-1 overflow-y-auto p-8">

            <div className="mx-auto max-w-4xl">

                {!response && !loading && (

                    <div className="rounded-xl bg-white p-8 shadow">

                        Ask me anything about your documentation.

                    </div>

                )}

                {loading && (

                    <div className="rounded-xl bg-white p-8 shadow">

                        Thinking...

                    </div>

                )}

                {response && (

                    <div className="space-y-6">

                        <div className="rounded-xl bg-white p-8 shadow">

                            <h2 className="mb-4 text-xl font-bold">

                                Answer

                            </h2>

                            <p className="whitespace-pre-wrap leading-8">

                                {response.answer}

                            </p>

                        </div>

                        <div className="rounded-xl bg-white p-6 shadow">

                            <strong>

                                Confidence:

                            </strong>{" "}

                            {(response.confidence * 100).toFixed(1)}%

                        </div>

                        <div className="rounded-xl bg-white p-6 shadow">

                            <h3 className="mb-4 text-lg font-bold">

                                Sources

                            </h3>

                            {response.sources.map((source) => (

                                <div
                                    key={source.url}
                                    className="mb-3"
                                >

                                    <a
                                        href={source.url}
                                        target="_blank"
                                        rel="noreferrer"
                                        className="text-blue-600 hover:underline"
                                    >

                                        {source.title}

                                    </a>

                                </div>

                            ))}

                        </div>

                    </div>

                )}

            </div>

        </main>

    );

}