import axios from "axios";
import { AxiosResponse } from "axios";
import { BASE_URL } from "../constants";
import { RoomIface } from "../ifaces/Room";
import { ChatIface } from "../ifaces/Chat";

export const getAllChatByRoomId = (
  roomId: string | string[]
): Promise<AxiosResponse<ChatIface[], any>> => {
  return axios.get(`${BASE_URL}/chats/${roomId}`);
};
