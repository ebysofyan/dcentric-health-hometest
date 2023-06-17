import { UserIface } from "./user.iface";

export interface RoomIface {
  id: number;
  name: string;
  encryption_key: string;
  user: UserIface;
}
