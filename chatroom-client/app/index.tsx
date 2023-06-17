import * as React from "react";
import {
    Button,
    Pressable,
    StyleSheet,
    Text,
    TextInput,
    View,
} from "react-native";
import { createNewRoom, joinRoom } from "../api/room.api";
import { Stack, useRouter } from "expo-router";

export default function Index() {
    const router = useRouter();
    const [newRoom, setNewRoom] = React.useState("");
    const [existingRoom, setExistingRoomName] = React.useState("");
    const [createRoomLoading, setCreateRoomLoading] = React.useState(false);
    const [joinRoomLoading, setJoinRoomLoading] = React.useState(false);

    const resetInput = () => {
        setNewRoom("");
        setExistingRoomName("");
    };

    const handleCreateNewRoomClick = async () => {
        setCreateRoomLoading(true);
        try {
            const room = await createNewRoom(newRoom);
            router.push({
                pathname: "room/[id]",
                params: {
                    id: room.data.id,
                    userId: room.data.user.id,
                    encryptionKey: room.data.encryption_key,
                },
            });
            resetInput();
        } catch (error) {
            alert(error.message);
        }
        setCreateRoomLoading(false);
    };
    const handleJoinExistingRoomClick = async () => {
        setJoinRoomLoading(true);
        try {
            const room = await joinRoom(existingRoom);
            router.push({
                pathname: "room/[id]",
                params: {
                    id: room.data.id,
                    userId: room.data.user.id,
                    encryptionKey: room.data.encryption_key,
                },
            });
            resetInput();
        } catch (error) {
            alert(error.message);
        }
        setJoinRoomLoading(false);
    };
    return (
        <View style={styles.container}>
            <Stack.Screen
                options={{
                    title: "Home",
                }}
            />
            <Text>Create room #{newRoom}</Text>
            <View style={styles.inputWrapper}>
                <TextInput
                    placeholder="Enter room name"
                    style={styles.input}
                    onChange={(e) => setNewRoom(e.nativeEvent.text)}
                    value={newRoom}
                />
                <Pressable
                    style={{ ...styles.button, backgroundColor: "#4682B4" }}
                    onPress={handleCreateNewRoomClick}
                >
                    <Text style={styles.textButton}>
                        {createRoomLoading ? "Creating..." : "Create"}
                    </Text>
                </Pressable>
            </View>
            <Text>Or join room #{existingRoom}</Text>
            <View style={styles.inputWrapper}>
                <TextInput
                    placeholder="Enter existing room name"
                    style={styles.input}
                    onChange={(e) => setExistingRoomName(e.nativeEvent.text)}
                    value={existingRoom}
                />
                <Pressable
                    style={{ ...styles.button, backgroundColor: "#40B5AD" }}
                    onPress={handleJoinExistingRoomClick}
                >
                    <Text style={styles.textButton}>
                        {joinRoomLoading ? "Joining..." : "Join"}
                    </Text>
                </Pressable>
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        gap: 12,
        flexDirection: "column",
        backgroundColor: "#fff",
        padding: 32,
    },
    inputWrapper: {
        flexDirection: "row",
        alignItems: "center",
        gap: 16,
    },
    input: {
        flex: 1,
        maxWidth: "100%",
        height: 55,
        fontSize: 16,
        borderWidth: 1,
        borderColor: "grey",
        padding: 12,
        borderRadius: 4,
    },
    button: {
        height: 55,
        width: 100,
        alignItems: "center",
        justifyContent: "center",
        paddingVertical: 12,
        paddingHorizontal: 8,
        borderRadius: 4,
        elevation: 3,
    },
    textButton: {
        fontSize: 14,
        fontWeight: "600",
        color: "white",
    },
});
