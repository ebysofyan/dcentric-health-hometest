import axios from "axios";
import { AxiosResponse } from "axios";
import { BASE_URL } from "../constants";
import { RoomIface } from "../ifaces/RoomIface";
export const createNewRoom = (
  name: string
): Promise<AxiosResponse<RoomIface, any>> => {
  return axios.post(`${BASE_URL}/rooms`, {
    name: name,
    creator_id: null,
  });
};

export const joinRoom = (name: string): Promise<AxiosResponse<RoomIface>> => {
  return axios.post(`${BASE_URL}/rooms/join`, {
    name: name,
  });
};

export const getAllRooms = (
  name: string
): Promise<AxiosResponse<RoomIface[]>> => {
  return axios.get(`${BASE_URL}/rooms`);
};
