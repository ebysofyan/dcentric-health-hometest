import axios from "axios";
import { AxiosResponse } from "axios";
import { BASE_URL } from "../constants";
import { RoomIface } from "../ifaces/RoomIface";
import { ChatIface } from "../ifaces/ChatIface";

export const getAllChatByRoomId = (
  roomId: string | string[]
): Promise<AxiosResponse<ChatIface[], any>> => {
  return axios.get(`${BASE_URL}/chats/${roomId}`);
};
