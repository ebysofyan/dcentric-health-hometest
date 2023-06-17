import axios from "axios";
import { AxiosResponse } from "axios";
import { BASE_URL } from "../constants";
import { RoomIface } from "../ifaces/room.iface";
import { ChatIface } from "../ifaces/chat.iface";

export const getAllChatByRoomId = (
  roomId: string | string[]
): Promise<AxiosResponse<ChatIface[], any>> => {
  return axios.get(`${BASE_URL}/chats/${roomId}`);
};
