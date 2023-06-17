export interface ChatSenderIface {
  id: number;
  name: string;
}
export interface ChatIface {
  text: string;
  room_id: number;
  sender: ChatSenderIface;
  created_at: string;
}
