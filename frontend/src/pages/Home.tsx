import Header from "../components/Header";
import Sidebar from "../components/Sidebar";
import ChatInput from "../components/ChatInput";
import ChatWindow from "../components/ChatWindow";

import { useChat } from "../hooks/useChat";

export default function Home() {

    const {
        ask,
        loading,
        response,
    } = useChat();

    return (

        <div className="flex h-screen bg-slate-100">

            <Sidebar />

            <div className="flex flex-1 flex-col">

                <Header />

                <ChatWindow
                    loading={loading}
                    response={response}
                />

                <ChatInput
                    onSend={ask}
                    loading={loading}
                />

            </div>

        </div>

    );

}