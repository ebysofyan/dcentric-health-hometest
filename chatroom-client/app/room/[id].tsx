import * as React from "react";
import { useRouter, useSearchParams } from "expo-router";
import { Text, View } from "react-native";
import { getAllChatByRoomId } from "../../api/Chat";
import { ChatIface } from "../../ifaces/ChatIface";

export default function ChatRoom() {
    const { id } = useSearchParams();
    const [chats, setChats] = React.useState([])

    React.useEffect(() => {
        const fetchChat = async () => {
            const result = await getAllChatByRoomId(id)
            setChats(result.data)
        }
        fetchChat()
    }, [id])
    const ChatView = (chat: ChatIface, index: number) => {
        return (
            <Text key={index}>{chat.text}</Text>
        )
    }
    return (
        <View>
            {chats.map((chat, index) => ChatView(chat, index))}
        </View>
    )
}