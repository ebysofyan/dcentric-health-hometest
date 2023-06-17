import 'react-native-get-random-values';
import CryptoJS from "crypto-js";

export const encrypt = ({ plaintext, encryptionKey }) =>
  CryptoJS.AES.encrypt(plaintext, encryptionKey).toString();
export const decrypt = ({ ciphertext, encryptionKey }) =>
  CryptoJS.AES.decrypt(ciphertext, encryptionKey).toString(CryptoJS.enc.Utf8)
