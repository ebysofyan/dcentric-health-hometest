import { UserIface } from "./User";

export interface RoomIface {
  id: number;
  name: string;
  encryption_key: string;
  user: UserIface;
}
