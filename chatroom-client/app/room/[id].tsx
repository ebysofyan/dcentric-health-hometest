import * as React from "react";
import { Stack, useGlobalSearchParams } from "expo-router";
import {
    Text,
    View,
    StyleSheet,
    SafeAreaView,
    TouchableOpacity,
    FlatList,
    TextInputKeyPressEventData,
    NativeSyntheticEvent,
} from "react-native";
import { getAllChatByRoomId } from "../../api/Chat";
import { ChatIface } from "../../ifaces/Chat";
import { TextInput } from "react-native-gesture-handler";
import useWebSocket, { ReadyState } from "react-use-websocket";
import { WS_URL } from "../../constants";
import { decrypt, encrypt } from "../../utils/chiper-utils";

export default function ChatRoom() {
    const { id, userId, encryptionKey } = useGlobalSearchParams();
    const flatListRef = React.useRef<FlatList>();
    const [chats, setChats] = React.useState([]);
    const [message, setMessage] = React.useState("");

    // const [socketUrl, setSocketUrl] = React.useState();
    const { sendJsonMessage, lastJsonMessage, readyState } = useWebSocket(
        WS_URL.concat(`/ws/${id}`),
        {
            onOpen: () => console.log("opened"),
            shouldReconnect: (closeEvent) => true,
        }
    );
    const connectionStatus = {
        [ReadyState.CONNECTING]: "Connecting",
        [ReadyState.OPEN]: "Open",
        [ReadyState.CLOSING]: "Closing",
        [ReadyState.CLOSED]: "Closed",
        [ReadyState.UNINSTANTIATED]: "Uninstantiated",
    }[readyState];

    React.useEffect(() => {
        if (lastJsonMessage !== null) {
            setChats((prev) => prev.concat(lastJsonMessage));
        }
    }, [lastJsonMessage, setChats]);

    React.useEffect(() => {
        const fetchChat = async () => {
            const result = await getAllChatByRoomId(id);
            setChats(result.data);
        };
        fetchChat();
    }, [id]);
    const getSafeMessage = (chat: ChatIface): string => {
        try {
            return decrypt({ ciphertext: chat.text, encryptionKey: encryptionKey })
        } catch (error) {
            return "Unsupported message"
        }
    }
    const ChatItemView = (chat: ChatIface, index: number) => {
        const isSender = userId.toString() === chat.sender.id.toString();
        return (
            <View
                key={index}
                style={{
                    ...styles.chatItem,
                    alignSelf: isSender ? "flex-end" : "flex-start",
                    backgroundColor: isSender ? "#6F8FAF" : "#088F8F",
                }}
            >
                <Text style={styles.chatItemSender}>{isSender ? "You" : chat.sender.name}</Text>
                <Text style={styles.chatItemContent}>{getSafeMessage(chat)}</Text>
                <Text style={styles.chatItemTime}>
                    {chat.created_at}
                </Text>
            </View>
        );
    };

    const handleSendPress = () => {
        if (Boolean(message)) {
            console.log(id)
            sendJsonMessage({
                text: encrypt({ plaintext: message, encryptionKey: encryptionKey }),
                sender_id: userId.toString(),
            });
            setMessage("");
        }
    };
    const handleKeyPress = (e: NativeSyntheticEvent<TextInputKeyPressEventData>) => {
        if (e.nativeEvent.key === "Enter") {
            handleSendPress()
        }
    }
    return (
        <SafeAreaView style={styles.container}>
            <Stack.Screen
                options={{
                    title: "Chat Room",
                }}
            />
            <Text style={{ textAlign: "center", padding: 4 }}>
                Connction status : {connectionStatus}
            </Text>
            <FlatList
                ref={flatListRef}
                style={styles.scrollview}
                data={chats}
                renderItem={({ item, index }) => ChatItemView(item, index)}
                onContentSizeChange={() => chats.length > 0 && flatListRef.current.scrollToEnd({ animated: true })}
            />
            <View style={styles.chatInputContainer}>
                <TextInput
                    style={styles.chatInput}
                    placeholder="Type something..."
                    onChange={(e) => setMessage(e.nativeEvent.text)}
                    value={message}
                    onSubmitEditing={handleSendPress}
                />
                <TouchableOpacity style={styles.buttonSend} onPress={handleSendPress}>
                    <Text>Send</Text>
                </TouchableOpacity>
            </View>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        gap: 8,
    },
    scrollview: {
        paddingHorizontal: 12,
        paddingTop: 24,
        paddingBottom: 32,
    },
    chatContainer: {
        flex: 1,
        gap: 8,
    },
    chatItem: {
        display: "flex",
        maxWidth: 250,
        minWidth: 50,
        paddingHorizontal: 12,
        paddingVertical: 8,
        borderRadius: 8,
        borderColor: "transparent",
        fontWeight: "600",
        marginBottom: 8,
        gap: 4
    },
    chatItemSender: { color: "white", fontWeight: "200", fontSize: 14, marginBottom: 4 },
    chatItemContent: { color: "white", fontWeight: "600" },
    chatItemTime: { fontSize: 10, alignSelf: "flex-end", color: "white" },
    chatInputContainer: {
        flexDirection: "row",
        flexShrink: 0,
        alignItems: "center",
        borderTopColor: "gray",
        borderBottomColor: "transparent",
        borderRightColor: "transparent",
        borderLeftColor: "transparent",
        borderStyle: "solid",
        borderWidth: 1,
        paddingHorizontal: 16,
        gap: 8,
    },
    chatInput: {
        flex: 1,
        height: 55,
        paddingVertical: 8,
    },
    buttonSend: {
        flexShrink: 0,
        fontSize: 16,
        fontWeight: "600",
        color: "black",
    },
});
